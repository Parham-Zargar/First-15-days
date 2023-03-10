row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# Don't change the code above 👆
# The lines of codes below are somehow similar to the 2D lists from Bro Code's lessons

horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "🔑"

print(f"{row1}\n{row2}\n{row3}")
