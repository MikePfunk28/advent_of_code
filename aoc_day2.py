# -*- coding: utf-8 -*-
"""A program to analyze sequences of numbers for safety based on adjacent number differences.
This module reads sequences of numbers from a file and determines if they are 'safe' or 'unsafe'
based on whether the difference between adjacent numbers is within ±3 and the numbers are not equal.
Functions:
    read_file_lines(filename: str) -> list:
        Reads the input file and returns processed lines as integers.
    convert_to_int(lines: list) -> list:
        Converts each line from the input into a list of integers.
    convert_toint(line: str) -> tuple:
        Converts a single line into integers and checks for safety.
    is_line_safe(line_ints: list) -> tuple:
        Determines if a sequence of integers is safe based on adjacent differences.
        A sequence is safe if all adjacent numbers differ by no more than 3 and are not equal.
    print_results(results: str) -> None:
        Prints the final results of the safety analysis.
    main() -> tuple:
        Main entry point that processes the input file and returns safety statistics.
Global Variables:
    safe (int): Counter for safe sequences
    unsafe (int): Counter for unsafe sequences
File Dependencies:
    aoc_day2.txt: Input file containing sequences of numbers to analyze
Returns:
    tuple: Contains counts of safe and unsafe sequences (safe1, safe, unsafe1, unsafe)
"""
import logging
import numpy as np

logger = logging.getLogger("SequenceSafe")
logger.setLevel(logging.DEBUG)

logging.basicConfig(filename='aoc_day2.log', level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")
logging.debug("Debugging information: Starting the program.")
class SequenceSafe:
    """define safe, unsafe, and filename variables.
    """
    safe = 0
    unsafe = 0

    def __init__(self, filename):
        self.filename = filename
        self.read_file_lines(filename)
        self.safe = 0
        self.unsafe = 0

    # Read the file and convert to intSAFE = 0
    def read_file_lines(self, filename):
        """Reads the file and returns a list of lines."""
        logger.info("Reading file: %s", filename)
        with open(filename, mode="r", encoding="utf-8") as f:
            return self.convert_to_int(f.readlines())

    def convert_to_int(self, lines):
        """This is actually splitting up the lines into a list of lines,
        then just a list of one line, which gets converted to an int and passed."""
        logger.info("Converting lines to integers: %s", type(lines))
        for line in lines:
            
            return [self.convert_toint(line) for line in lines]
    

    def convert_toint(self, line):
        """Converts the line to an integer.  So the first one technically
        also splits them up, I don't know if it really converts as much as
        gets them ready to be converted."""
        line_ints = [int(x) for x in line.split()]
        logger.info("Converting to integers: %s", line_ints)
        # Check if the line is safe or unsafe
        return self.is_line_safe2(line_ints)

    def is_line_safe2(self, data):
        """Check if the int is with +/- 3, is the
        line safe or unsafe."""
        data = np.array(data)
        diff_list_safe = np.diff(data, axis=0).flatten()
        logging.debug("Difference list: %s", diff_list_safe)
        if np.all(diff_list_safe >= -3) and np.all(diff_list_safe < 0):
            self.safe += 1
            logging.debug("Safe: %s, Unsafe: %s", self.safe, self.unsafe)
            print(f"Safe: {self.safe}, Unsafe: {self.unsafe}")
            return (f"is safe: {self.safe} equals {len(data)} {self.safe} : {self.unsafe}", True)
        elif np.all(diff_list_safe > 0) and np.all(diff_list_safe <= 3):
            self.safe += 1
            logging.debug("Safe: %s, Unsafe: %s", self.safe, self.unsafe)
            print(f"Safe: {self.safe}, Unsafe: {self.unsafe}")
            return (f"is safe: {self.safe} equals {len(data)} {self.safe} : {self.unsafe}", True)

        else:
            self.unsafe += 1
            logging.debug("Safe: %s, Unsafe: %s", self.safe, self.unsafe)
            print(f"Safe: {self.safe}, Unsafe: {self.unsafe}")
            return (f"is unsafe: {self.unsafe}", False)

    def print_results(self, results):
        """Prints the results of the analysis."""
        logging.debug("Printing results: %s", results)
        print(results)
        return (self.safe, self.unsafe)

    def is_line_safe(self, line_ints: list):
        """Check if the int is with +/- 3, is the
        line safe or unsafe.

        i = index of the list of numbers
        unsafe = the result of the comparison
        safe = a safe result of the comparison
        
        The tricky part was determining if they
        continues decreasing or increasing.
        """
        i = 0
        psafe = 0
        unsafe = 0
        safe = 0
        line_diff = 0
        first_index = 0
        second_index = 0
        # for index in range 0 to 7 which will include 8 numbers.
        # using len(line_ints) if I subtract the 1 there it will be 7, not 8.
        logging.debug("Line integers: %s", line_ints)
        for i in range(len(line_ints) - 1):

            first_index = line_ints[i]
            second_index = line_ints[i + 1]
            line_diff = first_index - second_index
            logging.debug("First index: %s, Second index: %s, Difference: %s", first_index, second_index, line_diff)
            #print(len(line_ints))
            # Here need to be careful, because if the first number is 0 and the second is 3, it will be 3.
            # This is the same as abs(line_diff) <= 3 and first_index != second_index:\
            if abs(line_diff) <= 3 and first_index != second_index:
                # This if statement now just checks if it is done.
                #print(f" Index: {i})")
                #print(line_ints[i], line_ints[i + 1])
                if line_diff > 0:
                    # Here is where I needed it to be 8 normally but in this case I was 7 as there
                    # are only 7 pairs.
                    if psafe == len(line_ints) - 1:
                        self.safe += 1
                        #print(f"Safe: {self.safe}, Unsafe: {self.unsafe}")
                        i += 1
                        return (f"is safe: {psafe} equals {len(line_ints)} {self.safe} : {self.unsafe}", True)
                    elif (line_ints[i]-line_ints[i + 1]) <= 3 and line_ints[i] != line_ints[i + 1]:
                        psafe += 1
                        logging.debug("Safe: %s, Unsafe: %s", psafe, unsafe)
                        i += 1
                    else:
                        unsafe += 1
                        i += 1
                        return (f"is unsafe: {unsafe}", False)
                else:
                    if self.safe == int(len(line_ints) - 1):
                        self.safe += 1
                        #print(f"Safe: {self.safe}, Unsafe: {self.unsafe}")
                        i += 1
                        return (f"is safe: {self.safe} equals {len(line_ints)} {self.safe} : {self.unsafe}", True)
                    elif -3 <= (line_ints[i]-line_ints[i + 1]) and line_ints[i] != line_ints[i + 1]:
                        safe += 1
                        logging.debug("Safe: %s, Unsafe: %s", safe, unsafe)
                        i += 1
                    else:
                        unsafe += 1
                        i += 1
                        return (f"is unsafe: {unsafe}", False)

            else:
                self.unsafe += 1
                return (f"is unsafe: {self.unsafe}", False)
            logging.debug("Safe: %s, Unsafe: %s", self.safe, self.unsafe)
        return f"Safe: {self.safe}, Neg-Safe {self.safe}Unsafe: {self.unsafe}"


def main():
    """Main function to call the code, and make sure
    it only runs when directly called."""
    sequence = SequenceSafe("aoc_day2.txt")
    results = sequence.read_file_lines("aoc_day2.txt")
    print(sequence)
    print(sequence.print_results(results))
    safe: int = sequence.safe
    unsafe: int = sequence.unsafe
    print(f"Safe: {safe}, Unsafe: {unsafe}")
    return sequence.safe, sequence.unsafe, safe, unsafe


if __name__ == "__main__":
    main()
