#Objective: The aim of this assignment is to understand the importance of indentation in Python, especially with if statements.

#Task 1: Code Correction: Below is a piece of Python code with incorrect indentation. Your task is to correct it.

weather = "rainy" #test by changing value b/t "sunny" & "rainy"

if weather == "sunny":
    print("Wear sunglasses!") #indented to include in the "if" block
else:
    print("Take an umbrella!") #indented to include in the "else" block

#Task 2: Your Mood Today: Ask the user how they feel today. If they say "happy", print "That's great to hear!", and if they say "sad", print "I hope your day gets better!". Ensure your if statement is properly indented. HINT: Use the input() function to ask the user how they feel!

mood = input ("How are you doing today? Happy or sad?") #request input from user

#added various responses to account for some user input variance
happy = ["happy","Happy"," happy"]
sad = ["sad","Sad"," sad"]

if mood in happy: #used if/in operator to compare to the happy variable
    print ("That is great to hear!")
if mood in sad: #used if/in operator to compare to the sad variable
    print ("I hope your day get's better!")
else: #added an else line so the code has an endpoint
    print ("This feeling does not compute with my machine brain...")