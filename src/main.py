from data_pipeline import *
from data_analysis import *

file_name="worldData.csv"

def prompt_yes_no():
    choice = input("Do you want to export the cleaned data? (Y/N): ").strip().upper()
    while choice not in ("Y", "N"):
        choice = input("Please enter Y or N: ").strip().upper()
    return choice

def print_menu():
    print("\n=== Analysis Menu ===")
    print("A - Continent with most countries")
    print("B - Region with largest combined area")
    print("C - Country with highest life expectancy")
    print("D - Subregion with lowest/highest average GDP per capita")
    print("E - Run all")
    print("F - Show Menu Again")
    print("Q - Quit")

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

    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
