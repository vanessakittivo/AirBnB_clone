#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()

my_model.name = "My_First_Model"
my_model.my_number = 89

my_model_json = my_model.to_dict()

print("Original:")
print(my_model)
print(type(my_model.created_at))

print("\nDictionary:")
print(my_model_json)

my_new_model = BaseModel(**my_model_json)

print("\nNew object:")
print(my_new_model)
print(type(my_new_model.created_at))

print("\nSame object?")
print(my_model is my_new_model)

print("\nSame ID?")
print(my_model.id == my_new_model.id)
