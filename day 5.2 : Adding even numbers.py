#Write your code below this row 👇

# sum of all even numbers from 1 to 100

total = 0
for i in range(2,101,2):
  total += i
print(total)

# or 👇

total = 0
for i in range(1 , 101):
  if i % 2 == 0 :
    total += i
print(total)