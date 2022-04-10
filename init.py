import time

EDGES_LIST = []
visited = []


class Link:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination
        self.weight = 0


def write_file_mtx():
    for edge in EDGES_LIST:
        with open("output.mtx", "a") as file:
            file.write(str(edge.origin) + " " +
                       str(edge.destination) + " " + str(edge.weight) + "\n")


def print_edges():
    write_file_mtx()
    for edge in EDGES_LIST:
        print('Edge: [' + edge.origin + ',' +
              edge.destination + ']', 'Weight:', edge.weight)


def create_adjacency_list(edges_list):
    adjacency_list = {}
    for edge in edges_list:
        if edge.origin not in adjacency_list:
            adjacency_list[edge.origin] = []
        adjacency_list[edge.origin].append(edge.destination)
    return adjacency_list


def increment_weight(origin, destination):
    for edge in EDGES_LIST:
        if edge.origin == origin and edge.destination == destination:
            edge.weight += 1


def edges(line):
    if(line != ""):
        origin, destination, _ = line.split(" ")
        if origin != destination:
            return Link(origin, destination)
    return None


def dfs_visit(adjacency_list, vertex, visited):
    visited.append(vertex)
    for neighbor in adjacency_list[vertex]:
        if neighbor not in visited:
            increment_weight(vertex, neighbor)
            dfs_visit(adjacency_list, neighbor, visited)


def dfs(adjacency_list):
    for vertex in adjacency_list:
        if vertex not in visited:
            dfs_visit(adjacency_list, vertex, [])
    print_edges()


def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            edges_list = []
            while True:
                line = file.readline()
                if line.__contains__("%"):
                    continue
                else:
                    if(line != ""):
                        if edges(line) is not None:
                            edges_list.append(edges(line))
                            EDGES_LIST.append(edges(line))
                    if not line:
                        break
            adjacency_list = create_adjacency_list(edges_list)

            time_start = time.time()
            dfs(adjacency_list)
            time_end = time.time()
            Time = time_end - time_start
            print("Time:", Time)
    except FileNotFoundError:
        print("File not found")


def main():
    read_file("data/olm500.mtx")


main()
