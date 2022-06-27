import random
import array as arr



index = random.randint(5,10)
print('this is the index',index)
    
array_1 = arr.array("i", [index])

# num = random.randint(-10,10)
for i in range(1,index):
   
  num = random.randint(-10,10)
  array_1.append(num)

for x in array_1:
   
  print(x)

number_of_elements = len(array_1)

print("Number of elements in the list: ", number_of_elements)
