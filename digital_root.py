# def digital_root(n):
#     s=0
#     for i in str(n):
#         s+=int(i)
#     return s
# print(digital_root(123))
def digital_root(n):
    s=0
    for i in str(n):
        s+=int(i) 
    t=s
    if t>10:
        return digital_root(t)
    else:
        return t
print(digital_root(10))
def check(n):
    if n==1:
        return True
    else:
        return False
print(check(1))