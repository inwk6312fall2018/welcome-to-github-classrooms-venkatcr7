import csv
name="Crime.csv"
def crimelist(n):
	with open("crime.csv") as csvfile:
		readCSV=csv.reader(csvfile,"r")
	a=dict()
	b=dict()
	list1=[]
	list2=[]
	for i in readCSV:
		i.strip()
		i.split()
		list1.append(i[-1])
		list2.append(i[-2])
	for j in list1:
		if j not in line:
			a[j]=1
		else:
			a[b]+=1
	print(prettytable(headers=['crimetype','CrimeId','CrimeCount']))
	def reverse_lookup(d,v):
		for k in a:
			if d[k] == v:
				print(prettytable(k)) #reverse lookup functio
crimelist(name)
