from dayOnePuzzleOne import read_lists_from_file

def calculate_similarity_score(left_list, right_list):
    similarity_score = 0

    for left_value in left_list:
        occurrence = right_list.count(left_value)
        similarity_score += left_value * occurrence

    return similarity_score

def main():
    filename = 'Day1/d1.txt'
    left_list, right_list = read_lists_from_file(filename)

    similarity_score = calculate_similarity_score(left_list, right_list)
    print("similarity score:", similarity_score)

if __name__ == "__main__":
    main()
