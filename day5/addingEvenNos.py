print("enter a number between 1 to 1000")
target = int(input()) 
total=0
for number in range(0,target+1,2):
  total+=number
print(total)
