"""2) გააკეთეთ 5-5 მაგალითი თთოეულ შედარების ოპერატორზე (>, >=, <, <=, ==, !=), გვერდზე კომენტარის საშვალებით მიუთითეთ თუ რომელ boolean მნიშვნელობას გამოიტანას, აიღეთ მრავალფეროვანი კომბინაციები, შეეცადეთ გქონდეთ ყველა ვარიანტი"""

# > 
print(5 > 3)   # True
print(2 > 7)   # False
print(10 > 10) # False
print(-1 > -5) # True
print(0 > -1)  # True

# >= 
print(5 >= 3)  # True
print(7 >= 7)  # True
print(2 >= 8)  # False
print(-3 >= -3) # True
print(0 >= 1)  # False

# < 
print(3 < 5)   # True
print(10 < 2)  # False
print(7 < 7)   # False
print(-5 < -1) # True
print(0 < 1)   # True

# <= 
print(3 <= 5)  # True
print(7 <= 7)  # True
print(8 <= 2)  # False
print(-3 <= -3) # True
print(0 <= -1) # False

# == 
print(5 == 5)  # True
print(10 == 2) # False
print(0 == 0)  # True
print(-3 == -3) # True
print(4 == -4) # False

# != 
print(5 != 3)  # True
print(7 != 7)  # False
print(2 != 8)  # True
print(-3 != -3) # False
print(0 != 1)  # True
