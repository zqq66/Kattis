
def IntegerDivision(lst, divider):
    result = {}
    output = 0
    for i in range(len(lst)):
        integer = int(lst[i])
        quotient = integer // divider
        if quotient not in result.keys():
            result[quotient] = 1
        else:
            result[quotient] += 1
    for i in result.keys():
        if result[i] - 1:
            output += int(result[i] * (result[i] - 1) / 2)

    return output


if __name__ == '__main__':
    length, divider = input().split()
    lst = input().split()
    print(IntegerDivision(lst, int(divider)))

