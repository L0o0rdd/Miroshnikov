# Даны три целых числа, одно из которых отлично от двух других, равных между собой.
# Определить порядковый номер числа, отличного от остальных
try:
    a = int(input("Введите число 1: "))
    b = int(input("Введите число 2: "))
    c = int(input("Введите число 3: "))

    if a == b:
        print("3")
    elif a == c:
        print("2")
    else:
        print("1")
except:
    print('Error')