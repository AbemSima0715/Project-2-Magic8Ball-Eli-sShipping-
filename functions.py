# """
#  *****************************************************************************
#    FILE:        functions.py
#
#    AUTHOR:      {Your Name Here}
#
#    ASSIGNMENT:  Magic 8 Ball fortune teller and Eli's Shipping
#
#    DATE:         {Today's Date}
#
#    DESCRIPTION: {Your Description Here}
#
#  *****************************************************************************

# ELI's SHIPPING RATES
# Ground Shipping
# Weight of Package                         | Price per Pound   | Flat Charge
# 2 lb or less                              |	$1.50           |	$20.00
# Over 2 lb but less than or equal to 6 lb  |   $3.00           |	$20.00
# Over 6 lb but less than or equal to 10 lb |   $4.00           |	$20.00
# Over 10 lb                                |   $4.75           |	$20.00

# Ground Shipping Premium
# Weight of Package                         | Price per Pound   | Flat Charge
# 2 lb or less                              |	$0.00           |	$125.00
# Over 2 lb but less than or equal to 6 lb  |   $0.00           |	$125.00
# Over 6 lb but less than or equal to 10 lb |   $0.00           |	$125.00
# Over 10 lb                                |   $0.00           |	$125.00

# Drone Shipping
# Weight of Package                         | Price per Pound   | Flat Charge
# 2 lb or less                              |	$4.50           |	$0.00
# Over 2 lb but less than or equal to 6 lb  |   $9.00           |	$0.00
# Over 6 lb but less than or equal to 10 lb |   $12.00          |	$0.00
# Over 10 lb                                |   $14.25          |	$0.00

from random import randrange
# Make sure to add parameters
def fortune(name, quest):

name = input("What is your full name: ")
quest = input("What is your question you would like to answer? ")
space_index = name.find(" ")
name = name[:space_index]
letter = name[space_index -1:]
last_character = name[space_index -1]
rand_num = randrange(0,9)
if rand_num == 0:
  fortune = "Yes - definitely."
elif rand_num == 1:
  fortune = "It is decidedly so."
elif rand_num == 2:
  fortune = "Without a doubt"
elif rand_num == 3:
  fortune = "Reply hazy, try again"
elif rand_num == 4:
  fortune = "Ask again later."
elif rand_num == 5:
  fortune = "Better not tell you now."
elif rand_num == 6:
  fortune = "My sources say no"
elif rand_num == 7:
  fortune = "Outlook not so good."
elif rand_num == 8:
  fortune = "Very doubtful"
if last_character == "s":
  print(f"{name}' Question: {quest}")
else:
  print(f"{name}'s Question: {quest}")
print(f"Magic 8-balls answer: {fortune}")
    # This ignores our code so that we do not get an error Remove 'pass' when you want to start testing code.
    pass

#  Make sure to add parameters
def shipping(weight):
  def ground_shipping(weight):
    if weight <= 2:
      weight * $1.50 + $20.00
    elif weight => 2 and weight <= 6:
      weight * $3.00 + $20.00
    elif weight => 6 and weight <= 10:
      weight * $4.00 + $20.00
    elif weight => 10:
      weight * $4.75 + $20.00
  def drone_shipping(weight)
    if weight <= 2:
      weight * $4.50
    elif weight => 2 and 

  
    
 
  
  shipping_types = ("Ground, Premium and Drone Shipping")
    # This ignores our code so that we do not get an error Remove 'pass' when you want to start testing code.
    pass


def main():
  weight = input("What is your package weight in kg?")
  pounds_to_kg = 0.453592
  weight = weight * pounds_to_kg
  ground_shipping_premium_cost = ($125.00)
  
  
  
    
  
  

  

  
  
  # fortune(name, quest)
  
    # Collect user input in main and pass these values to the functions fortune and shipping. 
    # This ignores our code so that we do not get an error Remove 'pass' when you want to start testing code.
    pass
# Ground Shipping
# Weight of Package                         | Price per Pound   | Flat Charge
# 2 lb or less                              |	$1.50           |	$20.00
# Over 2 lb but less than or equal to 6 lb  |   $3.00           |	$20.00
# Over 6 lb but less than or equal to 10 lb |   $4.00           |	$20.00
# Over 10 lb                                |   $4.75           |	$20.00

# Ground Shipping Premium
# Weight of Package                         | Price per Pound   | Flat Charge
# 2 lb or less                              |	$0.00           |	$125.00
# Over 2 lb but less than or equal to 6 lb  |   $0.00           |	$125.00
# Over 6 lb but less than or equal to 10 lb |   $0.00           |	$125.00
# Over 10 lb                                |   $0.00           |	$125.00

# Drone Shipping
# Weight of Package                         | Price per Pound   | Flat Charge
# 2 lb or less                              |	$4.50           |	$0.00
# Over 2 lb but less than or equal to 6 lb  |   $9.00           |	$0.00
# Over 6 lb but less than or equal to 10 lb |   $12.00          |	$0.00
# Over 10 lb                                |   $14.25          |	$0.00

from random import randrange
##################DO NOT EDIT BELOW THIS LINE################
# This invokes the main function.  It is always included in our
# python programs. 
if __name__ == "__main__":
    main()