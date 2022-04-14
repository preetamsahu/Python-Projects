import random
guessed_number=int(input("Guess any intiger number between 1 and 20  "))
if guessed_number<20:
    number=random.randint(0,20)
    half=number//2
    print(f"Correct Number is {number}")
    if guessed_number==number:
        print("Congretulation! Your gussed number is correct, you won")
    elif guessed_number>=half and guessed_number<((half+half//2)):
        print("You are slightly closed")
    elif  guessed_number<number and guessed_number>=((half+half//2)):
        print("You are too close")
    else:
        print("You are too far from the correct Number")
else:
    print("Wrong input")