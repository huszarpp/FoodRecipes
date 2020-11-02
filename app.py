from database import Database
from menu import Menu
from models.food import Food
from models.types_of_food import Types_Of_Food

Database.initialize()

#t1 = Types_Of_Food.find_one_type(ttype="type5")
#t2 = Types_Of_Food.find_one_type(ttype="type8")

#print(t1)
#print(t2)
menu = Menu()
menu.run_menu()
"""
food = Food(_id="4",
            name="name4",
            preparation="prep4",
            type_id="4")

food.save_food()

food2 = Food.find_one_food_by_name("name2")

print(food2)
"""


