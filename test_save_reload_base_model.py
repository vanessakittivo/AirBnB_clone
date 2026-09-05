#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

print("Objects currently in storage:")

all_objs = storage.all()

for obj_id, obj in all_objs.items():
    print(obj_id)
    print(obj)

print("\nCreating new object:")

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89

print(my_model)

print("\nSaving:")

my_model.save()

print(my_model)
