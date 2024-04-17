ci = 0

def getInversions(arr, n) :
	# Write your code here.    
    def merge(arr, s, m, e):
        global ci
        n1 = m-s+1
        n2 = e-m
        l1= []
        l2= []
        for i in range(n1):
            l1.append(arr[s+i])
        for i in range(n2):
            l2.append(arr[m+1+i])

        l1.append(float('inf'))
        l2.append(float('inf'))

        i=0
        j=0
        for k in range(s, e+1):
            if l1[i] < l2[j]:
                arr[k] = l1[i]
                i+=1
            else:
                arr[k] = l2[j]
                for g in range(i, n1):
                    if l1[g] > 2*l2[j]:
                        print(l1[g], l2[j])
                        ci+=(n1-g)
                        break
                j+=1
        

    def mergesort(arr, s, e):
        global ci
        if s < e:
            m = (s+e)//2
            mergesort(arr, s, m)
            mergesort(arr, m+1, e)
            merge(arr, s, m ,e)

    mergesort(arr, 0, len(arr)-1)
    
    return ci
    
print(getInversions([1,3,2,3,1], 5))