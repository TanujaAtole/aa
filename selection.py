def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Input & Output
arr = list(map(int, input("Enter numbers to sort (space-separated): ").split()))
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)



def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)
    n = max(job[1] for job in jobs)
    slots = [None] * n
    result = []

    for job in jobs:
        for i in range(min(n, job[1])-1, -1, -1):
            if slots[i] is None:
                slots[i] = job[0]
                result.append(job)
                break
    return result

# Input & Output
n = int(input("Enter number of jobs: "))
jobs = []
print("Enter jobs in format: ID Deadline Profit")
for _ in range(n):
    job_id, deadline, profit = input().split()
    jobs.append((job_id, int(deadline), int(profit)))
result = job_scheduling(jobs)
print("Scheduled jobs:")
for job in result:
    print(f"Job ID: {job[0]}, Deadline: {job[1]}, Profit: {job[2]}")

'''Enter number of jobs: 5
Enter jobs in format: ID Deadline Profit
a 2 100
b 1 19
c 2 27
d 1 25
e 3 15
'''


import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return dist

# Input & Output
n = int(input("Enter number of vertices: "))
graph = {}
for _ in range(n):
    u = input(f"Enter vertex {_+1}: ")
    m = int(input(f"How many neighbors for {u}? "))
    neighbors = []
    for _ in range(m):
        v, w = input("Enter neighbor and weight: ").split()
        neighbors.append((v, int(w)))
    graph[u] = neighbors

start = input("Enter start vertex: ")
distances = dijkstra(graph, start)
print("Shortest distances from", start)
for node in distances:
    print(f"{start} -> {node} = {distances[node]}")

'''Enter number of vertices: 4
Enter vertex 1: A
How many neighbors for A? 2
Enter neighbor and weight: B 1
Enter neighbor and weight: C 4
Enter vertex 2: B
How many neighbors for B? 2
Enter neighbor and weight: A 1
Enter neighbor and weight: C 2
Enter vertex 3: C
How many neighbors for C? 2
Enter neighbor and weight: A 4
Enter neighbor and weight: B 2
Enter vertex 4: D
How many neighbors for D? 0
Enter start vertex: A
'''