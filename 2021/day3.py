def sol(bits_inparsed):
    bits_inparsed = bits_inparsed.split("\n")
    bits = []
    for line in bits_inparsed:
        line = line.replace(" ", "")
        if line:
            bits.append(line)

    def find_numbers(arr, bit):
        no_of_1s = [x[bit] for x in arr].count("1")
        no_of_0s = len(arr) - no_of_1s
        return [no_of_0s, no_of_1s]

    oxygen = bits.copy()
    co2 = bits.copy()
    bit = 0
    while len(oxygen) != 1:
        result = find_numbers(oxygen, bit)
        zeroes = result[0]
        ones = result[1]

        def check_equals(number):
            if ones >= zeroes:
                return number[bit] == "1"
            else:
                return number[bit] == "0"

        oxygen = list(filter(check_equals, oxygen))
        bit += 1

    bit = 0
    while len(co2) != 1:
        result = find_numbers(co2, bit)
        zeroes = result[0]
        ones = result[1]

        def check_equals(number):
            if zeroes <= ones:
                return number[bit] == "0"
            else:
                return number[bit] == "1"

        co2 = list(filter(check_equals, co2))
        bit += 1
    return int(oxygen[0], 2) * int(co2[0], 2)

inp = """input_here"""
sol(inp)
