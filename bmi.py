import math

he= int(input("please input height = "))
we= int(input(" please input weight "))

height = (he / 100) ** 2

bmi = we / height

if 25<= bmi < 30 :      
    print("you fat")

elif  18<= bmi <25 :
    print("you normal")

elif 18> bmi:
    print(" you bony")

elif 30<= bmi <40:
    print('you very fat') 