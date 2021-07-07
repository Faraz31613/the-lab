import json
from file_manager import FileManager

data_string = ""
with FileManager('info_about_lunch.txt', 'r') as lunch_details_file:
    data_string=lunch_details_file.read()

data_dictionary=json.loads(data_string)

print("If you want to check the menu for ten days, Select numbers from 0-9 \nIf you want to exit press any other number")
key=0
lunch_according_day=""
lunch_according_day_list=[]

while(int(key)>=0 and int(key)<=9):
    key = input()
    
    if int(key)>=0 and int(key)<=9:
        lunch_according_day = data_dictionary[key]
        lunch_according_day_list=lunch_according_day.split("-")
        print("The day You selected is "+lunch_according_day_list[0]+" and the lunch today is "+ lunch_according_day_list[1]+"\n")
        print("____________________\n") #adding a seperating line between questions asked
        print("Again, If you want to check the menu for ten days, Select numbers from 0-9 \nIf you want to exit press any other number")

