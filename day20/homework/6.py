"""7) მომხმარებელს შემოაყვანინეთ წინადადება, შემდეგ for ციკლისა და პირობითი განცხადებების საშვალებით დაბეჭდეთ ჯერ ხმოვნების, შემდეგ კი თანხმოვნების რაოდენობა (ხმოვნებად ჩათვალეთ სიმბოლოები: a, e, i, o, u ხოლო სხვა ყველა თანხმოვნად)"""

sentence=str(input("enter your sentence: "))

vowel_count=0
consonant_count=0

for char in sentence:
    if char.isalpha():
        if char in 'a,e,i,o,u':
            vowel_count += 1
        else:
            consonant_count += 1 
print("numbers of vowels: ", vowel_count)
print("numbers of consonant: ", consonant_count)