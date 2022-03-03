#[x] create a program that take a file location
#[x] opens and reads the file (displays all the content on the terminal)
#[x] if no file, promps a message no file
#[x] asks if to create or quit
#[x] creates or quits

def gather_location(): 
    user_input = input("To open a data sheet specify file location.\nEnter \"default\" for the default file.\n") 
    user_input.strip()
    #add some string processing to clear the input

    if user_input.lower() == "default": 
        user_input = "/Users/martapodziewska/Documents/01_Coding/01_GitHub_working_repos/kcal-culator/main/draft_data_sheet.csv"
    return user_input

def open_data_sheet(file_location):
        
    try: 
        with open(file_location) as ds: 
            data_sheet_content = ds.read()
        print(data_sheet_content)
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