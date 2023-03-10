# two slashes give us an int
print (8 // 3)

# a comma after divide shows us how many decimal place we want
print (round(2.666666666, 2))

# if we want to continue dividing
result = 4 / 2
result /= 2
print(result)

# user score
score = 0
#instead of writing   score = score + 1
score += 1
# or
score -= 1
# or
score *= 1

# f string
# insread  this  print("Your score is ", score )  or  print("Your score is " + str(score))
print(f"Your score is {score}")