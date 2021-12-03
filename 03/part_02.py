from util.input_reader import InputReader


def get_most_comon_bit_by_index(puzzle_input, index):
    zero = 0
    one = 0

    for input in puzzle_input:
        if input[index] == "0":
            zero += 1
        else:
            one += 1

    if one >= zero:
        return "1"
    return "0"


def get_least_comon_bit_by_index(puzzle_input, index):
    zero = 0
    one = 0

    for input in puzzle_input:
        if input[index] == "0":
            zero += 1
        else:
            one += 1

    if zero <= one:
        return "0"
    return "1"


def filter_by_most_common_bit_by_index(puzzle_input, most_common_bit, index):
    result_list = []
    for input in puzzle_input:
        if input[index] == most_common_bit:
            result_list.append(input)
    return result_list


def calculate_oxygen_generator_rating(puzzle_input):
    for bit_index in range(12):
        most_common_bit = get_most_comon_bit_by_index(puzzle_input, bit_index)
        puzzle_input = filter_by_most_common_bit_by_index(puzzle_input, most_common_bit, bit_index)
        if len(puzzle_input) == 1:
            break

    return puzzle_input


def calculate_co2_scrubber_rating(puzzle_input):
    for bit_index in range(12):
        least_common_bit = get_least_comon_bit_by_index(puzzle_input, bit_index)
        puzzle_input = filter_by_most_common_bit_by_index(puzzle_input, least_common_bit, bit_index)
        if len(puzzle_input) == 1:
            break
    return puzzle_input


if __name__ == '__main__':
    puzzle_input = InputReader.read_input("input.txt")
    oxygen_genrator_rating = int(calculate_oxygen_generator_rating(puzzle_input)[0], 2)
    co2_scrubber_rating = int(calculate_co2_scrubber_rating(puzzle_input)[0], 2)

    answer = oxygen_genrator_rating * co2_scrubber_rating
