import random
def generator():
    print("please enter 14 number random or valid don't matter (;")
    user_input = input('> ')
    print('here is some information about the number you just enterd\n')
    result = []
    doplcate = []
    doplcate_dio = []
    double = []

    for i in user_input:
        result.append(int(i))
    for each in result:
        count = result.count(each)
        stri_a = str(each)
        stri_p = str(count)
        som = str(f"{stri_a} ===> {stri_p}")
        doplcate_dio.append(som)
    for number in result:
        if number not in doplcate:
            doplcate.append(number)
    for number in doplcate_dio:
        if number not in double:
            double.append(number)
    for i in double:
        print(i)
    for i in doplcate:
        print(i, end=' ')
    print("\n -------------")
    doplcate.sort()
    for i in doplcate:
        print(i, end=' ')
    print("\nthere is {} number".format(len(doplcate)))
    for i in range(14):                                     # generate random 14 number
        value = random.choice(doplcate)
        if i == 0:
            print("random numbers ==========>", end=' ')
        print(value, end='')


def multy():                                # another way to generate 14 number
    digit = input("\nenter three digit > ")
    number = int(digit)
    while True:
        number += number ** 2

        if len(str(number)) > 16:
            break
        print(number,"\n")

if __name__ == '__main__':
    generator()
    multy()
