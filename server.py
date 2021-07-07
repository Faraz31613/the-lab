import json
file1 = open("info_about_lunch.txt","r")
dic1=file1.read()
dic2=json.loads(dic1)

print("if you want to check the menu for ten days, Select numbers from 0-9 \nif you want to exit press any other number")
a=0
b=""
c=[]

while(int(a)>=0 and int(a)<=9):
    a = input()
    
    if int(a)>=0 and int(a)<=9:
        b = dic2[a]
        c=b.split("-")
        print("The day You selected is "+c[0]+" and the lunch today is "+ c[1]+"\n")
        print("Again, if you want to check the menu for ten days, Select numbers from 0-9 \nif you want to exit press any other number")

