from data_pipeline import *
from data_analysis import *
from data_filter import *

file_name="worldData.csv"

def prompt_yes_no():
    choice = input("Do you want to export the cleaned data? (Y/N): ").strip().upper()
    while choice not in ("Y", "N"):
        choice = input("Please enter Y or N: ").strip().upper()
    return choice

def print_menu():
    print("djfska")
    print("\n=== Analysis Menu ===")
    print("A - Continent with most countries")
    print("B - Region with largest combined area")
    print("C - Country with highest life expectancy")
    print("D - Subregion with lowest/highest average GDP per capita")
    print("E - Run all")
    print("F - Show Menu Again")
    print("Q - Quit")
    
def print_main_menu():
    print("\n=== Data Menu ===")
    print("A - Analyse Data")
    print("B - Filter/Statistic Data")
    
def print_filter_menu():
    print("\n=== Set Your Filters ===")
    print("A - Set continent filter")
    print("B - Set country filter")
    print("C - Set region filter")
    print("D - Set subregion filter")
    print("E - Set type filter")
    print("F - Set area in km sq filter")
    print("G - Set population filter")
    print("H - Set life expectancy filter")
    print("I - Set per-capita GDP filter")
    print("J - Show results + stats")
    print("K - Show menu")
    print("L - Clean Store Selection")
    print("Q - Quit")

def get_filter_string(data,column, type):
        options_list = getOptions(data, column)
        print(f"Please pick from the following {type} (comma-separated):")
        print(", ".join(options_list))
        raw_input_value = input(f"{type}(s): ").strip()
        if raw_input_value == "":
            print(f"No {type} filter set.")
            return None
        else:
            inputs = [x.strip() for x in raw_input_value.split(",") if x.strip()]
            # normalize
            options_set = {opt.upper() for opt in options_list}
            invalid = [x for x in inputs if x.upper() not in options_set]

            if invalid:
                print(f"Invalid option(s): {', '.join(invalid)}")
                return None
            else:
                current_option = inputs
                print(f"{type} filter set to: {', '.join(current_option)}")
                return current_option
            
def get_filter_range(type):
    print("Please enter range as min-max (e.g. 10-100)")
    print("If you want only a min or max, use -1 for the missing value")
    print("Example: -1-100  OR  10--1")
    raw_input_value = input(f"{type} min-max: ").strip()

    # Empty input = no filter
    if raw_input_value == "":
        print(f"No {type} range set")
        return -1 , -1
    if "-" not in raw_input_value:
        print("Invalid format. Please use min-max")
        return -1,-1
    min_val_str, max_val_str = raw_input_value.split("-", 1)

    min_val = int(min_val_str)
    max_val = int(max_val_str)
    if (min_val < 0 and min_val != -1) or (max_val < 0 and max_val != -1):
        print("Only -1 is allowed as a negative value")
        return -1, -1

    if min_val != -1 and max_val != -1:
        if min_val > max_val:
            print("Min value cannot be greater than Max value.")
            return -1,-1

    print(f"{type} filter set to: {min_val} - {max_val}")
    return (min_val, max_val)

    
    
def main():
    print("Welcome to EPI Code Challenge!!!")
    file_name = input("Please enter a file name from inside the data folder: ").strip()

    try:
        # Load
        data = open_file(file_name)
        # Clean
        cleaned_data = clean_data(data)

        # Exportxport
        if prompt_yes_no() == "Y":
            export_path = export_clean_data(cleaned_data, file_name)
            print(f"Cleaned data exported to: {export_path}")
        while True :
            print_main_menu()
            analysis_main_command = input("Enter command: ").strip().upper()
            if analysis_main_command =="A":
                # Analysis 
                print_menu()
                while True:
                    analysis_command = input("Enter command: ").strip().upper()

                    if analysis_command =="A":
                        get_continent_with_most_countries(cleaned_data)

                    elif analysis_command =="B":
                        get_region_with_largest_combined_area_sq_km(cleaned_data)

                    elif analysis_command== "C":
                        get_country_with_highest_life_expectancy(cleaned_data)

                    elif analysis_command =="D":
                        get_subregion_with_lowest_and_highest_average_gdp_per_capita(cleaned_data)

                    elif analysis_command =="E":
                        get_continent_with_most_countries(cleaned_data)
                        get_region_with_largest_combined_area_sq_km(cleaned_data)
                        get_country_with_highest_life_expectancy(cleaned_data)
                        get_subregion_with_lowest_and_highest_average_gdp_per_capita(cleaned_data)
                    elif analysis_command == "F":
                        print_menu()
                        
                    elif analysis_command == "Q":
                        print("Session Ended")
                        break

                    else:
                        print("Invalid option. Please choose A, B, C, D, E, or Q.")
            elif analysis_main_command =="B":
                print_filter_menu()
                current_country=[]
                current_continent =[]
                current_region =[]
                current_sub_region=[]
                current_type=[]
                # values can not be negatives
                current_area_min,current_area_max = -1,-1
                pop_min,pop_max =-1,-1
                life_exp_min,life_exp_max = -1, -1
                gdp_min,gdp_max = -1 , -1
                
                while True:
                    analysis_command = input("Enter command: ").strip().upper()
                    if analysis_command == "A":
                        current_continent =get_filter_string(cleaned_data,"continent", "Continent")
                    elif analysis_command == "B":
                        current_country =get_filter_string(cleaned_data,"iso_a2", "Country code")
                    elif analysis_command == "C":
                        current_region =get_filter_string(cleaned_data,"region_un", "Region")
                    elif analysis_command == "D":
                        current_sub_region =get_filter_string(cleaned_data,"subregion", "Subregion")
                    elif analysis_command == "E":
                        current_type =get_filter_string(cleaned_data,"type", "Type")
                    elif analysis_command == "F":
                        current_area_min,current_area_max =get_filter_range("area_km2", "Type")
                    elif analysis_command == "G":
                        pop_min,pop_max =get_filter_range("Population")
                    elif analysis_command == "H":
                        life_exp_min,life_exp_max =get_filter_range( "Life Expectancy")
                    elif analysis_command == "I":
                        gdp_min,gdp_max =get_filter_range( "Per-Capita GDP")
                    elif analysis_command == "J":
                        filtered_data =get_data_analysis(cleaned_data, current_country,
                                            current_continent,
                                            current_region,
                                            current_sub_region,
                                            current_type,
                                            current_area_min,current_area_max,
                                            pop_min,pop_max,
                                            life_exp_min,life_exp_max,
                                            gdp_min,gdp_max)
                        print(f"Filtered rows: {len(filtered_data)} / {len(cleaned_data)}")
                        cols = ["iso_a2", "name_long", "continent", "region_un", "subregion", "type", "area_km2", "pop", "lifeExp", "gdpPercap"]
                        print(filtered_data[cols].head().to_string(index=False))

                    elif analysis_command == "K":
                        print_filter_menu()
                    elif analysis_command == "L":
                        current_country=[]
                        current_continent =[]
                        current_region =[]
                        current_sub_region=[]
                        current_type=[]
                        current_area_min,current_area_max = -1,-1
                        pop_min,pop_max =-1,-1
                        life_exp_min,life_exp_max = -1, -1
                        gdp_min,gdp_max = -1 , -1
                    elif analysis_command == "Q":
                        print("Session Ended")
                        break
                    else :
                        print("Invalid option.")
            else:
                print("Invalid option. Please choose A or B.")

    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()




