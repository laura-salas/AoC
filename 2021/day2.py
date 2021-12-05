# problem link https://adventofcode.com/2021/day/2
def sol(lines):
    lines = lines.split("\n")
    commands = []
    for line in lines:
        line = line.strip()
        if line:
            commands.append(line)

    totalDir = {}
    aim = 0
    depth = 0
    for comm in commands:
        ins = comm.split(" ")
        if ins[0] in totalDir:
            totalDir[ins[0]] += int(ins[1])
        else:
            totalDir[ins[0]] = int(ins[1])

        if "down" in ins[0]:
            aim += int(ins[1])
        elif "up" in ins[0]:
            aim -= int(ins[1])

        elif "forward" in ins[0]:
            depth += (aim * int(ins[1]))

    return totalDir["forward"] * depth

inp = """input_here"""
sol(inp)
