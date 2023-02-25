# This was a headache, but thx God I managed do finish it
# The program receives a list of lists that represents intervals, they can overlap each other, and the problem is about
# getting the total sum of the intervals without counting the parts that overlap. So [(1, 4), [7, 10], [3, 5]] will
# return 7 because there are two non overlapping intervals (1-5, 7-10), the first of length 4 and the other, 3.
# I've made two solutions for this, the first one is commented down below, and it cannot be submitted because for very
# large input values, the program simply takes too much RAM and the computer literally explodes. But it was O(n) and I
# liked it very much u.u
# The second one is the one uncommented, and is the one I submitted because of the tests with large input values.
# I say "input values" because it was the values (the differences of the min and max values) that matters. In my O(n)
# solution, I created a list that is the size of that difference, so when it was big, the list was also big.
# My second solution is O(n^2), but at least is efficient in terms of memory management.

# iList = [(1, 4), [7, 10], [3, 5]]
iList = [(-103, 71), (315, 467), (157, 381), (487, 494), (207, 376), (-20, 333), (9, 57), (-374, 27), (-10, 160), (-179, 293), (21, 407), (-256, -252), (-402, 182), (321, 435), (-343, 420), (-152, 362), (437, 485), (-14, 380)]
# iList = [(-1000000000, 1000000000)]


iCount = 0
jCount = 0

for i in iList:
    if i != [0, 0]:
        for j in iList:
            if j != [0, 0] and iCount != jCount and i[1] >= j[0] and i[0] <= j[1]:
                iList.append([min(i[0], j[0]), max(i[1], j[1])])
                iList[iCount] = [0, 0]
                iList[jCount] = [0, 0]
                break
            jCount += 1
        jCount = 0
    iCount += 1

print(iList)

sumIntervals = 0

for i in iList:
    sumIntervals += i[1] - i[0]

print(sumIntervals)


#
#
#
# allElem = []
#
# for i in iList:
#     for j in i:
#         allElem.append(j)
#
# minElem = min(allElem)
#
# dif = (max(allElem) - minElem)
#
# arrAux = [False] * dif
#
# for i in iList:
#     for j in range(i[0]+1, i[len(i)-1]+1):
#         arrAux[j-minElem-1] = True
#
# print(arrAux.count(True))
