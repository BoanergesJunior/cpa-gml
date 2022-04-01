class Link:
    def __init__(self, origin, destination, weight):
        self.origin = origin
        self.destination = destination
        self.weight = weight


def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            adjacent_list_link = []
            while True:
                line = file.readline()
                if(line != ""):
                    adjacent_list_link.append(adjacent_list(line))
                if not line:
                    break
    except FileNotFoundError:
        print("File not found")


def adjacent_list(line):
    if(line != ""):
        origin, destination, weight = line.split()
        return Link(origin, destination, weight)


def main():
    read_file("file.txt")


main()
