#Write your code below this row 👇
for number in range(1, 101):
  if number % 5 == 0 and number % 3 == 0:
    print("FizzBuzz")
  elif number % 3 == 0 :
    print ("Fizz")
  elif number % 5  == 0:
    print("Buzz")
  else:
    print(number)

# or (my way) 👇

game = 0
for number in range (1,101):
  if number % 5 == 0 and number % 3 == 0:
    game+=number
    number = "FizzBuzz"
  elif number % 5 == 0:
    game+=number
    number = "Buzz"
  elif number % 3 == 0:
    game+=number
    number = "Fizz"
  print(number)