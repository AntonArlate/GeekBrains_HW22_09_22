# Реализуйте RLE алгоритм: реализуйте модуль сжатия данных.

def serial_find(line):
    result = []
    count = 0
 
    if len(line) == 1:
        result.append((1, int(line[0])))
        return result
 
    for i in range(len(line)):
        count += 1
        if (i + 1) == len(line) or line[i] != line[i + 1]:
            result.append((count, line[i]))
            count = 0

    return result


def zip_cort(cort):
    result = ''
    count = 0
    temp = [0,'']
    for i in range(len(cort)):
        s = cort[i]
        if s[0]>1:
            if temp[0] != 0:
                result = result + str(temp[0]) + temp[1]
                temp = [0,'']
            result = result + str(s[0]) + s[1]
            # print (result)
        else: 
            temp = [temp[0]-s[0],temp[1]+s[1]]

    if temp[0] != 0:
        result = result + str(temp[0]) + temp[1]
    return (result)
            

with open("input.txt", "r") as in_file:
    with open("output.txt", "w") as out_file:

        for line in in_file:
            cort = serial_find(line)
            print(cort)
            string = zip_cort(cort)
            out_file.write(string)

                