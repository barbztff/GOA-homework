"""3) შექმენით სია რომელშიც ჩამოწერეთ სპორტის სახეობებს (მინიმუმ 10 სახეობა), აქედან slicing-ის გამოყენებით ამოჭერით და დაბეჭდეთ:
1-5
3-8
-2-0
4-0
შემობრუნებული სია"""

sports = ["ფეხბურთი", "კალათბურთი", "კრივი", "ცურვა", "რაგბი", "ტენისი", "ჭიდაობა", "სნოუბორდი", "სკეიტბორდი", "გოლფი"]

print("1-5:", sports[1:5])     
print("3-8:", sports[3:8])      
print("-2-0:", sports[-2:])     
print("4-0:", sports[4:])       
print("შემობრუნებული სია:", sports[::-1])  
