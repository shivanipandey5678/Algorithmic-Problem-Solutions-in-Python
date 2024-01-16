//1
n=int(input())
res=[]
dic={}
count=1
for _ in range(n):
    s=input()
    res.append(s)
for i in range(0,len(res)):
    dic[res[i]]=count
    count+=1
print(dic["India"])
//2
tc=int(input())
for  i in range(tc):
    n=int(input())
    stri=input()
    mini=9999999
    dic={
        "w":0,"i":0,"s":0,"h":0}
    for i in range(len(stri)):
        if stri[i] in dic:
            dic[stri[i]]+=1
    mini=min(dic.values())
    for k in dic:
        if dic[k]==mini:
            print(mini)
            break

//3
n,m=map(int,input().split())
mat=[]
for i in range(n):
    arr=list(map(int,input().split()))
    mat.append(arr)
for i in range(n):
    if i%2==0:
        for j in range(m-1,-1,-1):
            print(mat[i][j],end=" ")
    elif i%2!=0:
        for j in range(m):
            print(mat[i][j],end=" ")
//4
n=int(input())
arr=list(map(int,input().split()))
dic={}
for i in range(n):
    if arr[i] not in dic:
        dic[arr[i]]=1
    else:
        dic[arr[i]]+=1
M=max(dic.values())
for k,v in dic.items():
    if v==M:
        print(k)
        break

//5
tc=int(input())
for i in range(tc):
    n=int(input())
    mat=[]
    for i in range(n):
        arr=list(map(int,input().split()))
        mat.append(arr)
    for i in range(n-1,0,-1):
        for j in range(n):
            if j==0:
                print(mat[i][j],end=" ")
    for i in range(n):
        for j in range(n):
            if i==j:
                print(mat[i][j],end=" ")
    for i in range(n-2,-1,-1):
        for j in range(n):
            if j==n-1:
                print(mat[i][j],end=" ")
    print()

