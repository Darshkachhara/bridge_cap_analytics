import pandas as pd 
import numpy as np 
from pathlib import Path
from datetime import datetime
import yaml


def load_config(config_file=Path(__file__).parent.parent / 'config' / 'file_path.yaml'):
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)

def cm_build_path(date_str,base_dir):
    #please write what the function does
    #what does it use
    #what does it generate
    #why is this useful

    date = datetime.strptime(date_str,"%Y-%m-%d") #parse the date
    day = date.strftime("%d")
    month = date.strftime("%b").upper()
    year = date.strftime("%Y")

    filename = f"cm_bhavcopy_cm{day}{month}{year}bhav.csv"
    base = Path(base_dir).expanduser()
    full_path = base/ date_str/filename

    return full_path 
def get_cm_file_path(date_str):
    config = load_config
    project_root = Path(config['project_root']).expanduser()
    data_dir = config['data_dir']
    base_dir = project_root/date_dir
    return cm_build_path(date_str,base_dir)
