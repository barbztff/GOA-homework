"""4) დაწერეთ პითონის კოდი რომელიც მომხმარებელს input-ის საშვალებით შეეკითხება და ცვლადში შეინახავს შემდეგ ინფორმაციას: name,surname,age,location,occupation,hobby,ამ ცვლადების საშვალებით კი გამოიტანს ერთ წინადადებას რომელშიც ყველა მიღებული ინფორმაცია იქნება გამოყენებული. 

მაგალითად:

Enter your name: Alex  
Enter your surname: Johnson  
Enter your age: 25  
Enter your location: New York  
Enter your occupation: Engineer  
Enter your hobby: Playing guitar  

Alex Johnson is 25 years old, lives in New York, works as an Engineer, and enjoys Playing guitar.""" 

name=input("what is your name? ")
surname=input("what is your surname? ")
age=input("how old are you? ")
location=("where do you live? ")
occupation=("what is your occupation? ") 
hobby=("what is your hobby? ")

print( name + " " + surname + " " + age + " " + location + " " + occupation + " " + hobby ) 

