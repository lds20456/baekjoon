nums=[]
for i in range(0,9):
    N = int(input())
    nums.append(N)
    
max=nums[0]
for j in nums:
    if max<j:
        max=j
print(max)

for i in range(9):
    if max == nums[i]:
        print(i+1)
        


    
        
        





    






