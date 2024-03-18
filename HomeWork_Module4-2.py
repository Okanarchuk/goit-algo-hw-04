import sys

def get_cats_info(path):
    cats_info = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for f in file:
                id, name, age = f.strip().split(',')
                cats_info.append({
                    'id': id,
                    'name': name,
                    'age': int(age)
                })
            if len(cats_info) == 0:
                return None, None, 0
            return cats_info
        
    except OSError as err:
        print("Failed to open the file:", err)

cats_info = get_cats_info("C:\\Users\\Ксюша\\Documents\\My_repository\\Start\\cats_file.txt")
print(cats_info)