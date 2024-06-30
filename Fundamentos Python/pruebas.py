sequence = []
first_num = 0
second_num = 1
sum = first_num + second_num

sequence.append(first_num)
sequence.append(second_num)


while True:
    sequence.append(sum)
    first_num = sum
    second_num = second_num + sum
    sum = first_num + second_num
                
    sequence.append(second_num)
    sequence.append(sum) 


    if len(sequence) == 10:
        break


print(sequence)
