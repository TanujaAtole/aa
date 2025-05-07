import heapq

def manhattan(state, goal):
    distance = 0
    for i, val in enumerate(state):
        if val == -1: continue
        goal_index = goal.index(val)
        distance += abs(i // 3 - goal_index // 3) + abs(i % 3 - goal_index % 3)
    return distance

def get_neighbors(state):
    neighbors = []
    zero = state.index(-1)
    row, col = zero // 3, zero % 3
    moves = [(-1,0),(1,0),(0,-1),(0,1)]  # up, down, left, right

    for dr, dc in moves:
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            new_idx = r * 3 + c
            new_state = state[:]
            new_state[zero], new_state[new_idx] = new_state[new_idx], new_state[zero]
            neighbors.append(new_state)
    return neighbors

def is_solvable(state):
    inv = 0
    arr = [x for x in state if x != -1]
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]: inv += 1
    return inv % 2 == 0

def print_state(state):
    for i in range(0, 9, 3):
        row = ['_' if x == -1 else str(x) for x in state[i:i+3]]
        print(" ".join(row))
    print()

def a_star(start, goal):
    heap = []
    visited = set()
    heapq.heappush(heap, (manhattan(start, goal), 0, start, []))

    while heap:
        f, g, state, path = heapq.heappop(heap)
        state_key = tuple(state)
        if state_key in visited:
            continue
        visited.add(state_key)

        if state == goal:
            for s in path + [state]:
                print_state(s)
            print(f"Solved in {len(path)} moves.")
            return

        for neighbor in get_neighbors(state):
            if tuple(neighbor) not in visited:
                h = manhattan(neighbor, goal)
                heapq.heappush(heap, (g + 1 + h, g + 1, neighbor, path + [state]))

    print("No solution found.")

# ----------- MAIN -----------

start = list(map(int, input("Enter start state (use -1 for empty): ").split()))
goal = list(map(int, input("Enter goal state (use -1 for empty): ").split()))

if is_solvable(start):
    a_star(start, goal)
else:
    print("This puzzle is unsolvable.")
