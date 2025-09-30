
import pandas as pd 
import numpy as np 
from pathlib import Path
from datetime import datetime
import yaml

#Path(__file__).parent.parent / 'config' / 'file_path.yaml'
#can be used in the main function or when loading is required

def load_config(config_file):
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)

def cm_build_path(date_str,base_dir):
    #please write what the function does
    #what does it use
    #what does it generate
    #why is this useful
    #also no error checking or edge case analysis written in code

    date = datetime.strptime(date_str,"%Y-%m-%d") #parse the date
    day = date.strftime("%d")
    month = date.strftime("%b").upper()
    year = date.strftime("%Y")

    filename = f"cm_bhavcopy_cm{day}{month}{year}bhav.csv"
    base = Path(base_dir).expanduser()
    full_path = base/ date_str/filename

    return full_path 
def fo_build_path(date_str, base_dir,ftype):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    
    day = date.strftime("%d")      
    month = date.strftime("%m")    
    year = date.strftime("%Y")    
    
    if ftype == "OP":
        filename = f"fo_market_activity_op{day}{month}{year}.csv"
    else:
        filename = f"fo_market_activity_fo{day}{month}{year}.csv"
    base = Path(base_dir).expanduser()
    full_path = base / date_str / filename
    
    return full_path

def get_file_path(date_str,ftype):
    
    config = load_config
    project_root = Path(config['project_root']).expanduser()
    data_dir = config['data_dir']
    base_dir = project_root/data_dir
    if ftype == "CM":
        return cm_build_path(date_str,base_dir)
    else:
        return fo_build_path(date_str,base_dir,ftype)
def gen_trading_dates(start_date="2017-01-02",end_date=None):
    #here we assume that the start date is in 2017 and this is the first monday of the year, but this #to make a list of dates to make to make it easier to call for reports, although this function will #be used only once 
    if end_date is None:
        end_date = datetime.now().strftime("%Y-%m-%d")
    dates = pd.bdate_range(start=start_date, end=end_date)
    
    return dates.strftime("%Y-%m-%d").tolist()
def reverse_map(df):
    reverse_name={

        "SYMBOL":"symbol",	
        "SERIES":"series",
        "OPEN":"open_price",
        "HIGH":"high_price",
        "LOW":"low_price",
        "CLOSE":"close_price",
        "LAST":"last_price",
        "PREVCLOSE":"Previous_close",
        "TOTTRDQTY":"total_traded_qty",
        "TOTTRDVAL":"total_traded_value",
        "TIMESTAMP":"date",
        "TOTALTRADES":"nf_trades",
        "ISIN":"isin",
        "INSTRUMENT":"instrument",	
        "EXP_DATE":"expiry_date",  	
        "OPEN_PRICE": "open_price",
        "HI_PRICE": "high_price",
        "LO_PRICE" :"low_price",
        "CLOSE_PRICE":"close_price",
        "OPEN_INT*":"open_interest",
        "TRD_VAL":"total_traded_value",
        "TRD_QTY":"total_traded_qty",
        "NO_OF_CONT":"nf_contracts",
        "NO_OF_TRADE":"nf_trades",
        "NOTION_VAL":"notioanl_value",
        "PR_VAL":"prem_value",       
        "Index Name":"symbol",
        "Index Date":"date",
        "Open Index Value":	"open_price",
        "High Index Value":	"high_price",
        "Low Index Value":	"low_price",
        "Closing Index Value":"close_price",	
        "Points Change"	:"pts_chng",
        "Change(%)"	:"chng_pct",
        "Volume"	:"total_traded_qty",
        "Turnover (Rs. Cr.)":"total_traded_value",
        "P/E":"p/e"	,
        "P/B":"p/b"	,
        "Div Yield":"div",
    	"DATE1":"date",
        "PREV_CLOSE":"previous_close",	 
        "OPEN_PRICE":"open_price",	 
        "HIGH_PRICE":"high_price",	
        "LOW_PRICE":"low_price",	 
        "LAST_PRICE":"last_price",	 
        "CLOSE_PRICE":"close_price", 
        "AVG_PRICE":"avg_price",	 
        "TTL_TRD_QNTY":"total_traded_qty",
        "TURNOVER_LACS":"total_traded_value_lks",	 
        "NO_OF_TRADES"	 :"nf_trades",
        "DELIV_QTY"	 :"delivery_qty",
        "DELIV_PER":"delivery_qty_pct",
        "TrdDt":"trade_date",
        "BizDt":"date",	
        "Sgmt":"segment",
        "Src":"source",
        "FinInstrmTp":"instrument",
        "FinInstrmId":"instrument_id",
        "ISIN":"isin",
        "TckrSymb":"symbol",	
        "SctySrs":"",
        "XpryDt":"expiry_date",	
        "FininstrmActlXpryDt":"fin_expiry_date",
        "StrkPric":"strike_price",	
        "OptnTp":"opt_type",
        "OPT_TYPE":"opt_type",	
        "FinInstrmNm":"fin_instrument_symbol",	
        "OpnPric":"open_price",	
        "HghPric":"high_price",	
        "LwPric":"low_price",	
        "ClsPric":"close_price",	
        "LastPric":"last_price",	
        "PrvsClsgPric":"previous_close",	
        "UndrlygPric":"underlying_close_price",	
        "SttlmPric":"settlement_price",	
        "OpnIntrst":"open_interest",	
        "ChngInOpnIntrst":"chng_open_interest",	
        "TtlTradgVol":"total_traded_qty",	
        "TtlTrfVal":"total_traded_value",	
        "TtlNbOfTxsExctd":"nf_trades",	
        "SsnId":"ssnid",	
        "NewBrdLotQty":"lots"

    }
    return df.rename(columns=reverse_name)