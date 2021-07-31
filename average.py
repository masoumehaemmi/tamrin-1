 n = input('enter your name: ')
 
 
 f = input('enter your family ')

 a = float(input("enter your 1 lessons"))
 b =float(input("enter your 2 lessons"))
 c =float(input("enter your 3 lessons"))

 sum = a + b + c 

 ave = sum / 3

 if ave >= 17 :
    print(n , f , "  Great ")

 elif  17> ave >= 12 :
     print(n ,f , " normal ") 

 elif  ave < 12 :

    print(n , f , " fail " )       
