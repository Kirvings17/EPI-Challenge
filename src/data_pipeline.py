from pathlib import Path
import pandas as pd
import uuid

def open_file(file_name):
    file_path = get_file_path(file_name)
    if file_path.suffix == ".csv":
        data = pd.read_csv(file_path, index_col=0,  na_values=["#N/A"])
    elif file_path.suffix in {".xls", ".xlsx"}:
        data = pd.read_excel(file_path, na_values=["#N/A"])
    else:
        raise TypeError("please provide a file name or path  of a file inside the data folder that is type csv, xls, or xlsx")
    return data

def get_file_path(file_name):
    file_path = Path(file_name)
    # check if path is absolute or relative
    if not file_path.is_absolute():
        base_dir = Path(__file__).resolve().parents[1]
        file_path = base_dir / "data" / file_name
    return file_path

def clean_data(data):
    # validate the data we are gettign that the colum names are what we expect...
    data=remove_duplicated_colum(data)
    # validate column name
    validate_data_format(data.columns)    
    # remove incorrect data range
    # remove incorrect datatype 
    validate_data_type(data)
    
    # remove duplicate rows
    data= data.drop_duplicates()
    
    # remove rows with missing value
    data = data.dropna()

    return data 

def validate_data_type(data):
    # validate it has 2 characters
    data["iso_a2"] = data["iso_a2"].str.upper()
    data.loc[~data["iso_a2"].str.match(r"^[A-Z]{2}$", na=False), "iso_a2"] = pd.NA
    # validate string
    for column in ["name_long","continent","region_un", "subregion","type"] :
        data[column] = data[column].astype("string").str.strip()
        data[column] = data[column].replace("", pd.NA)
        data.loc[data[column].isna(), column] = pd.NA
    # validate integers 
    for column in ["area_km2","pop","lifeExp", "gdpPercap"] :
        data[column] = pd.to_numeric(data[column], errors="coerce")
        if(column == "lifeExp" ):
            # assume max age expectancy is not more than 120 none inclusive
            data.loc[((data[column]<0)  | (data[column]>120 )), column] = pd.NA
        else:
            data.loc[data[column]<0 , column] = pd.NA


    
def remove_duplicated_colum(data): 
    # remove comuns if they are cahgne once it is loaded by renaming it
    base_names = data.columns.str.replace(r"\.\d+$", "", regex=True)
    data = data.loc[:, ~base_names.duplicated()]
    return data 

def validate_data_format(colums):
    expected_format = {"iso_a2","name_long", "continent","region_un","subregion", "type","area_km2","pop", "lifeExp","gdpPercap"}
    if (set(colums) != expected_format):
        raise ValueError("Invalid data format. The file does not contain the expected columns.")

def export_clean_data(clean_data, file_name):
    random_uuid = str(uuid.uuid4())
    file_path =get_file_path(file_name[:-4]+random_uuid +file_name[-4:])
    if file_path.suffix == ".csv":
        clean_data.to_csv(file_path, index=False)
    else:
        clean_data.to_excel(file_path, index=False)
    return file_path