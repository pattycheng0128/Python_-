def bubble(list):
  list_length = len(list)
  
  for i in range(list_length-1):
    for j in range(list_length-i-1):
      if list[j] > list[j+1]:
        list[j], list[j+1] = list[j+1], list[j]
  return list


print(bubble([33, 66, 22, 9, 2]))
