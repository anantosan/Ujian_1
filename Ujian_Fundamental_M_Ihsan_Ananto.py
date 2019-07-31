#NO 1
def calculate_years(principal,interest,tax,desired):
    year=0
    while principal<desired:
        principal = principal + (principal * interest * (1-tax))
        year+=1

    return year

print(calculate_years(1000,0.05,0.18,1100))
print(calculate_years(1200,0.17,0.05,2000))
print(calculate_years(1500,0.07,0.6,5000))


#NO 2
def expandedform(num):
    z=''
    num=str(num)
    for i in range(len(num)):
        if num[i]!='0':
            angka=str(int(num[i])*(10**(len(num)-1-i)))
            z+=angka
            if i != (len(num)-1):
                z+=' + '
            else:
                z+=''
        else:
            z+=''
    return z
print(expandedform(3))
print(expandedform(12))
print(expandedform(149))
print(expandedform(1502))
print(expandedform(70304))

#NO 3
def tower_builder(n_floors,block_size):
    w,h = block_size
    z=''
    for k in range(n_floors):
        for j in range(h):
            for i in range(0,w+(4*k)):
                # if i<=(w+(4*k))
                z+='*'
            z+='\n'
    return z

print(tower_builder(3,(2,3)))
