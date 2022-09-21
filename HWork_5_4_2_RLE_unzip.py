# Реализуйте RLE алгоритм: реализуйте модуль восстановления данных.


with open("output.txt", "r") as in_file:
    with open("output_unzip.txt", "w") as out_file:
        result = ''
        for line in in_file:
            i = 0
            while i in range(len(line)):


                if line[i] == '-': 
                    i+=1
                    result = result + line[i+1:i+1+int(line[i])]
                    i = i+int(line[i])+1
                
                elif int(line[i]) > 1:
                    result = result + line[i+1]*int(line[i])
                    i+=2

            print (result)
        out_file.write(result)


                