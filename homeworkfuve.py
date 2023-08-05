#Задание №1
print("Задание №1")
lam_fun = list(map(lambda x : "четные" if x % 2 == 0 else "нечетные", [1,2,3,4,5,6] ))
print(lam_fun, end ="\n\n" "Задание №2\n")

#Задание №2

return_str = list(map(lambda x: str(x) , [1,2,3,4,5,6,7]))
print(return_str, end ="\n\n" "Задание №3\n")

#Задание №3

polindrom = tuple(filter(lambda x: x[::] == x[::-1], ("mom","car","racecar","kayak","father")))
print(polindrom, end ="\n\n" "Задание №4\n")

#Задание №4
import time

def validator(func):
    def wrapper(a):
        start = time.time()
        func(a)
        end = time.time()
        print(f'Время выполнения функции {end - start}')
    return wrapper

@validator
def factorial(a):
    result = 1
    for i in range(a):
        result *= i

factorial(100000)

@validator
def pow(a):
    result = 0
    for i in range(a):
        result += i

pow(10000)

#Задание 5
print("\nЗадание №5")
def take_strin(value : str):
    dotIndex = value.find(".")
    if dotIndex > -1:
        left = value[:dotIndex]
        right = value[dotIndex+1:]
        if left.isdigit() and right.isdigit():
            print("Вы ввели положительное дробное число :", float(value))
        elif left[1:].isdigit() and left[0] == "-" and right.isdigit():
            print("Вы ввели отрицательное дробное число :", float(value))
        else:
            print("Вы ввели некоректное число!")
    elif value.isdigit():
        print("Вы ввели положительное целое число :", int(value))
    elif value[0] == "-" and value[1:].isdigit():
        print("Вы ввели отрицательное целое число :", int(value))
    else:
        print("Вы ввели некоректное число!")

take_strin("-5")
