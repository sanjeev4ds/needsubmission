from sys import argv
from Processing import Process
def main():
    
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()

    # initializing the object for class Process, this will initialize the final_dict
    object_process = Process()
    # iterating for each line and processing the input commands of the input file
    for input_line in Lines:
        # print("line- ", input_line)
        # MOVE_IN section
        if( input_line.__contains__("MOVE_IN") ):
            # calling the function with same object name object_process to MOVE_IN function of the class Process
            object_process.MOVE_IN(input_line)
        # SPEND section
        elif( input_line.__contains__("SPEND") ):
            # calling the function with same object name object_process to MOVE_IN function of the class Process
            object_process.SPEND(input_line)
        # DUES section
        elif( input_line.__contains__("DUES") ):
            # calling the function with same object name object_process to MOVE_IN function of the class Process
            object_process.DUES(input_line)
        # ClEAR_DUE section
        elif( input_line.__contains__("CLEAR_DUE") ):
            # print("clear due entered")
            # calling the function with same object name object_process to MOVE_IN function of the class Process
            object_process.ClEAR_DUE(input_line)
        # MOVE_OUT section
        elif( input_line.__contains__("MOVE_OUT") ):
            # calling the function with same object name object_process to MOVE_IN function of the class Process
            object_process.MOVE_OUT(input_line)
    # iterating for each line of final_output
    for line in object_process.final_output:
        print(line)

if __name__ == "__main__":
    main()