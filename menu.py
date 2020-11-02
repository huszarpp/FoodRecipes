from database import Database
from models.food import Food
from models.ingredients import Ingredients
from models.types_of_food import Types_Of_Food


class Menu(object):

    def run_menu(self):
        while True:
            try:
                new_or_find = input("Do you want to create a New recipe (N) or Find a recipe (F)?")
            except:
                print("Choose (N) or (F)")
                break
            else:
                if new_or_find.lower() == "n":
                    self.new_recipe()
                    break
                elif new_or_find.lower() == "f":
                    self.find_recipe()
                    selected = input("Pick one food name to show the ingredients!\n")
                    self.find_ingredients(selected)
                    break

    def new_recipe(self):
        name = input("Please enter the NAME of the food\n")
        preparation = input("Please enter the PREPARATION of the food\n")
        type_name = input("Please enter the TYPE of the food\n")

        if self.type_is_exists(type_name):
            typef = Types_Of_Food.find_one_type(ttype=type_name)
            type_id = typef['_id']
        else:
            typef = Types_Of_Food(ttype=type_name)
            typef.save_type()
            typef = Types_Of_Food.find_one_type(ttype=type_name)
            type_id = typef['_id']

        food = Food(name, preparation, type_id)
        food.save_food()

        while True:
            one_more = input("Do you want to add (another) ingredient? Y/N")
            if one_more.lower() == "y":
                # ingredient, quantity, unit, food_id, _id=None
                ing_name = input("Ingredient NAME?\n")
                ing_quant = input("Ingredient QUANTITY?\n")
                ing_unit = input("Ingredient UNIT?\n")
                ing_food_id = food.get_id()
                ingredient = Ingredients(ingredient=ing_name, quantity=ing_quant, unit=ing_unit, food_id=ing_food_id)
                Ingredients.save_ingredient(ingredient)
            else:
                break

    @staticmethod
    def type_is_exists(type_name):
        return Types_Of_Food.find_one_type(ttype=type_name) is not None

    @staticmethod
    def find_recipe():
        foods = Database.find(collection='food', query={}
                              )
        for food in foods:
            print(
                "ID: {}, name: {}, preparation: {}, type_ID: {}".format(food['_id'], food['name'], food['preparation'],
                                                                        food['type_id'])
            )
        filt = input("Do you want to filter by type? Y/N\n")
        if filt.lower() == "y":
            enter_type = input("Enter the type!\n")
            type_item = Types_Of_Food.find_one_type(enter_type)
            foods = Food.find_foods_by_type(type_item.get_id())

            for food in foods:
                print(
                    "ID: {}, name: {}, preparation: {}, type_ID: {}".format(food['_id'], food['name'],
                                                                            food['preparation'],
                                                                            food['type_id'])
                )

    @staticmethod
    def find_ingredients(selected):
        food = Food.find_one_food_by_name(name=selected)
        print(food.get_id())
        ingredients = Ingredients.find_ingredients(food.get_id())

        for ingredient in ingredients:
            print(
                "ID: {}, ingredient: {}, quantity: {}, unit: {}, food_ID: {}".format(ingredient['_id'],
                                                                                     ingredient['ingredient'],
                                                                                     ingredient['quantity'],
                                                                                     ingredient['unit'],
                                                                                     ingredient['food_id'])
            )
