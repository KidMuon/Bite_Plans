import hashlib, datetime

def hash_string(string, salt = datetime.datetime.now().strftime(r"%I:%M:%S%f_%Y%m%d")):
    salted_string = string + salt
    return hashlib.sha256(salted_string.encode()).hexdigest()

description = r"All Natural* 93% Lean/7% Fat Lean Group Beef Patties, 4 Count, 1 lb Tray"
print(hash_string(description))