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
#[ ] work on the main function
#   [ ] implement all the functions in the flow
#   [ ] make the program run constantly
#[ ] find a solution for the source file (keyboard?)

from csv import reader, writer

class DataSheet():

    def gather_location(self): 
        location = input("Specify file location or enter \"d\" for the default file.\n").strip()

        if location.lower() == "d": 
            location = "/Users/martapodziewska/Documents/01_Coding/01_GitHub_working_repos/kcal-culator/main/draft_data_sheet.csv"
        
        return location

    def open_data_sheet(self,file_location):
            
        try: 
            with open(file_location) as ds: 
                data_sheet_content = ds.read()
                print(data_sheet_content)
        except FileNotFoundError: 
            user_input = input("The file %s does not exist. \nWould you like to create a new file? Y/N:\n" %(file_location))
            
            if user_input.lower() == "y": 
                create_data_sheet(file_location) 
            else:
                return

        return

    def create_data_sheet(self,file_name): 
        
        ds = open(file_name, "x")
        ds.close()
        print("File created at %s" %(file_name))
        return

class Ingredient: 

    def input_ingredient_name(self): 
        ingredient_name = input("Enter an engredient:").lower().strip()
        return ingredient_name

    def find_ingredient(self, file_location, ingredient_name): 
        ingredient_kcal = 0

        with open(file_location) as ds: 
            data_sheet_content = reader(ds)
            for row in data_sheet_content:
                if row[0] == ingredient_name:
                    ingredient_kcal = int(row[1])
                    print(ingredient_kcal)
                    break
                
            if ingredient_kcal == 0: 
                self.save_ingredient(file_location, ingredient_name)

        return

    def save_ingredient(self, file_location, ingredient_name):
        calorie_content = input("Enter the number of calories in 100g of %s:\n" %ingredient_name)
        with open(file_location, 'a') as ds: 
                ds_writer = writer(ds)
                ds_writer.writerow([ingredient_name, calorie_content])
        return

def main(): 
    
    NewDataSheet = DataSheet()
    NewIngredient = Ingredient()

    NewIngredient.find_ingredient(NewDataSheet.gather_location(), NewIngredient.input_ingredient_name())

    return

if __name__ == "__main__": 
    main()