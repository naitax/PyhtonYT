secret_word = 'giraffe'
guess = ''
count = 0
limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if count < limit:
        guess = input('Enter guess: ')
        count += 1
        print('Its your {} guess'.format(count))
    else:
        out_of_guesses = True
    
if out_of_guesses:
    print('Out of guesses, you lose!')
else:
    print('You win!')
