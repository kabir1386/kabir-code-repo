import sys

#THIS IS THE FIRST SIMPLE PYTHON SCRIPT MADE BY 'KABIR' PLEASE GIVE ME FEEDBACK IF IT WORKS CORRECTLY OR NOT.

#I KNOW THAT IT WAS NOT NECESSARY TO ADD ALL THE CODE IN ONE FUNCTION, BUT I FOUND THIS METHOD EASY THAT IS WHY I DID IT. YOU CAN SUGGEST ME SOME MORE WAYS TO MAKE THE CODE MORE SIMPLER! 

start = input("do you want to play a simple game of answering some general knowledge questions? (make sure you type the spelling correctly when answering) \n\nif yes, then type 'yes':")
if start != "yes":
    sys.exit()

def questions():
    print()
    print("Answer the following questions in one or two word - ")
    print()
    a = input("1. What is the capital of France?.\nanswer - ")
    print()
    b = input("2. What is the capital of Nepal?. \nanswer - ")
    print()
    c = input("3. who was the father of communism?. \nanswer - ")
    print()
    if a == "paris":
        print("1. correct!")
    else:
        print("1. wrong, if you think its correct, please check the spelling and sentence structure!")
    if b == "kathmandu":
        print("2. correct!")
    else:
        print("2. wrong, if you think its correct, please check the spelling and sentence structure!")
    if c == "Karl Marx":
        print("3. correct!")
    else:
        print("3. wrong, if you think its correct, please check the spelling and sentence structure!")
    if a != "paris" and b != "kathmandu":
        print("sorry, all are wrong!")


questions()
