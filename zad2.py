def missingElements(list,n):
    missing = []
    for elem in range(1,n+1):
        if elem not in list:
            missing.append(elem)
    return(missing)
    
print(missingElements([2,3,7,4,9], 10))