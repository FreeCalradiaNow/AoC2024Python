def is_safe_report(levels):
    increasing = all(levels[i] < levels[i + 1] and 1 <= levels[i + 1] - levels[i] <= 3 for i in range(len(levels) - 1))
    decreasing = all(levels[i] > levels[i + 1] and 1 <= levels[i] - levels[i + 1] <= 3 for i in range(len(levels) - 1))
    return increasing or decreasing

def calculate_total_safereports(reports):
    safe_count = 0
    for report in reports:
        levels = list(map(int, report.split()))
        if is_safe_report(levels):
            safe_count += 1
    return safe_count

def read_lists_from_file(filename):
    with open(filename, 'r') as file:
        reports = file.readlines()
    reports = [report.strip() for report in reports]
    return reports

def main():
    filename = 'Day2/d2.txt'
    reports = read_lists_from_file(filename)

    total_safereports = calculate_total_safereports(reports)
    print("total number of safe reports:", total_safereports)

if __name__ == "__main__": 
    main()