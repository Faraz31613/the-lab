import json
file1 = open("info_about_lunch.txt","r")
dic1=file1.read()
dic2=json.loads(dic1)
print("if you want to check the menu for ten days, Select numbers from 0-9 \nif you want to exit press any other number")
a=None
b=""
c=[]
while(a>=0 and a<=9 or a==None):
    a = input()
    if a>=0 and a<=9:
        aa=str(a)
        b = dic2[aa]
        c=b.split("-")
        print("The day You selected is "+c[0]+" and the lunch today is "+ c[1]+"\n")
        print("Again, if you want to check the menu for ten days, Select numbers from 0-9 \nif you want to exit press any other number")

