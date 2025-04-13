"""4) შექმენით 5 ცვლადი, რომლებშიც შეინახავთ განსხვავებულ ლოგიკურ და შედარების ოპერაციათა შედეგებს (უნდა იყოს შედარების და ლოგიკური ოპერატორები ერთად მაგალითად temperature > 30 and not cloudy), გვერდზე კომენტარის საშვალებით მიუწერეთ ეს შედეგი (boolean მნიშვნელობა) აიღეთ მრავალფეროვანი კომბინაციები""" 

temperature = 35
humidity = 60
cloudy = True
wind_speed = 15
is_raining = False

var1 = temperature > 30 and not cloudy     
# True and False = False

var2 = humidity < 70 or is_raining         
# True or False = True

var3 = not (wind_speed > 20) and cloudy    
# not False and True = True

var4 = temperature == 35 or humidity > 80  
# True or False = True

var5 = not is_raining and wind_speed < 20 and temperature > 20 
# True and True and True = True
