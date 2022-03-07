# Requirements v1:
#[x] create a program that take a file location
#[x] opens and reads the file (displays all the content on the terminal)
#[x] if no file, promps a message no file
#[x] asks if to create or quit
#[x] creates or quits

# Requirements v2:
#[ ] request the user to input an ingredient
#[ ] display the calorie content of the given ingredient. 
#[ ] ]If the ingredient is not in the file, prompt the user to input the calorie content 
#[ ] and then store in the file.

from csv import reader

def gather_location(): 
    user_input = input("Specify file location or enter \"d\" for the default file.\n").strip()

    if user_input.lower() == "d": 
        user_input = "/Users/martapodziewska/Documents/01_Coding/01_GitHub_working_repos/kcal-culator/main/draft_data_sheet.csv"

    #ingredient = input("enter an engredient:").lower().strip()
    
    return user_input

def open_data_sheet(file_location):
        
    try: 
        with open(file_location) as ds: 
            data_sheet_content = reader(ds)
            for row in data_sheet_content:
                print(row)
    except FileNotFoundError: 
        print("The file you specified does not exist.")
        create_data_sheet(file_location)

    return

def create_data_sheet(file_name): 
    user_input = input("Entered file name: %s.\nWould you like to create a new file? Y/N:\n" %(file_name))

    if user_input.lower() == "y": 
        ds = open(file_name, "x")
        ds.close()
        print("File created at %s" %(file_name))
        return
    else:
        return

def main(): 
    open_data_sheet(gather_location())
    return

if __name__ == "__main__": 
    main()