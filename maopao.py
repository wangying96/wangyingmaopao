a=[15,78,23,56,758,415]
for i in range(len(a)-1):
    for j in range(len(a)-1-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print (a)
# D:\pycharm项目\wangying\bao1\maopao.py