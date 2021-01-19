

def CaloriesFromFat():
    calory_table = [9, 4, 4, 4, 7]
    input_table = input().split()
    while True:
        fat_calory = 0
        total_calory = 0
        while input_table != ['-']:
            calory = 0
            percentage = 0
            helper = True
            if input_table[0][-1] == "%":
                helper = False
            for i in range(len(input_table)):
                if input_table[i][-1] == "g":
                    calory += float(input_table[i][0:-1]) * calory_table[i]
                    input_table[i] = float(input_table[i][0:-1]) * calory_table[i]
                elif input_table[i][-1] == "C":
                    calory += float(input_table[i][0:-1])
                    input_table[i] = float(input_table[i][0:-1])
                else:
                    percentage += float(input_table[i][0:-1]) / 100
                    input_table[i] = float(input_table[i][0:-1]) / 100
            total_calory += calory / (1 - percentage)
            current_calory = calory / (1 - percentage)
            # print(input_table)
            # print("calory", calory)
            # print("percentage", percentage)
            # print("total_calory", total_calory)
            if not helper:
                fat_calory += float(input_table[0]) * current_calory
            else:
                fat_calory += float(input_table[0])
                # print("fat_calory", fat_calory)
            input_table = input().split()
        print(round(100 * fat_calory / total_calory), end='%\n')

        # print("fat_calory2", fat_calory)
        # print("total_calory2", total_calory)
        input_table = input().split()
        if input_table == ['-']:
            break


if __name__ == '__main__':

    CaloriesFromFat()