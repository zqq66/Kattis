

def ants(l, numberOfAnts, lst):
    lst.sort()

    maximum = max(l - lst[0], lst[-1])
    index = numberOfAnts // 2
    minimum = 0
    while minimum == 0:
        if lst[index] < l // 2:
            index = (index + numberOfAnts) // 2
        elif lst[index] > l // 2:
            if lst[index - 1] < l // 2:
                minimum = max(l - lst[index], lst[0])
                break
            else:
                index = (numberOfAnts - index) // 2
    print(minimum, maximum)


def quicker(l, numberOfAnts, lst):

    minimum = 0
    maximum = 0
    for i in lst:
        temp_min = min(l - i, i)
        temp_max = max(l - i, i)
        if temp_min > minimum:
            minimum = temp_min
        if temp_max > maximum:
            maximum = temp_max
    print(minimum, maximum)


if __name__ == '__main__':
    numberOftests = input()
    for i in range(int(numberOftests)):
        l, numberOfAnts = input().split()
        lst = input().split()
        while len(lst) != int(numberOfAnts):
            lst += input().split()
        # ants(int(l), int(numberOfAnts), [int(j) for j in lst])
        quicker(int(l), int(numberOfAnts), [int(j) for j in lst])
