user_wegiht = int(input("Please enter your weight: "))

weight_metric = input("Is your weight in kilograms or pounds? \n Enter 'K' for kg and 'L' lbs: ").upper()

if weight_metric == 'K':
    user_wegiht *= 2.2
    print("Your weight in pounds is " + str(user_wegiht))

elif weight_metric == 'L':
    user_wegiht *= 0.45
    print("Your weight in kilograms is " + str(user_wegiht))

else:
    print("Invalid entry!")