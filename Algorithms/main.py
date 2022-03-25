import math
items = [4,3,2,1]

#merge sort
def mergeSort(items, left, right):
    if(left < right):
        mid = math.floor( (left + right)/2)
        mergeSort(items, left, mid)
        mergeSort(items, mid + 1, right)
        merge(items,mid,left, right)

# merge
def merge(items:list, mid, left, right):
    print("merging")
    leftArray = items[left:mid + 1]
    rightArray = items[mid+1:right+1]
    a = 0
    b = 0
    c = left
    while(a < len(leftArray) and b < len(rightArray)):
        if(leftArray[a] <= rightArray[b]):
            items[c] = leftArray[a]
            a += 1
        else:
            items[c] = rightArray[b]
            b += 1
        c += 1
    while(a < len(leftArray)):
        items[c] = leftArray[a]
        a += 1
        c += 1
    while(b < len(rightArray)):
        items[c] = rightArray[b]
        b += 1
        c += 1

mergeSort(items, 0, len(items) - 1)
print(items)
# # insertion sort
# def insertionSort():
#     for i in range(1, len(items)):
#         currentElement = items[i]
#         index = i - 1
#         while (index >= 0) and currentElement <= items[index]:
#             items[index + 1] = items[index]
#             index -= 1
#         items[index + 1] = currentElement
#     print(items)
# # call to push in stack
