import math


def __task1():
    print("Task 1")
    a = float(input("Enter number a: "))
    z = (math.sqrt(2) / 2) * math.sin(a / 2)
    print("z = ", z)


def __task2():
    print("Task 2")
    hours = int(input("Enter number of hours: "))
    amount_of_amebs = 1
    for i in range(0, hours + 1, 3):
        amount_of_amebs = 2 ** (i / 3)
    print("Amount of amebs after %d hours: %d" % (hours, amount_of_amebs))


def __task3():
    print("Task3")
    size = int(input("Enter size of an array: "))
    array = []
    for i in range(size):
        array.append(int(input("Enter %d number: " % i)))
    print("Max negative number in array: ", __find_max_negative(array))
    print("Average of odd numbers: ", __odd_average(array))
    print("Negative numbers:\n", __negatives(array))


def __find_max_negative(array):
    array_of_negatives = __negatives(array)
    if len(array_of_negatives) == 0:
        print("There is no negative numbers")
    else:
        return max(array_of_negatives)


def __odd_average(array):
    sum = 0
    counter = 0
    for element in array:
        if element % 2 == 0:
            sum += element
            counter += 1
    return sum / counter


def __negatives(array):
    array_of_negatives = []
    for element in array:
        if element < 0:
            array_of_negatives.append(element)
    return array_of_negatives


def start():
    __task1()
    __task2()
    __task3()


if __name__ == "__main__":
    start()
