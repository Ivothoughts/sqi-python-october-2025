def read_data(file_path):
    new_list = []
    try:
        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    separated_line = line.split(",")
                    name = separated_line[0]
                    age = int(separated_line[1])  
                    new_list.append((name, age))
    except FileNotFoundError:
        with open(file_path, "w") as f:
            f.write("""Alice,30
Fiona,28
Jasmine,31
George,33
Bob,25
Ella,22
Hannah,27
Daniel,40
Isaac,29
Charlie,35
""")
    return new_list
