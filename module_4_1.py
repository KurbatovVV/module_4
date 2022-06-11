massive_a=[2,8,1,9,3,6,4,7] #массив
element=4                   #Искомый элемент
      
      #Сортировка элементов массива

def module_4_1(massive_a):  #Создаем ф-ию
	n=len(massive_a)        #Определяем длину массива
	for i in range(n-1):    #Определяем число шагов
		for j in range(n-i-1): #Идём по всем элементам массива
			if massive_a[j]>massive_a[j+1]: #Сравниваем каждый элемент
				massive_a[j], massive_a[j+1]=massive_a[j+1], massive_a[j] #Меняем местами

	return massive_a

print (massive_a)
print (module_4_1(massive_a)) 

    #Бинарный поиск элемента

def binary_serch(massive_a, element, start, end):
	
	if start>end:
		return -1

	mid=(start+end)//2
	if element==massive_a[mid]:
		return mid
	if element<massive_a[mid]:
		return binary_serch(massive_a, element, start, mid-1)
	else:
		return binary_serch(massive_a, element, mid+1, end)

print ("Serch element " , element)
print ("element " , element, ":" , "index : " , binary_serch(massive_a,element,0, len(massive_a)))