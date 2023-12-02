### Eratosthenes sieve ----------
n = 1000
arr = []

for i in range(n):
    arr.append(i)
arr[1] = 0
for i in range(n):
    if arr[i] != 0:
        j = i * 2
        while j < n:
            arr[j] = 0
            j += i

for elim in arr:
    if elim != 0:
        print(elim, end=' ')
### -----------------------------

### Search algorithms ###########
import random

n = 40
arr = list()

for i in range(n):
    number = random.randint(1, 100)
    arr.append(number)

to_search = random.randint(1, 100)
answer = -1

### Linear search ---------------
# for i in range(n):
#     if arr[i] == to_search:
#         answer = i
#         break

### Binary search ---------------
# arr.sort()
# low = 0
# high = len(arr) - 1
# while low <= high:
#     mid = (low + high) // 2
#     if arr[mid] < to_search:
#         low = mid + 1
#     elif arr[mid] > to_search:
#         high = mid - 1
#     else:
#         answer = mid
#         break

### Interpolation search ---------
arr.sort()
left = 0
right = len(arr) - 1
while (left <= right and to_search >= arr[left] and to_search <= arr[right]):
    index = left + int((float(right - left) / (arr[right] - arr[left])) * (to_search - arr[left]))
    if arr[index] == to_search:
        answer = index
        break
    if arr[index] < to_search:
        left = index + 1
    else:
        right = index - 1

### ------------------------------

print(arr)
print(to_search)
print("------")

if answer != -1:
    print(f"Found, index: {answer}" )
else:
    print("Not found")
