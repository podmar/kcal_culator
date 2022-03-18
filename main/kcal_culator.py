# Requirements v1:
#[x] create a program that take a file location
#[x] opens and reads the file (displays all the content on the terminal)
#[x] if no file, promps a message no file
#[x] asks if to create or quit
#[x] creates or quits

# Requirements v2:
#[x] request the user to input an ingredient
#[x] display the calorie content of the given ingredient. 
#[x] ]If the ingredient is not in the file, prompt the user to input the calorie content 
#[x] and then store in the file.

#TO DO
#[ ] rewrite Ingredient class for its instances to fit into the DataSheet class
#[ ] research and choose a data structure for the ingredients (not duplicating ingredients)
#[ ] rewrite open_data_sheet function to open and store data in the NewDataSheet object
#[x] find a solution for the source file

from csv import reader, writer
import sys

class DataSheet:
    def __init__(self, data_sheet_location):
        self.data_sheet_location = data_sheet_location.strip()
        self.raw_data = self.open_data_sheet(self.data_sheet_location)
        self.data_set = set()

        for element in self.raw_data: 
            try: 
                self.data_set.add(Ingredient(element[0], int(element[1])))
            #remove after bug fixing / correcting the file or add an option to correct the data in the spreadsheet. Can move to when int is actually needed?
            except ValueError:
                print("The kcal value of %s has been entered incorrectly" %{element[0]})
                continue

    def open_data_sheet(self, file_location):
        data_set = []

        try: 
            with open(file_location, newline="") as ds: 
                data_sheet_content = reader(ds)
                data_set = list(data_sheet_content).pop(0)
                #data_set = set(data_set) -> gives TypeError: unhashable type: 'list'

        except FileNotFoundError: 
            user_input = input("The file %s does not exist. \nWould you like to create a new file? Y/N: \n" %(file_location))
            
            if user_input.lower() == "y": 
                create_data_sheet(file_location) 
            else:
                data_set = None

        return data_set
    
    def display_kcal(self, ingredient_name): 
        ingredient_kcal = 0

        #cannot use the below loop in set, find out how to search in sets.

        for element in self.data_set: 
            print(element.ingredient_data[0])
            if element.ingredient_data[0] == ingredient_name:
                ingredient_kcal = element.ingredient_data[1]
                print(ingredient_kcal)
                break
                
            # if ingredient_kcal == 0: 
            #     self.save_ingredient(file_location, ingredient_name)

        return ingredient_kcal

def gather_location(): 
    location = input("Specify file location or enter \"d\" for the default file.\n").strip()

    if location.lower() == "d": 
        location = "draft_data_sheet.csv"
    
    return location

def create_data_sheet(file_name): 
    
    ds = open(file_name, "x")
    ds.close()
    print("File created at %s" %(file_name))
    return

class Ingredient: 
    def __init__(self, ingredient_name, ingredient_kcal): 
        self.ingredient_data = [ingredient_name, ingredient_kcal]

    # def input_ingredient_name(self, ): 
    #     ingredient_name = input("Enter an engredient:").lower().strip()
    #     return ingredient_name

#moved to datasheet
    def save_ingredient(self, file_location, ingredient_name):
        calorie_content = input("Enter the number of calories in 100g of %s:\n" %ingredient_name)
        with open(file_location, 'a') as ds: 
                ds_writer = writer(ds)
                ds_writer.writerow([ingredient_name, calorie_content])
        return

def main(): 
    
    try: 
        NewDataSheet = DataSheet(sys.argv[1])
        #print(NewDataSheet.data_set) 
    except IndexError:
        NewDataSheet = DataSheet(gather_location())
    
    print(NewDataSheet.display_kcal(input("Which ingredient would you like to check? Type: ")))

    #NewIngredient = Ingredient()
    #NewIngredient.find_ingredient(NewDataSheet.gather_location(), NewIngredient.input_ingredient_name())

    return

if __name__ == "__main__": 
    main()