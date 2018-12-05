def BubbleSort(listt):
	for roundd in range(len(listt) - 1):
		for i in range(len(listt) - 1 - roundd):
			if listt[i] > listt[i+1]:
				'''
				temp = listt[i]
				listt[i] = listt[i+1]
				listt[i+1] = temp
				'''
				listt[i],listt[i+1] = listt[i+1],listt[i]

listt = [34,19,5,17]
BubbleSort(listt)
print(listt)
