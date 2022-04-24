import builtins
from canteen_project.canteen_pos import CanteenSystem
import re
from canteen_project.helper_methods import HelperMethods as hm


class Flo:

    PROMPTS = (
        "Student(T),  Not a student(N): ",
        "Enter category Hot food (H), Snacks (S), Drinks (D), Quit (Q): ",
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

        self.responses = []

        with open(self.path) as file:
            for line in file.readlines():
                for prompt in self.PROMPTS:
                    if line.startswith(prompt):
                        response = line.split(prompt)[1].strip()
                        self.responses.append(response)

    def escape_ansi(self, line):
        pattern = r"((\\\\|\\[x][1][b])(\[[0-9]+[a-z]))"
        return re.sub(pattern, '', line)

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

    def _decolorize_text(self, lines):
        self.old_print(lines, '\n\n')
        for i, item in enumerate(lines):
            if item.startswith('(\''):
                table_cha = re.compile(r"(\(')|(',\))")
                new_text = table_cha.sub('', item)
                uncolorized_text = self.escape_ansi(new_text)
                n = self._separate_text(uncolorized_text)
                n = [i for i in n if i != '']
                lines[i] = n
                self.old_print(lines)
                return n

    def _separate_text(self, text):
        return text.split("\\n")

    def _exit(self):

        with open(self.path) as file:

            print_lines = self.prints.strip().split("\n")

            # self._decolorize_text(print_lines)

            file_lines = file.read().strip().split("\n")

            pairs = zip(print_lines, file_lines)

            for i, pair in enumerate(pairs):
                actual, expected = pair

                assert (
                    actual == expected
                ), f"line {i + 1} - actual:{actual} - expected:{expected}"

        builtins.print = self.old_print
        builtins.input = self.old_input


if __name__ == "__main__":
    Flo.test("/Users/noureddeinal-abassi/Desktop/401-ASAC/mid-term-project/Canteen-Management-System/Canteen-project/tests/flow/cash.sim.txt")
