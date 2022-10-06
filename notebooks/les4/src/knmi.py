"""Functions for getting KNMI station and temperature data."""

import io
from datetime import datetime, timedelta
from http import HTTPStatus

import numpy as np
import pandas as pd
import requests
from matplotlib.artist import get
from settings import settings


def get_hourly_temperatures(days_back: int=1, stations: list[int]=[]) -> pd.DataFrame:
    """Return a series of temperature observations (degrees Celsius) 
    of a given (set of) KNMI station(s). At least data of one full day 
    (yesterday) is returned. 
    """
    temperatures = pd.DataFrame()
    
    start_date = datetime.today() - timedelta(days=days_back)
    end_date = datetime.today() - timedelta(days=1)
    start = datetime.strftime(start_date, '%Y%m%d01')
    end = datetime.strftime(end_date, '%Y%m%d24')

    if len(stations) > 0:
        stns = ':'.join(str(s) for s in stations)
    else:
        stns = 'ALL'

    payload = {
        'start': start,
        'end': end,
        'vars': 'T',
        'stns': stns,
        'fmt': 'json'    
    }

    resp = requests.post(settings.knmi_uurgegevens_api_url, payload)
    if resp.status_code == HTTPStatus.OK:
        temperatures = pd.read_json(io.BytesIO(resp.content))
        if temperatures.shape[0] > 0:

            # Combine date and hour, convert to degrees Celsius and 
            # drop original columns.
            date_col = settings.knmi_uurgegevens_date_col
            hour_col = settings.knmi_uurgegevens_hour_col
            raw_temp_col = settings.knmi_uurgegevens_raw_temp_col
            temperatures['date_time'] = (temperatures[date_col] + 
                                        pd.to_timedelta(temperatures[hour_col], 'h'))
            temperatures['temperature_degrees_celsius'] = temperatures[raw_temp_col] / 10
            temperatures.drop(columns=[date_col, hour_col, raw_temp_col], inplace=True)
        
    return temperatures
    
    
def get_stations() -> pd.DataFrame:
    """Return KNMI weather stations metadata."""
    stations = pd.DataFrame()
    resp = requests.get(settings.knmi_stations_file_url)
    if resp.status_code == HTTPStatus.OK:
        raw_data = io.BytesIO(resp.content)
        stations = pd.DataFrame(
            pd.read_csv(raw_data, **settings.knmi_stations_import_spec)
        )
        
        # Rename columns and index. Remove spaces before actual renaming.
        stations.columns = stations.columns.str.strip()
        stations.rename(columns=settings.knmi_stations_column_mapping, inplace=True)
        stations.index.name = settings.knmi_stations_index_name
        
        # Strip white spaces from string columns.
        stations = stations.applymap(lambda c: c.strip() if isinstance(c, str) else c)
        
    return stations


def get_nearest_n_stations(stations: pd.DataFrame, latitude: float, longitude: float, 
                           n: int) -> pd.DataFrame:
    """Return the n stations that are closest to a given coordinate.
    """
    stations['dist'] = np.sqrt(
        np.power(stations.latitude - latitude, 2) + 
        np.power(stations.longitude - longitude, 2)
    )
    return stations.nsmallest(n, 'dist')
    
    
def avg_temperature_at_location(stations: pd.DataFrame, temperatures: pd.DataFrame, 
                                latitude: float, longitude: float, n: int) -> pd.DataFrame:
    """Calculate the average temperature averaged across the n nearest stations, 
    weighted by the reciproke of the distance of the stations to a given
    coordinate.
    """
    nearest_sts = get_nearest_n_stations(stations, latitude, longitude, n)
    temps = temperatures[temperatures['station_code'].isin(nearest_sts.index)]
    temps = temps.join(nearest_sts['dist'], on='station_code')
    avg_temps = temps.groupby('date_time').apply(
        lambda x: np.average(
            x['temperature_degrees_celsius'], 
            weights=1/x['dist']
        )
    )
    avg_temps.name = 'temperature_degrees_celsius'
    return pd.DataFrame(avg_temps)