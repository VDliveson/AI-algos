def noOfOperations(m,n,x):
    count =1
    fromJug=n
    toJug=0
    
    while(fromJug!=x):
        if(fromJug):
            if(fromJug+toJug<=m):
                toJug=fromJug+toJug
                fromJug=0
            else:
                fromJug=fromJug-m+toJug
                toJug=m
            count+=1
            
        if(fromJug==0):
            fromJug=n
            count+=1
            
        if(toJug==m):
            toJug=0
            count+=1
        
    return count    
        

m=int(input("Enter the capacity of smaller jug "))
n=int(input("Enter the capacity of larger jug" ))
x=int(input("Enter the capacity of water needed in larger jug "))

print("Number of operations:",noOfOperations(m,n,x))

