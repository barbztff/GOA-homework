"""5) მომხმარებელს 3 მცდელობა აქვს სწორი PIN კოდის შეყვანისთვის. თუ შეიყვანს სწორად, დაიბეჭდება "Access Granted", სხვა შემთხვევაში "Access Denied" გამოიყენეთ პირობითი განცხადებები"""

correct_pin = "1997"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    entered_pin = input("Enter your PIN: ")
    if entered_pin == correct_pin:
        print("Access Granted")
        break
    else:
        print("Incorrect PIN")
        attempts += 1
if attempts == max_attempts:
    print("Access Denied")


