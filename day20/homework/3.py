"""4) შექმენით პროგრამა რომელშიც მომხმარებელმა უნდა შეიყვანოს რიცხვები, სანამ უარყოფითს არ შეიყვანს. დაბეჭდეთ შეყვანილი ლუწი და კენტი რიცხვების რაოდენობა გამოიყენეთ პირობითი განცხადებები"""

even_count=0 
odd_count=0

while True:
    number=int(input("enter your number: "))
    if number < 0:
        break
    if number % 2==0:
        even_count += 1
    else:
        odd_count += 1

print("numbers of even numbers entered: ", even_count)
print("numbers of odd numbers entered: ", odd_count)