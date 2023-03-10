print("welcome to the tip calculator")

Bill = float(input("How much is the total bill ?"))
Tip = float(input("What percantage do you want to tip ?"))
people = float(input("How many people to split the bill ? "))
Bill_with_Tip = Tip / 100 * Bill + Bill
final_bill = round(Bill_with_Tip / people, 2)
print(f"Your final Bill is : {final_bill}")

# My Way👆
# My New Way 👇
print("Welcaome to the tip calculator")
total_bill = input("What was your total bill ? ")
tip = input("What percentage tip would you like to give ? 10, 12, or 15 ?")
people = input("How many people to split the bill ? ")

each_person_pay = round((float(total_bill) + (int(tip) / 100 * float(total_bill))) / int(people))

print(f"each person should pay {each_person_pay}")

# Their Way👇

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")