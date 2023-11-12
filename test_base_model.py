#!/usr/bin/python3
from models.base_model import BaseModel
from models.user import User

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
model_str = str(my_model).split(' ')
print(model_str)
# print(type(model_str).split(""))
# my_model_json = my_model.to_dict()
# print(my_model_json)
# print("JSON of my_model:")
# for key in my_model_json.keys():
#     print("\t{}: ({}) - {}".format(key,
#           type(my_model_json[key]), my_model_json[key]))

my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.email = "airbnb@mail.com"
my_user.password = "root"
my_user.save()
