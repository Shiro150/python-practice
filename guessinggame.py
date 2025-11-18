answer = 5

print('please guess a number between 1 to 10 = ')
guess = int(input())

if guess < answer:
    print('low: guess higher')
    guess = int(input())
    if guess==answer:
        print('you guessed right')
    else:
        print('you have guess wrong')
elif guess == answer:
    print('right answer')
else:
    print('high: guess lower')