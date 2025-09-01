word = input("Please enter a word:")
look_for = "0123456789"
index = 0
found = False

while index < len(look_for):
    digit = look_for[index]

    if digit in word:
        print("Number " + digit + " found")
        found = True
    index += 1

if found == False:
    print("No digits found")
