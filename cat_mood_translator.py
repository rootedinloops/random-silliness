def cat_mood(mood):

    mood = mood.lower()
        
    if mood == "happy":
        return "😺 Purrfect!"
    elif mood == "grumpy":
        return "😾 Hisss..."
    elif mood == "sleepy":
        return "😴 zzz..."
    elif mood == "chaotic":
        return "🙀 CATastrophe!"
    else:
        return "🐱 Just being a cat."
    

while True:
    user_input = input("Enter a cat mood (or 'exit' to quit): ")

    if user_input == "exit":
        break

    print("You said:", user_input)
    result = cat_mood(user_input)
    print(result)


    
