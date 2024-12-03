def is_safe_report(lvl):
    higher = all(lvl[i] < lvl[i + 1] and 1 <= lvl[i + 1] - lvl[i] <= 3 for i in range(len(lvl) - 1))
    lower = all(lvl[i] > lvl[i + 1] and 1 <= lvl[i] - lvl[i + 1] <= 3 for i in range(len(lvl) - 1))
    return higher or lower

def dampener(lvl):
    for i in range(len(lvl)):
        modified_lvls = lvl[:i] + lvl[i+1:]
        if is_safe_report(modified_lvls):
            return True
    return False

def calculate_total_safe_reports(reports):
    safe_rep_ctr = 0
    for report in reports:
        lvl = list(map(int, report.split()))
        if is_safe_report(lvl) or dampener(lvl):
            safe_rep_ctr += 1
    return safe_rep_ctr

def read_lists_from_file(filename):
    with open(filename, 'r') as file:
        reports = file.readlines()
    reports = [report.strip() for report in reports]
    return reports

def main():
    filename = 'Day2/d2.txt'
    reports = read_lists_from_file(filename)

    total_safe_reports = calculate_total_safe_reports(reports)
    #print(total_safe_reports == 4, "\nnumber of safe reports:", total_safe_reports, "\n")
    print("\nnumber of safe reports:", total_safe_reports, "\n")

if __name__ == "__main__": 
    main()