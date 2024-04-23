import sys
import os

# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)

# adding the parent directory to
# the sys.path.
sys.path.append(parent)

from src.service.InputDifferentiate import InputDifferentiate
from src.service.OutputPrint import OutputPrint
class Process(InputDifferentiate, OutputPrint):

    def __init__(self):
        self.final_output = []
        self.giver_receiver = {}
        super().__init__()
    def process_all_lines(self, lines):
        # iterating for each line and processing the input commands of the input file
        for line in lines:
            line = line.split("\n")[0]
            output = super().process_line(line)

            if (isinstance(output, str)):
                self.final_output.append(output)
            else:
                # loop till each element in output
                for ele in output:
                    self.final_output.append(ele)

        # print all lines
        super().print_lines(self.final_output)