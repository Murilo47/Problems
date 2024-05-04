import numpy as np

airports = ["BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND", "ICN", "JFK", "LGA", "LHR", "ORD", "SAN", "SFO", "SIN", "TLV", "BUD"]

routes = [  
    ["DSM", "ORD"],
    ["ORD", "BGI"],
    ["BGI", "LGA"],
    ["SIN", "CDG"],
    ["CDG", "SIN"],
    ["CDG", "BUD"],
    ["DEL", "DOH"], 
    ["DEL", "CDG"],
    ["TLV", "DEL"],
    ["EWR", "HND"],
    ["HND", "ICN"],
    ["HND", "JFK"],
    ["ICN", "JFK"],
    ["JFK", "LGA"],
    ["EYW", "LHR"],
    ["LHR", "SFO"],
    ["SFO", "SAN"],
    ["SFO", "DSM"],
    ["SAN", "EYW"],
]


# adj_matrix = [[0 for _ in range(len(airports))] for _ in range(len(airports))]
adj_matrix = np.identity(len(airports))

# print(adj_matrix)

for route in routes:
    origin = airports.index(route[0])
    destination = airports.index(route[1])
    adj_matrix[origin][destination] = 1

# print(adj_matrix)

def find_all_conections(airport, connections):
    adj = adj_matrix[airport]
    # print("-----")
    # print(adj)
    # print("-----")
    for index in range(len(adj)):
        if adj[index] == 1 and index not in connections:
            connections.append(index)
            connections = find_all_conections(index, connections)
    return connections

# print(find_all_conections(2, []))


def add_connections_to_matrix(airport_to_add):
    connections = sorted(find_all_conections(airport_to_add, []))
    for index in connections:
        if adj_matrix[airport_to_add][index] == 0:
            adj_matrix[airport_to_add][index] = 1


for i in range(len(adj_matrix)):
    add_connections_to_matrix(i)

# print(adj_matrix)

airports_connected = [10]

def count_connections_excluding_already_connected(airports_connected):
    numbers = []
    for i in range(len(adj_matrix)):
        count = 0
        for j in range(len(adj_matrix)):
            if j not in airports_connected and adj_matrix[i][j] == 1:
                count += 1
        numbers.append(count)

    return numbers

# print(count_connections_excluding_already_connected(airports_connected))
# print(np.argmax(count_connections_excluding_already_connected(airports_connected)))

# adj = adj_matrix[6]
# for index in range(len(adj)):
#     if adj[index] == 1 and index not in airports_connected:
#         airports_connected.append(index)

# airports_connected.sort()

# print(airports_connected)

i = 0
while len(airports_connected) < len(airports):
    i += 1
    n = np.argmax(count_connections_excluding_already_connected(airports_connected))
    adj = adj_matrix[n]
    for index in range(len(adj)):
        if adj[index] == 1 and index not in airports_connected:
            airports_connected.append(index)
    airports_connected.sort()

print(i)
print(airports_connected)