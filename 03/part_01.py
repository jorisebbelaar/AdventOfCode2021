from util.input_reader import InputReader


def get_most_comon_bit_by_index(puzzle_input, index):
    zero = 0
    one = 0

    for input in puzzle_input:
        if input[index] == "0":
            zero += 1
        else:
            one += 1

    if zero > one:
        return "0"
    return "1"


def calculate_gamma(puzzle_input):
    gamma = ""
    for bit_index in range(12):
        gamma += get_most_comon_bit_by_index(puzzle_input, bit_index)
    return gamma


def calculate_epsilon(gamma):
    epsilon = ""
    for x in gamma:
        reverse = 1 - int(x)
        epsilon += str(reverse)
    return epsilon


if __name__ == '__main__':
    puzzle_input = InputReader.read_input("input.txt")
    gamma = calculate_gamma(puzzle_input)
    epsilon = calculate_epsilon(gamma)

    gamma_decimal = int(gamma, 2)
    epsilon_decimal = int(epsilon, 2)

    answer = gamma_decimal * epsilon_decimal
