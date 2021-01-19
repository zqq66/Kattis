

def LostLineup(lst):
    arr = sorted(range(len(lst)), key=lst.__getitem__)
    result = [str(i + 2) for i in arr]

    print("1", " ".join(result))


if __name__ == '__main__':

    length = input()
    lst = [int(i) for i in input().split()]

    LostLineup(lst)
    # n = int(input())
    # d = list(map(int, input().split()))
    #
    # lineup = [0] * n
    # lineup[0] = 1
    #
    # for person, pos in zip(range(2, n + 1), d):
    #     lineup[pos + 1] = person
    #
    # for each in lineup:
    #     print(each, end=' ')