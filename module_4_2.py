massiv_b = [2,4,1,8,4,9]

def insertion_f(massiv_b):
	for i in range(1, len(massiv_b)):
		y=massiv_b[i]
		j=i-1
		while j>=0 and massiv_b[j]>y:
			massiv_b[j+1]=massiv_b[j]
			j-=1
		massiv_b[j+1]=y

insertion_f(massiv_b)
print (massiv_b)