import json
file1 = open("info_about_lunch.txt","r")
data_string=file1.read()
data_dictionary=json.loads(data_string)

print("if you want to check the menu for ten days, Select numbers from 0-9 \nif you want to exit press any other number")
key=0
value=""
value_list=[]

while(int(key)>=0 and int(key)<=9):
    key = input()
    
    if int(key)>=0 and int(key)<=9:
        value = data_dictionary[key]
        value_list=value.split("-")
        print("The day You selected is "+value_list[0]+" and the lunch today is "+ value_list[1]+"\n")
        print("____________________\n") #adding a seperating line between questions asked
        print("Again, if you want to check the menu for ten days, Select numbers from 0-9 \nif you want to exit press any other number")

