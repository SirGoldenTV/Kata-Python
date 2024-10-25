def binary_array_to_number(arr):
  number = 0
  for idx, x in enumerate(arr):
    if x == 1:
        power2 = pow(2,(len(arr) - (idx + 1))) 
        number = number + power2
  return number

def binary_array_to_number_best(arr):
  return int("".join(map(str, arr)), 2)