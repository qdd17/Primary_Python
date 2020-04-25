#Zodiac script. V1.0
Zod1, Zod2, Zod3, Zod4, Zod5, Zod6, Zod7, Zod8, Zod9, Zod10, Zod11, Zod12, Znak = "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces", "Your zodiac sign "
MonthName = ['January' , 'February' , 'March' , 'April' , 'May' , 'June' , 'July' , 'August' , 'September' , 'October' , 'November' , 'December']

MWrong = "There are only "
MWrong2 = " days in "
wrong = 0

while wrong != 1:
  month = int(input("Enter month of birth "))
  if month > 12:
	  print("Only 12 mouth in a year")
  elif month < 13: 
    day = int(input("Enter day of birth"))
    if month == 1:
      if day < 21:
        print(Znak + Zod10)
      elif day > 31:
        print(MWrong + '31' + MWrong2 + MonthName [0])
      elif day > 20:
        print(Znak + Zod11)
    elif month == 2:
      if day < 19:
        print(Znak + Zod11)
      elif day > 29:
        print(MWrong + '28' + MWrong2 + MonthName [1])
      elif day == 29:
        print(Znak + Zod12)
      elif day > 18:
        print(Znak + Zod12)
    elif month == 3:
	    if day < 21:
		    print(Znak + Zod12)
	    elif day > 31:
	      print(MWrong + '31' + MWrong2 + MonthName [2])
	    elif day > 20:
		    print(Znak + Zod1)
    elif month == 4:
	    if day < 21:
	     	print(Znak + Zod1)
	    elif day > 30:
	      print(MWrong + '30' + MWrong2 + MonthName [3])
	    elif day > 20:
	    	print(Znak + Zod2)
    elif month == 5:
	    if day < 22:
		    print(Znak + Zod2)
	    elif day > 31:
	      print(MWrong + '31' + MWrong2 + MonthName [4])
	    elif day > 21:
		    print(Znak + Zod3)
    elif month == 6:
	    if day < 22:
		    print(Znak + Zod3)
	    elif day > 30:
		    print(MWrong + '30' + MWrong2 + MonthName [5])
	    elif day > 21:
		    print(Znak + Zod4)
    elif month == 7:
	    if day < 23:
		    print(Znak + Zod4)
	    elif day > 31:
	      print(MWrong + '31' + MWrong2 + MonthName [6])
	    elif day > 22:
		    print(Znak + Zod5)
    elif month == 8:
	    if day < 24:
		    print(Znak + Zod5)
	    elif day > 31:
	      print(MWrong + '31' + MWrong2 + MonthName [7])
	    elif day > 23:
		    print(Znak + Zod6)
    elif month == 9:
      if day < 24:
	      print(Znak + Zod6)
      elif day > 30:
	      print(MWrong + '30' + MWrong2 + MonthName [8])
      elif day > 23:
	      print(Znak + Zod7)
    elif month == 10:
	    if day < 24:
	    	print(Znak + Zod7)
	    elif day > 31:
	      print(MWrong + '31' + MWrong2 + MonthName [9])
	    elif day < 23:
    		print(Znak + Zod8)
    elif month == 11:
    	if day < 23:
    		print(Znak + Zod8)
    	elif day > 30:
	      print(MWrong + '30' + MWrong2 + MonthName [10])
    	elif day > 22:
		    print(Znak + Zod9)
    elif month == 12:
    	if day < 22:
	    	print(Znak + Zod9)
    	elif day > 31:
    	  print(MWrong + '31' + MWrong2 + MonthName [11])
    	elif day > 21:
     		print(Znak + Zod10)
		
else:
	wrong = 1
	print ("Error! Restart script!")