#program to check a age of person

age=int(input("enter the age"))
if age>1 and age<=18:
        print("the person is child")
elif age>=18 and age<65:
    print("the person is adult")
else:
    age=65 and age<65
    print ("the person is senior citizen")
