Write a Python program to find the second smallest number in a list



def find_len(list1):
    length = len(list1)
    list1.sort()
    print("Second Smallest element is:", list1[1])
  
list1=[12, 45, 2, 41, 31, 10, 8, 6, 4]
Largest = find_len(list1)
