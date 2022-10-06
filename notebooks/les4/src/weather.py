
import knmi
import pandas as pd
import pydeck as pdk
import seaborn as sns
import streamlit as st
from geopy import Nominatim
from settings import settings

days_back = settings.days_back
n_closest_stations = settings.n_nearest_stations

# -------- Prepare station data ------------------------------------------------

stations = knmi.get_stations()
stations.drop(index=[871, 873, 990], inplace=True) # Exclude Saba, St. Eustatius and Bonaire

station_names = stations['location'].unique().tolist()
default_map_center = stations[['latitude', 'longitude']].mean()
       

# -------- Functions used on the dashboard --------------------------------------

@st.cache
def calculate_metric(temps: pd.DataFrame):
    """Return yesterday's average temperature and the delta with 
    respect to the day before.
    """
    avg_day_temps = (temps.groupby(temps['date_time'].dt.date)
                          .mean(numeric_only=True)
                          .sort_values(by='date_time', ascending=False)
                    )
    yesterday, daybefore = avg_day_temps['temperature_degrees_celsius'].values[:2]
    delta = yesterday - daybefore
    return yesterday, delta    
    
    
def geocode(search_text):
    """Find the longitude and latitude for a given location specified
    as a text.
    """
    geolocator = Nominatim(user_agent='app_dme_2022')
    location = geolocator.geocode(query=search_text)
    return location.longitude, location.latitude


def is_user_location_specified():
    """Returns true if user_location has a value in the session state.
    """
    return ('user_location' in st.session_state and
            len(st.session_state['user_location']) > 0)
    

# -------- Streamlit layout starts here ----------------------------------------


st.set_page_config(layout='wide')

# Split the title row in two columns.
title_col, metric_col = st.columns([8, 2])
with title_col:
    st.title('Weather stations in the Netherlands')
    
with metric_col:
    all_temperatures = knmi.get_hourly_temperatures(days_back)
    yesterday, delta = calculate_metric(all_temperatures)
    st.metric(
        label="Yesterday's temperature",
        value=f'{yesterday:.1f}°C',
        delta=f'{delta:.1f}°C',
        help='Average temperature of all stations compared with the day before'
    )

# The selection widget.
selected_station_names = st.multiselect(
    label='Select station(s)',
    options=station_names
)

# Filter the selected stations and their codes.
selected_stations = stations[stations['location'].isin(selected_station_names)]
station_codes = list(selected_stations.index.values)

# Load the temperatures.
temperatures = knmi.get_hourly_temperatures(days_back, station_codes)
temperatures = temperatures.join(stations['location'], on='station_code')


# -------- Find the coordinates of the location specified by the user ----------

if is_user_location_specified():
    user_coordinate = geocode(st.session_state['user_location'])
else:
    user_coordinate = []


# --------- Prepare the view state and the map layers --------------------------

if is_user_location_specified():        # Put searched location in the center.
    user_coordinate = geocode(st.session_state['user_location'])
    view_state = pdk.ViewState(         
        latitude=user_coordinate[1],
        longitude=user_coordinate[0],
        zoom=10
    )
else:
    view_state = pdk.ViewState(         # Use default map center.
        latitude=default_map_center[0],
        longitude=default_map_center[1],
        zoom=5.5
    )

all_stations_layer = pdk.Layer(         # Weather station locations.
    type='ScatterplotLayer',
    data=stations[['longitude', 'latitude']],
    get_position='[longitude,latitude]',
    radius_min_pixels=3,
    get_fill_color=[255, 0, 10],
)

selected_stations_layer = pdk.Layer(    # Highlight the selected stations.
    type='ScatterplotLayer',
    data=selected_stations[['longitude', 'latitude']],
    get_position='[longitude,latitude]',
    radius_min_pixels=10,
    get_fill_color=[255, 200, 0],
    opacity=0.4
)

if is_user_location_specified():        # Show circle at the user location.
    user_location_layer = pdk.Layer(
        type='ScatterplotLayer',
        data=[user_coordinate],
        get_position='-',
        radius_min_pixels=10,
        stroked=True,
        filled=False,
        get_line_color=[100, 100, 255],
        line_width_min_pixels=2,
        opacity=0.7
    )
else:                                   # Or else an empty layer.
    user_location_layer = pdk.Layer('ScatterplotLayer') 


# ------- Set up the column layout.

map_col, chart_col = st.columns([5, 3], gap='small')

# Left column.
with map_col:
    
    # The map.
    st.pydeck_chart(
        pdk.Deck(
            layers=[selected_stations_layer, 
                    all_stations_layer, 
                    user_location_layer], 
            initial_view_state=view_state, 
            map_style='light'
        )
    )
    # The search box.
    user_location = st.text_input(label='Search location: ', key='user_location')

# Right column.
with chart_col:
    
    # Show chart if stations are selected.
    if len(selected_station_names) > 0:
        
        # Create the plot of the selected stations' temperature.
        g = sns.lineplot(
            data=temperatures,
            x='date_time',
            y='temperature_degrees_celsius',
            hue='location',
            linewidth=0.3
        )
        # g.set_axis_labels('Date/time', 'Temperature (°C)')
        # g.set(title=f'Temperature during {days_back} day(s) at selected stations')
        
        if is_user_location_specified():
            
            # Estimate the temperature at the user location.
            avg_temp = knmi.avg_temperature_at_location(
                stations, 
                all_temperatures, 
                user_coordinate[1], 
                user_coordinate[0],
                n_closest_stations
            )
            
            # Add the estimated temperature at the user location.
            sns.lineplot(
                data=avg_temp,
                x='date_time',
                y='temperature_degrees_celsius',
                label='Search location (est.)',
                linewidth=.5,
                dashes=[5, 2]
            )
        
        # Show the plot.
        st.pyplot(g)
    else:
        st.write('No stations selected')
    



    

