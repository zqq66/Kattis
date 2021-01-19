

def SymmetricOrder():
    name = input()
    set_number = 0
    name_set = [0]
    while name != '0':

        if name.isdigit():
            index = 0
            turn_to_last = False
            name_set = [0 for i in range(int(name))]
            set_number += 1

        else:
            if turn_to_last:
                name_set[len(name_set) - index] = name
                turn_to_last = False
            else:
                name_set[index] = name
                index += 1
                turn_to_last = True
        if 0 not in name_set:
            print("SET", set_number)
            for j in name_set:
                print(j)

        name = input()


if __name__ == '__main__':
    SymmetricOrder()
