#Baby_Boomers = (1947 - 1964)
#Millenials = (1982 - 1995)
#Gen_Z = (1996 - 2015)

User_Age = int(input("What is your year of birth? "))
if User_Age > 1947 and User_Age < 1964:
    print("Hello Baby_Boomers")
elif User_Age > 1982 and User_Age < 1995:
    print("Hello Millenias")19
elif User_Age > 1996 and User_Age < 2015:
    print("Hola Gen ZZZ's")
else:
    print("Nothing for you")