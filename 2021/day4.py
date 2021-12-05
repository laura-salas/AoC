# problem link: https://adventofcode.com/2021/day/4
def sol(bingo_unparsed):
    bingo_unparsed = bingo_unparsed.split("\n")
    bingo = []
    for line in bingo_unparsed:
        line = line.strip()
        if line:
            bingo.append(line)
    numbers = [int(x) for x in list(filter(lambda x: x != "", bingo[0].split(",")))]
    numbers_set = set(numbers)
    boards = []

    numbers_in_boards = {}
    # print(bingo[1:])
    for idx, line in enumerate(bingo[1:]):
        if idx % 5 == 0:
            boards.append([])
        nums = [int(x) for x in list(filter(lambda x: x != "", line.split(" ")))]
        boards[len(boards) - 1].append(nums)

        for i, number in enumerate(nums):
            if number in numbers_set:
                if number in numbers_in_boards:  # save the board number, row and col where this number appears
                    numbers_in_boards[number].append([len(boards) - 1, len(boards[len(boards) - 1]) - 1, i])
                else:
                    numbers_in_boards[number] = [[len(boards) - 1, len(boards[len(boards) - 1]) - 1, i]]

    board_scores = {
    }
    board_has_won = {i: False for i in range(len(boards))}
    no_of_boards_won = 0

    for board_no in range(len(boards)):
        board_scores[board_no] = {"row": {i: 0 for i in range(len(boards[board_no]))},
                                  "col": {i: 0 for i in range(len(boards[board_no]))}}
    for idx, number in enumerate(numbers):
        if number in numbers_in_boards:  # at least one of the boards has this number
            for board_stats in numbers_in_boards[number]:
                board_no = board_stats[0]
                row_no = board_stats[1]
                col_no = board_stats[2]
                board_scores[board_no]["row"][row_no] += 1
                board_scores[board_no]["col"][col_no] += 1
                if board_scores[board_no]["row"][row_no] == 5 or board_scores[board_no]["col"][col_no] == 5:
                    sum_unmarked = 0
                    numbers_picked = set(numbers[0:idx + 1])
                    for row in range(len(boards[board_no])):
                        for col in range(len(boards[board_no][row])):
                            if boards[board_no][row][col] not in numbers_picked:
                                sum_unmarked += boards[board_no][row][col]
                    if not board_has_won[board_no]:
                        board_has_won[board_no] = True
                        no_of_boards_won += 1
                    if no_of_boards_won == len(boards):
                        print(sum_unmarked * number)
                        return


inp = """input_here"""
sol(inp)
