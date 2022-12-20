def canVisitAllRooms(rooms):
    visited, stack = set(), [0]
    while stack:
        i = stack.pop()
        visited.add(i)
        stack.extend([j for j in rooms[i] if j not in visited])
    return len(visited) == len(rooms)


rooms = [[1], [2], [3], []]
print('input  : ', rooms)
print('output : ', canVisitAllRooms(rooms))

rooms2 = [[1, 3], [3, 0, 1], [2], [0]]

print('input  : ', rooms2)
print('output : ', canVisitAllRooms(rooms2))
