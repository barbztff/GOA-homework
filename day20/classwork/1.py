"""1) მოხმარებელს შემოატანინეთ რიცხვი, შემდეგ კი დაუბეჭდეთ ეს რიცხვი დადებითია, უარყოფითი თუ ნეიტურალი ანუ ნული. შემდეგ კომენტარებით ახსენით რა გასნხვავებაა if-სა და elif-ს შორის რატომ არ შეიძლება ზოგერ elif-ს ნაცვლად if-ის გამოყენება"""

number = int(input("შეიყვანეთ რიცხვი: "))

if number > 0:
    print("რიცხვი დადებითია") 
elif number < 0:
    print("რიცხვი უარყოფითია")
else:
    print("რიცხვი ნეიტრალურია (ნულია)")

"""if: გამოიყენება, როდესაც გვსურს შევამოწმოთ გარკვეული პირობა. თუ ის სწორია (True), მაშინ შესაბამისი კოდი სრულდება."""

"""elif (else if): გამოიყენება მაშინ, როდესაც პირველი if პირობა არ შესრულდა, ანუ იყო False, და გვსურს მეორე პირობის შემოწმება."""