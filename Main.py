from typing import List

def selectionSort(array, size) -> List[int]:
  # Write your code here
  for j in range(size-1):
    min =arr[j]
    minpos=j
    for i in range(1,size):
      if array[j]<min:
        min =array[i]
        minpos=j
    temp=array[i]
    array[i]=min
    array[minpos]=temp
  return array 

# Do not change the following code
in_data = input()
data = []
for item in in_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
