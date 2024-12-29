import os

def create_csv_file(filename: str, headers: list) -> bool:
    try:
        if file_exists(filename):
            return True
        
        headers_string = ", ".join(headers)
        with open(filename, "w") as f:
            f.write(f"{headers_string}\n")
    except Exception as e:
        print(f"create_csv error: {e}")
        return False
    return True
        

def write_data_to_csv(filename: str, content: list) -> bool:
    try:
        data_string = ",".join(content)
        with open(filename, "a+") as f:
            f.write(f"{data_string}\n")
    except Exception as e:
        print(f"write_csv error: {e}")
        return False
    return True

def file_exists(filename: str) -> bool:
    try:
        with open(filename, "r"):
            pass
        return True
    except OSError:
        return False