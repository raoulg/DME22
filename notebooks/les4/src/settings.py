from pathlib import Path

from pydantic import BaseSettings


class _Settings(BaseSettings):
    root: Path = Path("~/code/DME22/").expanduser()
    raw_data_dir: Path = Path('data/raw')
    processed_dir: Path = Path("data/processed/")
    filename: Path = Path("processed.parq")
    target: str = "species"
    knmi_uurgegevens_api_url: str = r'https://www.daggegevens.knmi.nl/klimatologie/uurgegevens'
    knmi_uurgegevens_date_col: str = 'date'
    knmi_uurgegevens_hour_col: str = 'hour'
    knmi_uurgegevens_raw_temp_col: str = 'T'
    knmi_stations_file_url: str = r'https://cdn.knmi.nl/knmi/map/page/klimatologie/gegevens/AWS_april2022_1d.txt'
    knmi_stations_import_spec: dict = {
        'sep':  '\t', 
        'encoding': 'utf-16', 
        'index_col': 'STN',
        'decimal': ',',
        'parse_dates': [1, 2],
        'infer_datetime_format': True,
        'header': 0,
        'skiprows': [1]      # Line contains --- ----
    }
    knmi_stations_column_mapping: dict = {
        'STARTT': 'start_time', 
        'STOPT': 'stop_time', 
        'LOCATIE': 'location', 
        'HOOGTE': 'height_m', 
        'POS_X': 'position_x', 
        'POS_Y': 'position_y', 
        'POS_NB': 'latitude', 
        'POS_OL': 'longitude'
    }
    knmi_stations_index_name:str = 'station_code'
    days_back: int = 3
    n_nearest_stations: int = 4
    regex_practice_file = 'BWBR0047176-geldend_van_24-09-2022_tm_heden_zichtdatum_03-10-2022.txt'

settings = _Settings()
