# a=[1,2,3,4,5,6]
# i=0
# b=[]
# c=[]
# while i<len(a) :
#     if a[i]%2==0 :
#         print(a[i],"even number")
#         b.append(a[i])
#     else :
#         print(a[i],"odd number")
#         c.append(a[i])
#     i=i+1    
# print(b)
# print(c)  


# a=[1,2,3,4,5,6,7,8,9]
# i=0
# b=[]
# while i<len(a) :
#     if a[i]%3==0 :
#         b.append(20)
#     else :
#         b.append(a[i])
#     i=i+1
# print(b)            


# a="grecy is student of navgurukul"
# i=0
# count=0
# while i<len(a) :
#     if a[i]==" " :
#         count+=1
#     i+=1
# print(count)    


# a=[1,2,3,4,5,6,7,8]
# i=0
# b=2
# c=[]
# while i<len(a):
#     print(a[i:b])
#     c.append(a[i:b])
#     b=b+2
#     i=i+2
# print(c)    


# a=[[1,2,3],[4,6,5],[3,4,6]]
# i=0
# c=[]
# b=0
# while i<len(a) :
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]) :
#             if a[i][j]>b :
#                 b=a[i][j]
#             j=j+1
#         c.append(b)
#     i=i+1
# print(c)            


# a=[2,-4,-5,6,-7]
# i=0
# b=[]
# while i<len(a) :
#     if a[i]<0 :
#         b.append(0)
#     else :
#         b.append(a[i])    
#     i=i+1
# print(b)               


# a=[1,2,3,4,5,6,7,8,9,10]
# i=0
# sum=0
# b=1
# while i<len(a):
#     if i<5 :
#         sum=sum+a[i]
#     else :
#         b=b*a[i]    
#     i=i+1    
# print(sum)
# print(b)


# a=[2,5,8,6,5,4]
# i=0
# b=[]
# while i<len(a):
#     if a[i]**2+1 :
#         c=a[i]**2+1
#         b.append(c)
#     i=i+1
# print(b)      


# a=[1,2,3,4,5,6,7,8,9,10]
# x=int(input("enter the number :"))    
# i=0
# sum=0
# c=[]
# d=[]
# while i<len(a) :
#     if x<=a[i] :
#         c.append(a[i])
#         sum=sum+a[i]
#     i=i+1
# d.append(sum)    
# print(d)
# print(c)


# i=int(input("enter the number"))
# x=i
# rev=0
# while(i>0):
#     rev=rev*10+i%10
#     i=i//10
# if(x==rev):
#     print("num is parlidrome")
# else:
#     print("not parlidrome num")



