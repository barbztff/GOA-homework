"""2) შექმენით 5 ცვლადი რომლებშიც შეინახავთ წიგნების თავდაპირველ ფასს, შემდეგ შექმენით ცვლადი რომელშიც შეინახავთ ფასდაკლების ოდენობას, შექმენით ახალი ფასის მქონე წიგნების ცვლადები, რომელთა მნიშვნელობა იქნება ძველ მნიშვნელობას გამოკლებული ახალი, საბოლოოდ კი დაბეჭდეთ ახალი წიგნების ფასები (გამოიყენეთ კარგი მიდგომები: რომ ცვლადის მნიშვნელობის მინიჭებისას შეგიძლიათ სხვა ცვლადის გამოყენება, კოდი ახსენით კომენტარების საშვალებით, ცვლადებს დაარქვით აღმწერი სახელები snake_case-ის სტილში)"""


# წიგნების თავდაპირველი ფასები
book_price_1 = 30  # პირველი წიგნის ფასი
book_price_2 = 25  # მეორე წიგნის ფასი
book_price_3 = 40  # მესამე წიგნის ფასი
book_price_4 = 20  # მეოთხე წიგნის ფასი
book_price_5 = 35  # მეხუთე წიგნის ფასი

# ფასდაკლების ოდენობა
discount_amount = 5  # ყველა წიგნიდან ჩამოაკლდება 5 ერთეული

# ახალი ფასები ფასდაკლების შემდეგ
new_book_price_1 = book_price_1 - discount_amount
new_book_price_2 = book_price_2 - discount_amount
new_book_price_3 = book_price_3 - discount_amount
new_book_price_4 = book_price_4 - discount_amount
new_book_price_5 = book_price_5 - discount_amount

# დაბეჭდვა ახალი ფასებით
print("ახალი ფასები ფასდაკლების შემდეგ:")
print("პირველი წიგნი:", new_book_price_1)
print("მეორე წიგნი:", new_book_price_2)
print("მესამე წიგნი:", new_book_price_3)
print("მეოთხე წიგნი:", new_book_price_4)
print("მეხუთე წიგნი:", new_book_price_5)