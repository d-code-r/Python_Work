#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

# start message
print("wellcome to tip calculator:)")

# inputs
bill = float(input("enter your bill:) $"))
flag = True

while(flag):
  tip_string = input("enter your tip precent (for example 12% and not more than 20%: ")
  num_extracted = int(tip_string[0:2])
  if num_extracted <= 20:
    flag = False

number_of_people = int(input("how many people are here: "))

# logic
total_bill = (((num_extracted / 100) * bill) + bill)
idvdual_bill = round((total_bill / number_of_people),2)

# output
print(f"toatal bill for ech person payable ${idvdual_bill}")