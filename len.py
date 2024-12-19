a = [1, 2, 3, 4, 5]
i = 0

while True:
    try:
        a[i]  
        i += 1  
    except IndexError:  
        break  

print(i)  
