from sys import argv
from src.business_logic.ProcessCommands import Process
def main():
    
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()

    object_process = Process()
    # send all lines to get processed
    object_process.process_all_lines(lines)

if __name__ == "__main__":
    main()