
low = 0
high = 100
epsilon = 0
ans = (low + high)/2
secretGuess = raw_input("Please think of a number between 0 and 100! ")
while abs(ans - int(secretGuess)) >= epsilon:
    print("is your secrect number " + str(ans))
    i = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if i == 'l':
        low = ans
    elif i == 'h':
        high = ans
    elif i == 'c':
        break
    else:
        print("That isn't a valid answer")
    ans = (low + high)/2
print("Game over. Your secret number was: " + str(ans))