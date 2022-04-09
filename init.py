class Link:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination


def create_adjacency_list(edges_list):
    adjacency_list = {}
    for edge in edges_list:
        if edge.origin not in adjacency_list:
            adjacency_list[edge.origin] = []
        adjacency_list[edge.origin].append(edge.destination)


def edges(line):
    if(line != ""):
        origin, destination, _ = line.split(" ")
        return Link(origin, destination)


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
                        edges_list.append(edges(line))
                    if not line:
                        break
            create_adjacency_list(edges_list)
    except FileNotFoundError:
        print("File not found")


def main():
    read_file("data/d_ss.mtx")


main()
