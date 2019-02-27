

def parse_data(filename):
    with open(filename, 'r') as data_file:
        lines = [x.strip('\n') for x in data_file.readlines()]
        n_rows, n_columns, n_vehicles, n_rides, ride_bonus, n_steps = tuple(lines[0].split(' '))


parse_data("b_should_be_easy.in")