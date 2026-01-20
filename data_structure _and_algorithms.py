#Array (List in Python),Stores elements in contiguous memory.Use when: fast access by index,Access: O(1)
arr = [10, 20, 30, 40]
print(arr[2])     # 30
arr.append(50)
arr.remove(20)

#Example
numbers = [34, 12, 9, 56, 21]
print("Original array:", numbers)


#String,Immutable sequence of characters.
s = "python"
print(s[::-1])   # reverse


#Stack (LIFO) ,Last In, First Out,Push/Pop: O(1),Use: undo, function calls
stack = []
stack.append(10)
stack.append(20)
print(stack.pop())   # 20

#Example
stack = []

for n in numbers:
    stack.append(n)

print("Stack pop:", stack.pop())



#Queue (FIFO),First In, First Out,Use: scheduling, buffering
from collections import deque

q = deque()
q.append(10)
q.append(20)
print(q.popleft())   # 10

#Example
from collections import deque

queue = deque(numbers)
print("Queue dequeue:", queue.popleft())



#Linked List. Each node points to next node.Types:Singly,Doubly,Circular
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

current = head
print("Linked List:", end=" ")
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")
      


#Dictionary (Hash Map),Key–value pairs,Search: O(1)
student = {"name": "John", "age": 20}
print(student["name"])


#Set,Unique elements
s = {1, 2, 3, 3}
print(s)   # {1,2,3}


#Tree (Binary Tree),Used in:Hierarchy,Searching,Databases
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


#Graph,Nodes + edges
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": []
}





#PART 2: Algorithms,Searching Algorithms

#Linear Search
def linear_search(arr, x):
    for i in arr:
        if i == x:
            return True
    return False


#Binary Search (Sorted array)
def binary_search(arr, x):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return False



#Algorithms,Sorting Algorithms

#Bubble Sort
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
bubble_sort(numbers)
print("Sorted array:", numbers)
               


#Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


#Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


#Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


#Recursion
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


#Dynamic Programming,Fibonacci (Optimized)
def fib(n):
    dp = [0,1]
    for i in range(2,n+1):
        dp.append(dp[i-1]+dp[i-2])
    return dp[n]


#Graph Algorithms,BFS
from collections import deque

def bfs(graph, start):
    visited = set()
    q = deque([start])

    while q:
        node = q.popleft()
        if node not in visited:
            print(node)
            visited.add(node)
            q.extend(graph[node])


#DFS
def dfs(graph, node, visited=set()):
    if node not in visited:
        print(node)
        visited.add(node)
        for n in graph[node]:
            dfs(graph, n, visited)



