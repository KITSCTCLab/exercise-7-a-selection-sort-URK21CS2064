from typing import List

def selectionSort(array, size) -> List[int]:
  # Write your code here
  for j in range(size-1):
    min =j
    for i in range(1,size):
      if array[min]>array[i]:
        min =i
      swap(array[min],array[j]

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
