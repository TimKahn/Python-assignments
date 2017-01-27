list1 = []
list2 = []
common = []

for n in range(1,8):
    list1.append(int(raw_input('List comparison, LIST 1: enter element #' + str(n) + ': ' )))
for m in range(1,8):
    list2.append(int(raw_input('List comparison, LIST 2: enter element #' + str(m) + ': ' )))

for elem in list1:
    if elem in list2 and elem not in common:
        common.append(elem)

if common == []:
    print '\nNo items in common.'
else:
    print '\nThe elements in common are:'
    print common
