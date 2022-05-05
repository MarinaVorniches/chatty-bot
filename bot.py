def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    print(r'Why do we use methods?' '\n'
          r'    1. To repeat a statement multiple times.' '\n'
          r'2. To decompose a program into several small subroutines.' '\n'
          r'3. To determine the execution time of a program.' '\n'
          r'4. To interrupt the execution of a program.' '\n')
    answer = int(input())
    right = 2
    while answer != right:
        print('Please, try again.')
        answer = int(input())



def end():
    print('Congratulations, have a nice day!')


greet('Chatty', '2022')  # change it as you need
remind_name()
guess_age()
count()
test()
end()
