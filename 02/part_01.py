from util.input_reader import InputReader


def parse_puzzle_input(puzzle_input):
    parsed_input = []
    for input in puzzle_input:
        split_input = input.split()
        parsed = {
            "direction": split_input[0],
            "steps": split_input[1]
        }
        parsed_input.append(parsed)
    return parsed_input


def calculate_position(parsed_input):
    horizontal = 0
    depth = 0
    for input in parsed_input:
        if input["direction"] == "forward":
            horizontal += int(input["steps"])
        elif input["direction"] == "down":
            depth += int(input["steps"])
        elif input["direction"] == "up":
            depth -= int(input["steps"])
    return horizontal, depth


if __name__ == '__main__':
    puzzle_input = InputReader.read_input("input.txt")
    parsed_puzzle_input = parse_puzzle_input(puzzle_input)
    position = calculate_position(parsed_puzzle_input)

    answer = position[0] * position[1]
    print(answer)
