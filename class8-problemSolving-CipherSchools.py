n= 5
# for i in range(n):
#     for j in range(n):
#         print(i,end=" ")
#     print()    

# print()

# for i in range(n):
#     for j in range(n):
#         print(j,end=" ")
#     print() 

print()
for i in range(n):
    for j in range(n):
        print(max(i,j),end=" ")        
    print() 

# for i in range(n):
#     for j in range(n):
#         print(n-i,end=" ")
#     print()            
# print()
# for i in range(n):
#     for j in range(n):
#         print(n-j,end=" ")
#     print()
print()    
for i in range(n):
    for j in range(n):
        print(max(n-j,n-i),end=" ") 
    print()               
print()

for i in range(n):
    for j in range(n):
        print((max(n-j,n-i,i+1,j+1)),end=" ")
    print()    