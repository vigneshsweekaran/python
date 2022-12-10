import math

while True:
  try:
     days = int(input("Rental days: "))       
  except ValueError:
     print("Please enter a valid no of days. Eg: 5")
     continue
  else:
     break
 
while True:
  try:
     start_odometer = int(input("Starting Odometer reading: "))
  except ValueError:
     print("Please enter a valid Starting Odometer reading. Eg: 350")
     continue
  else:
     break
 
while True:
  try:
     end_odometer = int(input("Ending Odometer reading: "))
     if end_odometer <= start_odometer:
        print("Enter valid Ending Odometer reading")
        continue
  except ValueError:
     print("Please enter a valid Ending Odometer reading. Eg: 510")
     continue
  else:
     break
 
km_driven = end_odometer - start_odometer
print('Driven Kms: ', km_driven)

while True:
    code = input("Choose D for daily, W for Weekly, or Q to Quit:  ")
    if code[0].lower() == "d":
        print("You chose Daily!")
        if km_driven < 100:
            amount_due = 1000 * days
        else:
            amount_due = 1000* days + 10 * (km_driven - 100)
        print('Amount due is RS', amount_due)
        break
    elif code[0].lower() == "w":
        print("You chose Weekly!")
        weeks = days / 7
        weeks_round = math.ceil(weeks)
        if km_driven < 900 :
            amount_due = weeks_round * 3500
        elif km_driven >= 900 and km_driven < 1500:
            amount_due = weeks_round * 3500 + 1750
        else:
            amount_due = weeks_round * 3500 + 3500 + (km_driven - 1500) * 10
        print('Amount due is RS', amount_due)    
        break
    elif code[0].lower() == "q":
        print("You chose Quit!")
        break
    else:
        print("You must choose between D, W or W.")
        continue