def read_lists_from_file(filename):
    left_list = []
    right_list = []

    with open(filename, 'r') as file:
        for line in file:
            left_value, right_value = map(int, line.split())
            left_list.append(left_value)
            right_list.append(right_value)

    return left_list, right_list

def calculate_total_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()

    total_distance = 0

    for left_value, right_value in zip(left_list, right_list):
        distance = abs(left_value - right_value)
        total_distance += distance

    return total_distance

def main():
    filename = 'Day1/d1.txt'
    left_list, right_list = read_lists_from_file(filename)

    total_distance = calculate_total_distance(left_list, right_list)
    print("distance in sum:", total_distance)


if __name__ == "__main__": 
    main()
