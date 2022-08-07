import random
inputNumber = None
count = 1
flag = True
while flag:
    num = input('Type a number for an upper bound: ')
    # checking whether the given number is integer or string
    if num.isdigit():  # if integer then it will exit from loop else keeps on checking
        num = int(num)
        flag = False
    else:
        print('Invalid input! Try Again')

# random number will be generated from 1 to upperbound
randomNumber = random.randint(1, num)

while inputNumber != randomNumber:
    inputNumber = input('Guess a number between 1 and '+str(num)+" : ")
    if inputNumber.isdigit():
        inputNumber = int(inputNumber)
        # Both the input and guessed number are same
    if inputNumber == randomNumber:
        print('You got it!')
    else:
        print("Wrong Guess Try Again ")
        p = input("Want a clue=> 1 or 0 ?\n=>")
        if p == "1":
            ch = input(
                "\nClues:\n1)Divisor \n2)Muliplication \n3)Greater Or Lesser\n=>")
            if ch == "1":
                i = 1
                while i <= randomNumber:
                    if (randomNumber % i == 0):
                        print(i, end=" ")
                    i = i + 1
            if ch == "2":
                if inputNumber % randomNumber == 0:
                    print('The number is multiple of ', randomNumber)
            if ch == "3":
                if inputNumber < randomNumber:
                    print('Greater then ', inputNumber)
                if inputNumber > randomNumber:
                    print('Lesser then ', inputNumber)
        count += 1
print('It took you ', count, ' guesses!')
