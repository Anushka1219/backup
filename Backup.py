import os
import shutil

source=input("Enter the source folder")
destination=input("Enter the destination folder")

source="d:/"+source+"/"
destination="d:/"+destination+"/"

print("beforecopying")
print(os.listdir(destination))

list=os.listdir(source)

for everyfile in list:
    shutil.copy((source+everyfile),destination)

print("aftercopying")
print(os.listdir(destination))
