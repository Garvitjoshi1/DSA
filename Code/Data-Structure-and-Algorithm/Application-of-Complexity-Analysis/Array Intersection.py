# Time Complexity: O(mlogm + nlogn)

def intersection(arr1, arr2):
    arr1.sort()
    arr2.sort()

    p1 = 0
    p2 = 0

    while p1 < len(arr1) and p2 < len(arr2):

        if arr1[p1] == arr2[p2]:
            print(arr1[p1])
            p1 += 1
            p2 += 1

        elif arr1[p1] > arr2[p2]:
            p2 += 1

        elif arr1[p1] < arr2[p2]:
            p1 += 1


n1 = int(input())
arr1 = list(int(i) for i in input().strip().split(' ')[:n1])

n2 = int(input())
arr2 = list(int(i) for i in input().strip().split(' ')[:n2])

intersection(arr1, arr2)