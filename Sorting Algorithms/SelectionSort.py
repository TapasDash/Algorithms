def minn(listt,startIndex):
	loc = startIndex
	Min = listt[loc]
	for i in range(startIndex+1,len(listt)):
		if Min > listt[i]:
			Min = listt[i]
			loc = i
	return loc

def SelectionSort(listt):
	for i in range(len(listt) - 1):
		minIndex = minn(listt,i)
		'''
		temp = listt[i]
		listt[i] = listt[minIndex]
		listt[minIndex] = temp
		'''
		listt[i],listt[minIndex] = listt[minIndex],listt[i]

listt = [34,11,67,8,19]
SelectionSort(listt)
print(listt)
				
