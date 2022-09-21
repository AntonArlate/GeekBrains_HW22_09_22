def identical(line, i, s):
    count = 2
    while (i + count < len(line)) and (s == line[i+count]):
        count += 1

    print(type(str(count) + s))
    out_file.write(str(count) + s)
    # out_file.append(str(count) + s)
    return i + count


def not_identical(line, i, s):
    count = -2
    while (i +(-count) < len(line)) and (s != line[i+(-count)]):
        count -= 1

    # out_file.append(str(count) + line[i:i+(-count)])
    out_file.write(''.join(str(count) + line[i:i+(-count)]))
    return i +(-count)

with open("input.txt", "r") as in_file:
    with open("output.txt", "w") as out_file:
# in_file = ['aaaaassslkjh']
        # out_file = []

        for line in in_file:
            i=0
            count = 0
            while i < len(line)-1:
                s = line[i]
                if s == '\\': break
                if s == line[i+1]:
                    i = identical(line, i, s)
                else:
                    i = not_identical(line, i, s)
            
            # print(''.join(out_file))