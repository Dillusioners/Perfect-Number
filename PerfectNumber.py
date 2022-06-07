while True:
    print('**********************************************')
    number = int(input('Enter a number: '))
    total = 0
    i = 0
    while total < number:
        total = total + i
        i=i+1
        print(total , "=", i,)

    if total == number:
        print(f'The number {number} is a perfect number.')
    else:
        print(f'The number {number} is not a perfect number.')