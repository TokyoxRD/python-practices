
questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "what's the most abundant gas in the earth atmosphere?: ",
             "how many bones are in human body?: ")


options = (("A. 115", "B. 116", "C. 117", "D. 118"),     
           ("A. Crocodile", "B. Whale", "C. Ostrich", "D. Eagle"),  
           ("A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Argon"),  
           ("A. 195", "B. 206", "C. 213", "D. 220"))       


answers = ("D", "C", "B", "B")  

guesses = [] 
score = 0

question_num = 0

for question in questions:
    print(question)
    print("------------------")
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter your answer (A, B, C, D): ").upper()
    guesses.append(guess)
    

    if guess == answers[question_num]:
        score += 1
        print(f"Correct Answer!, your current score is: {score}/{len(questions)}")
    else:
        print(f"Incorrect Answer!")
        print(f"{answers[question_num]} is the correct answer")
    
    question_num += 1


print("--------------")
print("   Results      ")
print("--------------")

for answer in answers:
    print(answer, end="")
print()

for guess in guesses:
    print(guess, end="")
print()
        
print(f"Your final score is: {score}/{len(questions)}")
    