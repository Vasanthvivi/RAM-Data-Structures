datas = [5,4,3,2,1]

def sort(datas, len, left, right, mid):
    print(datas)
    if left < right:
        mid = (left + right) / 2
        sort(datas[left:mid+1])
        sort(datas[mid+1: right])