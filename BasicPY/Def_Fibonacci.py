def febo(fe):
    if fe <= 1:
        return fe
    else:
        return febo(n-1) + febo(n-2)
    
for i in range(10):
    print(i)