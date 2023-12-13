def menu():
    x = int(input("Какое задание вы хотите выбрать?"))

    if x == 1:
        first()
    elif x == 2:
        two()
    elif x == 3:
        third()
    elif x == 4:
        four()
    elif x == 5:
        five()
    elif x == 6:
        six()

def first():
    x = bool(False)
    print(x)

def two():
    mas = [1,2,3,4,5,6,7]
    a = mas[4:6]
    print(a)

def three():
    z = int(input("1 line"))
    x = int(input("2 line"))
    c = int(input("3 line"))
    if z + x > c:
        if z + c > x:
            if x + c > z:
                print("yes")
            else:
                print("no")
        else:
            print("no")
    else:
        print("no")


def get_permutations(number):
    if len(number) == 1:
        return [number]
    else:
        perms = []
        for i in range(len(number)):
            remaining = number[:i] + number[i+1:]
            sub_perms = get_permutations(remaining)
            for perm in sub_perms:
                perms.append(number[i] + perm)
        return perms

def get_digit_sum(number):
    digit_sum = 0
    for digit in number:
        digit_sum += int(digit)
    return digit_sum

def get_permutation_sum(number):
    permutations = get_permutations(str(number))

    permutation_sum = 0
    for perm in permutations:
        permutation_sum += int(perm)

    return permutation_sum

number = int(input("Введите число: "))
sum_of_permutations = get_permutation_sum(number)
print("Сумма всех чисел, полученных путем перестановки цифр числа {}: {}".format(number, sum_of_permutations))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result
def five():
    x = int(input("Введите число для факториала"))
    print(factorial(x))

def is_latin_square(matrix):
    n = len(matrix)

    for row in matrix:
        if sorted(row) != list(range(1, n+1)):
            return False
        
    for j in range(n):
        column = [matrix[i][j] for i in range(n)]
        if sorted(column) != list(range(1, n+1)):
            return False
    
    return True

def six():
    n = int(input("Введите размер матрицы: "))
    matrix = []
    for i in range(n):
        row = list(map(int, input(f"Введите {i+1}-ю строку через пробел: ").split()))
        matrix.append(row)

    if is_latin_square(matrix):
        print("yes")
    else:
        print("no")