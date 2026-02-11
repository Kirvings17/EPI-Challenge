def get_continent_with_most_countries(data):
    continent_country_count =data.groupby("continent")["iso_a2"].nunique().sort_values(ascending=False)
    continent = continent_country_count.index[0]
    country = continent_country_count.iloc[0]
    print(f"Contient with most countries: {continent} with {country:.3f} countries" )
    
def get_region_with_largest_combined_area_sq_km(data):
    region_area_sum = data.groupby("region_un")["area_km2"].sum().sort_values(ascending=False)
    region = region_area_sum.index[0]
    area = region_area_sum.iloc[0]
    print(f"Region with the largest combined area: {region} with {area:.3f} sq km" )
    
def get_country_with_highest_life_expectancy(data):
    country_max_expectancy = data.groupby("name_long")["lifeExp"].max().sort_values(ascending=False)
    country = country_max_expectancy.index[0]
    expectancy_of_life = country_max_expectancy.iloc[0]
    print(f"Country with the highest life expectancy : {country}  with {expectancy_of_life:.3f} years" )
    
    
def get_subregion_with_lowest_and_highest_average_gdp_per_capita(data):
    subregion_average_gdp = data.groupby("subregion")["gdpPercap"].mean().sort_values(ascending=False)
    max_subregion = subregion_average_gdp.index[0]
    max_gdp = subregion_average_gdp.iloc[0]
    min_subregion = subregion_average_gdp.index[-1]
    min_gdp = subregion_average_gdp.iloc[-1]
    print(f"Higgest subregion avg GDP/cap : {max_subregion} with {max_gdp:.3f}" )
    print(f"Lowest subregion avg GDP/cap : {min_subregion} with {min_gdp:.3f}" )