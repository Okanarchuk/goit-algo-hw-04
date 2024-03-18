import sys

def total_salary(path):
    salaries_list = []
    try:
        with open(path, "r", encoding="utf-8") as salaries_txt:
            for line in salaries_txt:
                name, salary = line.strip().split(',')
                salaries_list.append((name.strip(), int(salary)))
            if len(salaries_list) == 0:
                return None, 0, 0
            total = sum(salary for _, salary in salaries_list)
            average = total / len(salaries_list)
            return total, average

    except OSError as err:
        print("Failed to open the file:", err)

total, average = total_salary("C:\\Users\\Ксюша\\Documents\\My_repository\\Start\\salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
