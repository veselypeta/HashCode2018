

def parse_data(filename):
    with open(filename, 'r') as data_file:
        lines = [x.strip('\n') for x in data_file.readlines()]
        print(lines)


parse_data("a_example.in")