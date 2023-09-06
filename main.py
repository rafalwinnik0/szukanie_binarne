def search(array, target):
    left = 0
    right = len(array)
    index = 0
    iteration = 0

    while left < right:
        ciag = []
        iteration += 1
        print(f"Iteration: {iteration}, left: {left}, right: {right}")

        for a in array[left:right]:
            ciag.append(a)
        print(ciag)

        index = (left + right) // 2
        print(f"Index: {index}, value: {array[index]}")
        print()

        if array[index] == target_number:
            return index
        else:
            if array[index] < target_number:
                left = index + 1
            else:
                right = index

    return -1

A = [1, 3, 4, 5, 7, 9, 11, 15, 16, 17, 19]
target_number = 11
index = search(A, target_number)
print(index)
