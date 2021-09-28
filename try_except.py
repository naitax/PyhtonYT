try:
    answer = 10/0
    number = int(input('Enter a number: '))
    print(number)
except ZeroDivisonError as err:
    print(err)
except ValueError:
    print('invalid input')
