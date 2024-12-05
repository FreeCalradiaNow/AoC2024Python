# xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
# Only the four highlighted sections are real mul instructions. 
# Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).
# Scan for uncurrupted mul instrunctions

# 1. Datei einlesen, dabei parsen
# 2. geparste mul Paare multiplizieren
# 3. Produkte summieren
# 4. Ergebnis ausgeben / Zwischenergebnisse abgreifen: uncurrupted mul instructions, products, product sum

# parsen nach "mul(n,n)" wobei n eine bis zu zweistellige Zahl sein darf

def read_lists_from_file(filename):
    with open(filename, 'r') as file:
        reports = file.read()
        # reports = file.readline()
        mul_start = reports.find('mul(') + len('mul(')
        mul_end = reports[mul_start:].find(')')
        mul = reports[mul_start:mul_start + mul_end]
    reports = [report.strip() for report in reports]
    return mul

def main():
    filename = 'Day3/d3_TEST.txt'
    all_instructions = read_lists_from_file(filename)

    added_up_uncurrupted_mul_instructins = all_instructions #calculate_auumi(reports)
    print("added up uncurrupted mul instructions products:\n", added_up_uncurrupted_mul_instructins)

if __name__ == "__main__": 
    main()

