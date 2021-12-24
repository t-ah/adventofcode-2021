import re


def main():
    text = read_input("day24.txt")
    pattern = re.compile(r"inp w\nmul x 0\nadd x z\nmod x 26\ndiv z (\d+)\nadd x (-?\d+)\neql x w\neql x 0\nmul y 0\nadd y 25\nmul y x\nadd y 1\nmul z y\nmul y 0\nadd y w\nadd y (\d+)\nmul y x\nadd z y")
    modules = re.findall(pattern, text)
    
    data = [("", 0)]
    for i, module in enumerate(modules):
        divs = sum([1 for x in modules[i:] if x[0] == "26"])
        data = run([int(m) for m in module], data, divs)
    data = [d for d in data if d[1] == 0]
    print("max", max(data, key=lambda d: int(d[0])))
    print("min", min(data, key=lambda d: int(d[0])))


def run(module, prev_outputs, divs):
    outputs = set()
    for input, z in prev_outputs:
        if z > pow(26, divs):
            continue
        new_z = z
        if module[0] == 26: new_z //= 26
        comp = (z % 26) + module[1]
        for i in range(1, 10):
            if i != comp:
                outputs.add((input + str(i), 26 * new_z + i + module[2]))
            else:
                outputs.add((input + str(i), new_z))
    return outputs


def read_input(file_name):
    with open(file_name, "r") as f:
        return f.read()


if __name__ == "__main__":
    main()