# def is_safe_report(lvl):
#     return all(1 <= abs(lvl[i] - lvl[i + 1]) <= 3 for i in range(len(lvl) - 1)) and (
#         all(lvl[i] < lvl[i + 1] for i in range(len(lvl) - 1)) or
#         all(lvl[i] > lvl[i + 1] for i in range(len(lvl) - 1))
#     )

# def dampener(lvl):
#     return any(is_safe_report(lvl[:i] + lvl[i+1:]) for i in range(len(lvl)))

# def calculate_total_safe_reports(reports):
#     return sum(is_safe_report(list(map(int, report.split()))) or dampener(list(map(int, report.split()))) for report in reports)

# def read_lists_from_file(filename):
#     with open(filename, 'r') as file:
#         return [line.strip() for line in file]

# def main():
#     filename = 'Day2/d2.txt'
#     reports = read_lists_from_file(filename)
#     total_safe_reports = calculate_total_safe_reports(reports)
#     print("\nNumber of safe reports:", total_safe_reports, "\n")

# if __name__ == "__main__":
#     main()
# ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# def is_safe_report(lvl):
#     higher = True
#     lower = True
#     for i in range(len(lvl) - 1):
#         if not (1 <= abs(lvl[i] - lvl[i + 1]) <= 3):
#             return False
#         if lvl[i] >= lvl[i + 1]:
#             higher = False
#         if lvl[i] <= lvl[i + 1]:
#             lower = False
#     return higher or lower

# def dampener(lvl):
#     for i in range(len(lvl)):
#         modified_lvls = lvl[:i] + lvl[i+1:]
#         if is_safe_report(modified_lvls):
#             return True
#     return False

# def calculate_total_safe_reports(reports):
#     safe_rep_ctr = 0
#     for report in reports:
#         lvl = list(map(int, report.split()))
#         if is_safe_report(lvl) or dampener(lvl):
#             safe_rep_ctr += 1
#     return safe_rep_ctr

# def read_lists_from_file(filename):
#     with open(filename, 'r') as file:
#         reports = file.readlines()
#     reports = [report.strip() for report in reports]
#     return reports

# def main():
#     filename = 'Day2/d2.txt'
#     reports = read_lists_from_file(filename)
#     total_safe_reports = calculate_total_safe_reports(reports)
#     print("\nnumber of safe reports:", total_safe_reports, "\n")

# if __name__ == "__main__":
#     main()
# ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##original program
#
# def is_safe_report(lvl):
#     higher = True
#     lower = True
#     for i in range(len(lvl) - 1):
#         if abs(lvl[i] - lvl[i + 1]) < 1 or abs(lvl[i] - lvl[i + 1]) > 3:
#             return False
#         if lvl[i] >= lvl[i + 1]:
#             higher = False
#         if lvl[i] <= lvl[i + 1]:
#             lower = False
#     return higher or lower

# def dampener(lvl):
#     for i in range(len(lvl)):
#         modified_lvls = lvl[:i] + lvl[i+1:]
#         if is_safe_report(modified_lvls):
#             return True
#     return False

# def calculate_total_safe_reports(reports):
#     safe_rep_ctr = 0
#     for report in reports:
#         lvl = list(map(int, report.split()))
#         if is_safe_report(lvl) or dampener(lvl):
#             safe_rep_ctr += 1
#     return safe_rep_ctr

# def read_lists_from_file(filename):
#     with open(filename, 'r') as file:
#         reports = file.readlines()
#     reports = [report.strip() for report in reports]
#     return reports

# def main():
#     filename = 'Day2/d2.txt'
#     reports = read_lists_from_file(filename)
#     total_safe_reports = calculate_total_safe_reports(reports)
#     print("\nnumber of safe reports:", total_safe_reports, "\n")

# if __name__ == "__main__":
#     main()
# ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++