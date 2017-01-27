user_input = str(raw_input('Enter some whole numbers separated by commas: '))
input_list = user_input.split(',')

answer = []
for n in range(0,len(input_list)-1,2): #iterate through pairs, stop one short of list length
    answer.append((input_list[n], input_list[n+1]))

print answer
