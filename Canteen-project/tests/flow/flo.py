from ast import arg
import builtins
from canteen_project.canteen_pos import CanteenSystem


class Flo:

    PROMPTS = (
        "Enter category Hot food (H), Snacks (S), Drinks (d), Quit (Q): ",
        "Enter your item: ",
        "Enter quantity: ",
        "Choose another item (C), Check out (O), back to categories (G) , Quit (Q): ",
        "Payment method: Credit (R), Cash (S): ",
        "Cash amount : "
    )

    def __init__(self, path):
        self.path = path

        self.old_print = print
        self.old_input = input
        builtins.print = self._mock_print
        builtins.input = self._mock_input
        self.prints = ""

        self.responses = []  # [h]
        self.rolls = []

        with open(self.path) as file:
            for line in file.readlines():

                # gather prompt responses
                for prompt in self.PROMPTS:
                    if line.startswith(prompt):
                        response = line.split(prompt)[1].strip()
                        self.responses.append(response)

    @staticmethod
    def test(path):

        flo = Flo(path)
        canteen_sys = CanteenSystem()
        canteen_sys.order()

        flo._exit()

    def _mock_roller(self, num):
        return self.rolls.pop(0)

    def _mock_print(self, *args, **kwargs):
        self.prints += str(args) + "\n"

    def _mock_input(self, *args, **kwargs):

        self.prints += str(*args)

        response = self.responses.pop(0)

        self.prints += response + "\n"

        return response

    def _exit(self):

        with open(self.path) as file:

            print_lines = self.prints.strip().split("\n")

            file_lines = file.read().strip().split("\n")

            pairs = zip(print_lines, file_lines)

            for i, pair in enumerate(pairs):

                actual, expected = pair

                assert (
                    actual == expected
                ), f"line {i + 1} - actual:{actual} - expected:{expected}"

        builtins.print = self.old_print
        builtins.input = self.old_input
