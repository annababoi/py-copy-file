def copy_file(command: str) -> None:
    ls = command.split(" ")
    if len(ls) != 3 or ls[0] != "cp":
        return
    c_file = ls[1]
    new_file = ls[2]
    if c_file == new_file:
        return
    try:
        with open(c_file, "r") as file_in, open(new_file, "w") as file_out:
            file_content = file_in.read()
            file_out.write(file_content)
    except FileNotFoundError:
        print(f"File {c_file} not found")
