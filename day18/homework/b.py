for i in range(3):
  print("A")
print("B")

is_student = False
age = 16
print(is_student and (age < 18))

age = 32
is_student = True
if age < 18 or is_student:
  print("Discount")
else: 
  print("Regular price")