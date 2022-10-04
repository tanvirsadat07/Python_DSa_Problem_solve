# Initialize array
arr = [1, 2,  4, 2, 7, 8, 8, 3]
count = 0

print("Duplicate elements in given array: ")
# Searches for duplicate element
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if (arr[i] == arr[j]):

            count = count+1
            print(arr[i])
