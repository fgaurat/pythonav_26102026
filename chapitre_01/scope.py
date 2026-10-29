
a = 12

def f():
    global a
    
    a =22
    print(a)
    


print(a) # 12
f()# 14
print(a)# 12