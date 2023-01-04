#Jeny Patel 
#Tours and Travels 
# Each prompt is made error proof
#if user pays less then what then bill will keep on prompting user for remaining amount
#if user pays more than bill displays extra amount 

import random 
import time
print("Welcome to Jeny's Tours and Travels")

#asks user for payment 
def ask_for_payment(user_final_total_bill, user_full_name,tour_month, tour_date):

  print("\n-----------------")
  
  #keep prompting user for payment until they enter some number input
  while True:
   
    try:

      user_payment = float(input("Enter your payment here ("+str("$ {0:,.2f}".format(user_final_total_bill))+") : "))
      break
    
    #if user enters non number payment shows error 
    except:

      print("Invalid Entry - Please enter valid payment")
  
  #displays extra amount that user paid or remaining payment that user forgot to pay and prompts user to pay remaining payment 
  while True:
    
    #runs if user payment is less than or more than what they were suppose to pay (bill)
    if (user_final_total_bill - user_payment) > 0.01 or (user_payment - user_final_total_bill) > 0.01:

      #runs if user paid more than what they were suppose to pay
      if (user_payment - user_final_total_bill) > 0.01:
  
        user_extra_payment = user_payment - user_final_total_bill
        
        #displays the extra amount user paid
        print("You paid "+"$ {0:,.2f}".format(user_extra_payment)+" extra")

        break
      
      #runs if user paid less than what they were suppose to pay 
      elif (user_final_total_bill - user_payment) > 0.01:
        
        remaining_payment = user_final_total_bill - user_payment

        print("You Forgot to pay "+"$ {0:,.2f}".format(remaining_payment))

        #keep on prompting user for the remaining payment they forgot to pay until they pay all the payment
        while True:
          
          if (user_final_total_bill - user_payment) > 0.01:
            
            remaining_payment = user_final_total_bill - user_payment
       
            print("Please pay the remaining amount "+"$ {0:,.2f}".format(remaining_payment))
            
            #prompts user to pay remaining payment until they enter number input 
            while True:

              try:
                user_remaining_payment = float(input("Enter here: "))

                break
              
              #if user enters non number payment shows error 
              except:

                print("Invalid Entry - Please enter valid payment (don't enter comma in your payment)")

            user_payment = user_payment + user_remaining_payment

          else:
            break
    else:
      break

  print("\n-----------------")

  #slows down the program by 0.6 seconds 
  time.sleep(0.6)

  #displays name of the person who is booking tour and the date and month they want to go for tour 
  print(user_full_name+", your bookings for "+tour_month+" "+ str(tour_date) +" has been done !!")
  
  print("\n-----------------")

  time.sleep(0.5)
  
  #prompts user to rate there booking system and runs until user enters rating between 0 and 5
  while True:
   
    #prompts user to rate their system out of 5
    try:

      user_ratings = int(input("How would you rate our booking system out of 5: "))
      
      #if user enters rating out of more than 0(including) and less than 5(including) 
      if user_ratings >5 or user_ratings < 0:

        #shows error message 
        print("Invalid Entry - you need to rate from 0 to 5\n")

      #if user rates system between 0 and 5
      else:

        #stops this loop form running 
        break

    #if user enters non number input 
    except:

      #displays error message 
      print("Invalid Entry - You need to need to enter a whole number\n")
  
  print("\nWould you like to give us feedback ?")

  #prompts user to enter yes or no for feedback and runs until user enters yes or no 
  while True:
    
    feedBack_yes_or_no = input("Enter yes or no: ")
   
    #changes user answer to lower case and saves it 
    upper_feedback = feedBack_yes_or_no.upper()
    
    #if user enters anything apart from yes and no 
    if upper_feedback != "YES" and upper_feedback != "NO":

      #displays error message 
      print("Invalid Entry - please enter either yes or no")
    
    #if user enters yes or no 
    else:

      #stops loop from running 
      break
  
  #if user entered yes for feedback 
  if upper_feedback == "YES":

    #prompts user to enter feedback
    user_feedback = input("\nEnter your feedback: ")
    print("\nThanks for your valuable Feedback and Ratings :)")

  #if user enters no for feedback 
  else:

    #displays thanks message 
    print("\nThanks for your valuable Ratings :)")

  print("\n-----------------\nThank you ")

#cancels user bookings
def cancel_booking():

  #delets user total bill and cancels the booking and leaves out of program with thank you message 

  print("\n-----------------\nThank you ")


#makes bill for user 
def make_Bill(num_people_on_tour, user_bookings, user_meal_price_list, user_num_days, user_num_nights, user_discount, user_full_name, user_tour_month, user_tour_date):
  
  hotel_fair_list = [70, 200, 350]
  
  #calculates total bill for user without discount and tax
  user_total_bill = ((num_people_on_tour*(user_meal_price_list[user_bookings[1]] * user_num_days[user_bookings[2]-1]))+(user_bookings[5]*(user_num_nights[user_bookings[2]-1]*hotel_fair_list[user_bookings[4]-1]))+(num_people_on_tour*user_bookings[3])+user_bookings[6])
  
  time.sleep(1)

  print("\n---------------------")
  print("Here is your total tour Package Bill !\n")

  time.sleep(1.5)
  
  #displays total bill 
  print("Total Price:","$ {0:,.1f}".format(user_total_bill))
  
  #if user got any discount by winning math contest or lucky draw 
  if user_discount == 1:
    
    #reduces 30% from their total bill 
    discount_on_bill = user_total_bill * (30/100)
    user_total_bill = user_total_bill - discount_on_bill

    #displays new total bill 
    print("Total Price (after 30% discount):","$ {0:,.2f}".format(user_total_bill))
  
  #if user didn't get discount 
  else:

    user_total_bill = user_total_bill

  #calculates 13% discount on user total bill 
  tax = (13/100)*user_total_bill

  print("13 % Tax:","$ {0:,.2f}".format(tax))
  
  #calculates new total bill with 13% tax on it 
  user_total_tax_bill = tax + user_total_bill

  #displaysn new tax bill
  print("Total Price (with Tax):","$ {0:,.2f}".format(user_total_tax_bill))

  print("\n---------------------")
 

  print("Do you want to continue, cancel or rebook your tour package ? ")

   #prompts user if they want to continue, cancel or reebook their tour 
  while True:

    user_want = input("Enter Continue, Cancel or Rebook: ")
    
    #changes user input into upper case 
    upper_user_want = user_want.upper()
    
    #if user entered anything apart from continue, rebook and cancel 
    if upper_user_want != "CONTINUE" and upper_user_want != "CANCEL" and upper_user_want != "REBOOK":

      #displays error message 
      print("\nInvalid Entry - Please enter continue or cancel or rebook")
    
    #if user entered input from the above 3 given options 
    else:
      
      #stops this loop from running 
      break
  
  #if user wants to rebook the tour 
  if upper_user_want == "REBOOK":

    #cancels the previous booking and starts the booking from starting
      book_user_tour()

  #if user wants to cancel  booking and exit the system 
  elif upper_user_want == "CANCEL":
    
    cancel_booking()
  
  #if user wants to continue 
  else:

    #calls ask_for_payment function and sends user total bill, their full name and month and date for tour 
    ask_for_payment(user_total_tax_bill, user_full_name, user_tour_month, user_tour_date)
   
#books user choices for tour 
def book_user_tour():

  print("\n---------------------")
  user_first_name = input("Enter your first name: ")
  user_last_name = input("Enter your last name: ")
  user_full_name = user_first_name+" "+user_last_name
  print("\n---------------------")

  while True:

    user_trip = input("Would you like book international or domestic trip ?\n")
    
    #converts user input into upper case 
    upper_user_trip = user_trip.upper()
     
    #if user entered anything else apart from  internaitonal or domestic 
    if upper_user_trip != "INTERNATIONAL" and upper_user_trip != "DOMESTIC":
      
      #displays error message 
      print("Invalid Entry - Please enter either international or domestic\n")
    
    #if user entered internaitonal or domestic input 
    else: 

      #stops loop from  running 
      break

  print("\n---------------------")
  
  #keep on prompting user to enter num of people until user enters whole number greater than 0  for num of people 
  while True:

    try:
      
      #prompts user to enter number of people 
      num_people = int(input("Enter for how many number of people you are booking trip for ?\n"))
      
      #if user enters num people greater than 0
      if num_people >= 1:
        
        #stops loop from running 
        break

      else:
        print("Invalid Entry - please enter valid number of people greater than 0\n")
    
    #if user enters non integer input 
    except:

      #displays error message 
      print("Invalid Entry - Please enter whole number for number of people on trip\n")

  print("\n---------------------")
  
  month_list = ["january" , "february" , "march" , "april" , "may" , "june" , "july" , "august" , "september" , "october" , "november" , "december"]

  month_with_31 = ["january","march","may","july","august","october","december"]
 
  #prompts user to enter month in which they would like to travel 
  while True:

    user_tour_month = input("Enter in which month you want to go for tour: ")

    lower_user_tour_month = user_tour_month.lower()
    
    #if user entered month that is in the list of actual month list 
    if lower_user_tour_month in month_list:

      #stops loop from running 
      break
    
    #if user enters anything apart from 12 months shows error message 
    else:
      print("Invalid Entry - you need to enter valid month\n")
      
  
  print("")

  #propmts user on which date user want to go for tour 
  while True:
    
    #prompts user to enter date 
    try:
      user_tour_date = int(input("Enter on which date you want to go for tour: "))

      #if user enters any date less than 1 and more than 31
      if user_tour_date > 31 or user_tour_date < 1:

        #displays error message 
        print("Invalid Date - Please enter a valid date within a month\n")
      
      #if user enters any month from 12 normal month 
      else:
        
        #if user enters date above 30 for months that have 30 days 
        if lower_user_tour_month not in month_with_31 and lower_user_tour_month != "february" and user_tour_date > 30:
          
          #displays error 
          print("Invalid Entry- Please enter a valid date\n")
        
        #if user enters date greater than 28 for february month 
        elif lower_user_tour_month == "february" and user_tour_date > 28:

          #displays error
          print("Invalid Entry- Please enter a valid date\n")
        
        #if user entered valid date for valid month 
        else:

          #stops loop from running
          break   
    
    #if user enters non integer input 
    except:
      print("Invalid Entry - Please enter valid whole number date\n")

  user_tour_choices = [0,0,0,0,0,0,0]
  
  #if user chose international travel 
  if upper_user_trip == "INTERNATIONAL":
    
    #charges for booking international tour 
    user_tour_choices[6] = 350

    print("\n---------------------")
    
    #displays destinations options and prompts user to choose one of those destination options 
    int_desti_list = ["1. Egypt" , "2. Dubai","3. China"]
  
    print("We have 3 destinations for international travel")
    
    #displays destination options 
    for destination in range(3):

      time.sleep(0.7)
      print(int_desti_list[destination])
    
    time.sleep(0.8)

    #prompts user to enter num beside the destination option they would like to go 
    while True:
      
      #takes and saves user's input 
      try:
        
        user_tour_choices[0] = int(input("\nEnter the number corresponding to the destination you would like to go: "))
        
        #if user didn't chose destination option from given choices  
        if user_tour_choices[0] != 1 and user_tour_choices[0] != 2 and user_tour_choices[0] != 3:
          
          #displays error message 
          print("Invalid Entry - Please enter number only from the above given options")
        
        #if user entered destination option from the above given options 
        else:

          #stops user from running loop again and again 
          break
      
      #if user enters non integer input 
      except:

        #displays error message 
        print("Invalid Entry - PLease enter the number corresponding to the destination you would like to go")
    
    
    print("\n---------------------")
    
    #displays meal options to user and prompts user to enter meal option from given choices 
    int_meal_list = ["1. Non-Vegetarian","2. Vegetarian","3. Vegan"]

    meal_price_egypt = [120, 100, 130]
    meal_price_dubai = [100, 70 , 115]
    meal_price_china = [110, 90, 120]
    meal_price_list = [120, 100, 130, 100, 70 , 115, 110, 90, 120]
     
    print("What kind of meal you prefer for your whole trip ?")
    
    #runs for 3 times and displays 3 meal option and its cost depending which destination user chose 
    for meal_num in range(3):
      
      time.sleep(0.7)

      #if user chose 1 destination displays meal prices according to that place 
      if user_tour_choices[0] == 1:

        user_destination = 0
        print(int_meal_list[meal_num] +" ( $" +str(meal_price_egypt[meal_num])+" per person per day)")
      
      #if user chose 2 destination  displays price of meal according to that place  
      elif user_tour_choices[0] == 2:
        
        user_destination = 2
        print(int_meal_list[meal_num] + " ( $"+ str(meal_price_dubai[meal_num])+" per person per day)")
      
      #if user chose 3 destination option displays price of meals according to that destination 
      else:
        
        user_destination = 5
        print(int_meal_list[meal_num] + " ( $" + str(meal_price_china[meal_num])+" per person per day)")
    
    time.sleep(0.8)

  #prompts user to enter their liked meal option until user doesn't user enters option form the above given options 
    while True: 

      #prompts user to enter number 
      try:
        
        user_tour_choices[1] = int(input("\nEnter the number corresponding to the meal you prefer: "))
        
        #if user didn't choose option from the given above 3 choices 
        if user_tour_choices[1] != 1 and user_tour_choices[1] != 2 and user_tour_choices[1] != 3:
          
          #displays error message 
          print("Invalid Entry - Please enter number only from the above given options")
        
        #if user entered option from the given choices 
        else:

          user_tour_choices[1] = user_tour_choices[1]+( user_destination)

          #stops the loop from playing
          break
      
      #if user entered non number input for meal option 
      except:

        #displays error message 
        print("Invalid Entry - PLease enter the number corresponding to the meal you would like")
  
  
    print("\n---------------------")

    print("What kind of package would you like ?")

    int_package_list = ["7 days 6 nights", "10 days 9 nights", "13 days 12 nights"]

    user_tour_num_nights = [6, 9, 12]
    user_tour_num_days = [7, 10, 13]
  
    #displays package options for how many number days and nights user want to go for trip 
    num = 1
    for package_num in range (3):
      
      time.sleep(0.7)
      print(str(num)+". "+int_package_list[package_num])
      num = num + 1
    
    time.sleep(0.8)

    #keep on prompting user to enter number besides the package they would like until they enter any number form the given 3 above options
    while True:

        try:
          
          user_tour_choices[2] = int(input("\nEnter the number corresponding to the package you want: "))
          
          #if user enters any other number apart form the given 3 options 
          if user_tour_choices[2] != 1 and user_tour_choices[2] != 2 and user_tour_choices[2] != 3:
            
            #displays error message 
            print("Invalid Entry - Please enter number only from the above given options")
          
          #if user enters number form the above given options
          else:

            #stops the loop from running 
            break
        
        #if user enters non integer input 
        except:

          #displays error message 
          print("Invalid Entry - PLease enter the number corresponding to the package you like")

    travel_price_list = [900, 956, 1000]
    travel_destination = ["To Egypt", "To Dubai", "To China"]

    print("\n---------------------")

    print("Here is your flight fair for round trip")
    print("Flight will take off from toronto airport")
    time.sleep(1)
    
    #displays flight and per person ticket price written besides it depending which destination user chose 
    print(travel_destination[user_tour_choices[0]-1] +" ( $ "+ str(travel_price_list[user_tour_choices[0]-1])+" )")
    user_tour_choices[3] = travel_price_list[user_tour_choices[0]-1]
      
   
 # If user chose domestic trip 
  elif upper_user_trip == "DOMESTIC":
    
    #charges for booking domestic trip 
    user_tour_choices[6] = 250
      
    print("\n---------------------")

    domestic_desti_list = ["1. Banff, Alberta " , "2. Victoria, Vancouver island","3. Whitehorse, Yukon"]
   
   #displays 3 destination options 
    print("We have 3 destinations for Domestic travel")

    for destination in range(3):

      time.sleep(0.6)
      print(domestic_desti_list[destination])
    
    time.sleep(0.7)

    #keep on prompting user to enter number corresponding to the destination they would like to go until user enters number form the above given 3 options 
    while True:
      
      #prompts user to enter number 
      try:
        
        user_tour_choices[0] = int(input("\nEnter the number corresponding to the destination you would like to go: "))


        #if user enters number apart from the above given options 
        if user_tour_choices[0] != 1 and user_tour_choices[0] != 2 and user_tour_choices[0] != 3:

          #displays error message 
          print("Invalid Entry - Please enter number only from the above given options")
        
        #if user entered number from the given options 
        else:

          #stops the loop from running 
          break
      
      #if user enter non integer input 
      except:

        #displays error message 
        print("Invalid Entry - PLease enter the number corresponding to the destination you would like to go")
    
    
    print("\n---------------------")
    
    domestic_meal_list = ["1. Non-Vegetarian","2. Vegetarian","3. Vegan"]

    meal_price_alberta = [90, 55, 100]
    meal_price_vancouver = [100, 60 , 105]
    meal_price_yukon = [105, 65, 110]
    meal_price_list = [90, 55, 100, 100, 60, 105, 105, 65, 110]

    print("What kind of meal you prefer for your whole trip ?")
    
    #displays meal options and per person per day price for meal written besides it depending which destination user chose 
    for meal_num in range(3):
    
      time.sleep(0.7)
      if user_tour_choices[0] == 1:
        
        user_destination = 0
        print(domestic_meal_list[meal_num] +" ( $" +str(meal_price_alberta[meal_num])+" per person per day)")

      elif user_tour_choices[0] == 2:
        
        user_destination = 2
        print(domestic_meal_list[meal_num] + " ( $"+ str(meal_price_vancouver[meal_num])+" per person per day)")

      else:
        
        user_destination = 5
        print(domestic_meal_list[meal_num] + " ( $" +str(meal_price_yukon[meal_num])+" per person per day)")
  
    time.sleep(0.8)

    #keep on prompting user to enter number corresponding to the meal option they like until they enter number form the given above options 
    while True:
      
      #prompts user to enter number 
      try:
        
        user_tour_choices[1] = int(input("\nEnter the number corresponding to the meal you prefer: "))
        
        #if user entered any other number apart from the given options 
        if user_tour_choices[1] != 1 and user_tour_choices[1] != 2 and user_tour_choices[1] != 3:
          
          #displays error message 
          print("Invalid Entry - Please enter number only from the above given options")
        
        #if user entered number from the given options 
        else:
         
         #saves price of the meal depending which meal option user chose and which destination 
          user_tour_choices[1] = user_tour_choices[1] + user_destination

          #stops loop form running 
          break
      
      #if user enters non integer input 
      except:

        #displays error message 
        print("Invalid Entry - PLease enter the number corresponding to the meal you would like")
  
    print("\n---------------------")

    print("What kind of package you would like ?")

    domestic_package_list = ["4 days 3 nights", "6 days 5 nights", "8 days 7 nights"]
    user_tour_num_nights = [3, 5, 7]
    user_tour_num_days = [4, 6, 8]
  
    num = 1

    #displays package options for number of days and nights 
    for package_num in range (3):
      
      time.sleep(0.7)
      print(str(num)+". "+domestic_package_list[package_num])
      num = num + 1
   
    time.sleep(0.8)

    #keep on prompting user to enter number corresponding to package they like until they enter number from the above 3 given options 
    while True:
        
        #prompts user to enter number 
        try:
          
          user_tour_choices[2] = int(input("\nEnter the number corresponding to the package you want: "))
          
          #if user entered number apart from the above 3 given options
          if user_tour_choices[2] != 1 and user_tour_choices[2] != 2 and user_tour_choices[2] != 3:
            
            #displays error message 
            print("Invalid Entry - Please enter number only from the above given options")
          
          #if user enters number from the given options
          else:  

            #stops loop from running 
            break
        
        #if user entered non integer input
        except: 

          #displays error message
          print("Invalid Entry - PLease enter the number corresponding to the package you like")

    print("\n---------------------")
  
    travel_options = ["Flight","Train"]
    travel_price_alberta= [200, 300]
    travel_price_vancouver = [300, 400]
    travel_price_yukon = [500, 400]
    travel_price_list = [200, 300, 300, 400, 500, 400]
    

    print("How you would like to travel to your destination ?\n")
    print("Flight and Train will start it's journey from Toronto")
    
    #displays user how they would like to travel to their destination and price of ticket per person besides it depending which destination  user chose 
    for num in range(2):
     
      time.sleep(0.7)
      if user_tour_choices[0] == 1:
        
        user_destination = 0
        print(travel_options[num] +" ( $" +str(travel_price_alberta[num])+" per person)")

      elif user_tour_choices[0] == 2:
        
        user_destination = 2
        print(travel_options[num] + " ( $"+ str(travel_price_vancouver[num])+" per person)")

      else:
        
        user_destination = 4
        print(travel_options[num] + " ( $" +str(travel_price_yukon[num])+" per person)")
    
    time.sleep(0.8)

    #keep on prompting user how they would like to travel to their destination until user enters flighr or train 
    while True: 

      #prompts user to enter 
      user_travel_choice = input("\nEnter how you would like to travel: ")

     #converts user input to upper case 
      upper_user_travel_choice = user_travel_choice.upper()
     
      #if user didn't enter flight or train 
      if upper_user_travel_choice != "FLIGHT" and upper_user_travel_choice != "TRAIN":
          
          #displays error message 
          print("Invalid Entry - Please enter either Flight or Train")

      #if user entered flight or train 
      else: 

        #stops loop from running 
        break
     
    if upper_user_travel_choice == "FLIGHT":
      value = 0

    else:

      value = 1
    
    #saves price of ticket price depending either user chose flight or train and the destination they chose 
    user_tour_choices[3] = travel_price_list[value + user_destination]
  
  #if user choice is not international or domestic
  else: 
  
   #just to avoid error 
   print("")

  print("\n---------------------")

  print("What kind of Hotel you would like to stay in ?")

  hotel_list = ["4 Star Rating","5 Star rating","7 Star rating"]

  hotel_price_list = [70, 200, 350]

  num = 1

  #displays hotel options and price of room per night written besides it 
  for hotel_num in range (3):
    
    time.sleep(0.7)
    print(str(num)+". "+hotel_list[hotel_num]+" ( $"+ str(hotel_price_list[hotel_num])+" per night )")
    num = num + 1
  
  time.sleep(0.8)

  #keep on prompting user to enter number corresponding the hotel option they like until user enters number from the given options 
  while True:
    
    #prompts user to enter number 
    try:
      user_tour_choices[4] = int(input("\nEnter the number corresponding to the hotel you would like to stay in: "))

      #if user entered apart form the given options 
      if user_tour_choices[4] != 1 and user_tour_choices[4] != 2 and user_tour_choices[4] != 3:
        
        #displays error message 
        print("Invalid Entry - Please enter number only from the above given options")
      
      #if user entered number from the given option 
      else:

        #stops loop from running 
        break
    
    #if user's entered non integer input 
    except:

      #displays error message 
      print("Invalid Entry - PLease enter the number corresponding to the hotel you would like to stay in")
  
  print("\n---------------------")

  #keep on prompting user to enter number of room until they enter number greater than 0 
  while True:

    #prompts user to enter number 
    try:

      user_tour_choices[5] = int(input("How many hotels rooms you want to book\nEnter here: "))
       
      #if user enters number greater than or equal to 1
      if user_tour_choices[5] >= 1:

        #stops loop from running 
        break

      #if not 
      else:

        #displays error message 
        print("Invalid Entry - please enter valid number of rooms greater than 0")
    
    #if user enters non integer number 
    except:

      #displays error
      print("Please enter a number for number of hotel rooms you need")

  print("\n\n\t\t\t\t\t\t\t***** Special Offer *****\nWe have a special offer going on in which you can get 30% discount on your tour booking by either winning lucky draw or by doing math quiz correct")
  
  #keep on prompting user to enter yes or no until they enter yes or no 
  while True:

    user_discount = input("\nWould you like to get 30% discount ?\nEnter Yes or No: ") 
    
    upper_user_discount = user_discount.upper()
    
    #if user didn't enter yes or no 
    if upper_user_discount != "YES" and upper_user_discount != "NO":
      
      #displays error message 
      print("Invalid Entry - Please enter either yes or no")
    
    #if user entered yes or no 
    else:
     
     #stops loop from running 
     break
  
  #if user wants discount 
  if upper_user_discount == "YES":

    print("\n------------------")
    print("How would you like to get 30% discount")
    print("1. By lucky Draw")
    print("2. Math Quiz (you need to get all 3 questions correct)")
    
    #keep on prompting user to enter number corresponding the way they want to get discount until user enter number form given options 
    while True:
      
      #prompts user to enter number 
      try:
        user_discount_option = int(input("\nEnter number corresponding to the way you would like to get discount: "))
        
        #if user enters numbner apart from given option 
        if user_discount_option != 1 and user_discount_option != 2:

          #displays error message 
          print("Invalid Entry - Please enter number from the above given options") 

        #if user enters number from given option
        else:

          #stops loop from running 
          break
      
      #if user enters non intger input 
      except: 

        #shows error message 
        print("Invalid Entry - Please enter number either 1 or 2")

    #if user enters 1 way 
    if user_discount_option == 1:
      
      print("\n-----------------\n** Good Luck with Lucky Draw **")

      #generates random number and saves it 
      lucky_num = random.randint(1,3)
      print("\nGuess a lucky number between 1 and 3")
      
      #prompts user to enter integr number between 1 and 3 
      while True:
        try:
          user_guess_num = int(input("Enter your guessed number: "))

          if user_guess_num != 1 and user_guess_num != 2 and user_guess_num != 3:

            print("Invalid Entry - Please number between 1 and 3")
          
          else:
            break

        except:
         print("Invalid Entry - Please enter a number")
      
      time.sleep(0.4)

      #if user number is same as computer number 
      if user_guess_num == lucky_num:

        #user gets discounts 
        print("\nCongratulations !!! You get 30% discount.")
        discount = 1
      
      #if user number is not same as computer number 
      else:
        
        #user doesn't get discount 
        print("\nBad luck :( you don't get any discount.")
        discount = 0
    
    #if user enters 2 way 
    else:

      print("\n-----------------\n** Good Luck with Math Quiz **")
      print("Read Questions properly\n")

      math_questions = ["100 * 2", "0 / 453465565", "120 + 50"]
      correct_math_answers = ["200", "0", "170"]
      
      qus_num = 0
      user_math_ans = [0, 0, 0]
      
      #displays 3 math questions and prompts user to enter answer 
      for qus in range(3):
        qus_num = qus_num + 1
        user_math_ans[qus] = input(str(qus_num) + ". "+ math_questions[qus] + " = ")
      
      score = 0

      #checks user's answers 
      for ans in range(3):
        
        #if user answer is same as correct math answer 
        if user_math_ans[ans] == correct_math_answers[ans]:
          
          #user gets point 
          score = score + 1
        
        #if user answer is not correct 
        else:

          #no points 
          score = score + 0
      
      #if user got all 3 questions correct 
      if score == 3:
        
        #user gets discount 
        print("\nCongratulations !!! You get 30% discount.")
        discount = 1

      #if user didn't get all 3 questions correct 
      else:

        #user gets no discount 
        print("\nBad luck :( you don't get any discount.")
        discount = 0
  
  #if user entered no for discount 
  else:
    
    #user doesn't get discount 
    print("\n-----------------")
    print("Ok no problem no discount for you")
    discount = 0
  
  #calls make bill functions and sends user's choices and prices to it 
  make_Bill(num_people, user_tour_choices, meal_price_list, user_tour_num_days, user_tour_num_nights, discount, user_full_name, user_tour_month, user_tour_date)

book_user_tour()   
    

    








