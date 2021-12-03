class InputReader():
    @staticmethod
    def read_input(filepath):
        input_list = []

        file = open(filepath, "r")
        lines = file.readlines()

        for line in lines:
            input_list.append(line.replace("\n", ""))

        return input_list
