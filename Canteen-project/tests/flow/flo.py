import builtins
from canteen_project.canteen_pos import CanteenSystem
import re


class Flo:

    PROMPTS = (
        "Student(T),  Not a student(N): ",
        "Enter category Hot food (H), Snacks (S), Drinks (D), Quit (Q): ",
        "Enter your item: ",
        "Enter quantity: ",
        "Choose another item (C), Check out (O), back to categories (G) , Quit (Q): ",
        "Payment method: Credit (R), Cash (S): ",
        "Cash amount : ",
        "Do you want to Delete (D) or Quit (Q)?: ",
        "Enter the name of the item to delete: ",
        "You have 1 items of Curry with a zip, how many item/s you want to delete: ",
        "Do you want to delete another item Y/N?: ",
        "You have 1 items of Vindaloo, how many item/s you want to delete: ",
    )

    def __init__(self, path):
        self.path = path

        self.old_print = print
        self.old_input = input
        builtins.print = self._mock_print
        builtins.input = self._mock_input
        self.prints = ""

        self.responses = []

        with open(self.path) as file:
            for line in file.readlines():
                for prompt in self.PROMPTS:
                    if line.startswith(prompt):
                        response = line.split(prompt)[1].strip()
                        self.responses.append(response)

    @staticmethod
    def test(path):

        flo = Flo(path)
        canteen_sys = CanteenSystem()
        canteen_sys.logic()

        flo._exit()

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

            for i, line in enumerate(print_lines):
                line = re.sub(
                    r'\\x1b(\[.*?[@-~]|\].*?(\x07|\x1b\\))', '', line)
                print_lines[i] = re.sub(r"(\(')|(',\))", '', line)

            pairs = zip(print_lines, file_lines)

            for i, pair in enumerate(pairs):
                actual, expected = pair
                assert (
                    actual == expected
                ), f"line {i + 1} - actual:{actual} - expected:{expected}"

        builtins.print = self.old_print
        builtins.input = self.old_input
