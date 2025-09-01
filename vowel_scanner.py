word = input("Please enter a word:")
look_for = "aeiou"
index = 0

while index < len(look_for):
    character_search = look_for[index]
    if character_search in word:
        print(character_search + " found")
    else: 
        print(character_search + " not found")
    index += 1

print("Scan complete")
