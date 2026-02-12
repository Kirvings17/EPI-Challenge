
def getOptions(data,column):
    return sorted( data[column].astype("string").str.strip().unique().tolist())


def get_data_analysis(cleaned_data, 
                    current_country,
                    current_continent,
                    current_region,
                    current_sub_region,
                    current_type,
                    current_area_min,current_area_max,
                    pop_min,pop_max,
                    life_exp_min,life_exp_max,
                    gdp_min,gdp_max):
    data_copy = cleaned_data.copy()
    if current_continent != []:
        data_copy = data_copy[data_copy["continent"].str.upper().isin([c.upper() for c in current_continent])]
    if current_country !=[]:
        data_copy = data_copy[data_copy["iso_a2"].str.upper().isin([c.upper() for c in current_country])]
    if current_region !=[]:
        data_copy = data_copy[data_copy["region_un"].str.upper().isin([c.upper() for c in current_region])]
    if current_sub_region !=[]:
        data_copy = data_copy[data_copy["subregion"].str.upper().isin([c.upper() for c in current_sub_region])]
    if current_type !=[]:
        data_copy = data_copy[data_copy["type"].str.upper().isin([c.upper() for c in current_type])]
    data_copy = apply_numeric_range(data_copy,"area_km2", current_area_min, current_area_max)
    data_copy = apply_numeric_range(data_copy,"pop" ,pop_min,pop_max)
    data_copy = apply_numeric_range(data_copy,"lifeExp" ,life_exp_min,life_exp_max)
    data_copy = apply_numeric_range(data_copy,"gdpPercap" ,gdp_min,gdp_max)
    return data_copy


def apply_numeric_range (data, column , min_value, max_value):
    if(min_value != -1):
        data = data[data[column]>=min_value]
    if(max_value != -1):
        data = data[data[column]<=max_value]
    return data
    