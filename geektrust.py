from sys import argv
#
# def CheckStatementType(input_line):
#     if(input_line.__contains__("MOVE_IN")):
#         statement_type = "MOVE_IN"
#     elif(input_line.__contains__("SPEND")):
#         statement_type = "SPEND"
#     elif (input_line.__contains__("DUES")):
#         statement_type = "DUES"
#     elif (input_line.__contains__("CLEAR_DUE")):
#         statement_type = "CLEAR_DUE"
#     elif (input_line.__contains__("MOVE_OUT")):
#         statement_type = "MOVE_OUT"
#
#     return statement_type

# def MOVE_IN
final_dict = {}

def EvaluateFinalRemainingAmounts():
    #it will be good to evaluate all the dues at time of each spend for all the active members
    for member in final_dict:
        for due_member in final_dict[member]:
            #if A->B is greater than or equals to B->A
            if(final_dict[member][due_member] >= final_dict[due_member][member]):
                final_dict[member][due_member] -= final_dict[due_member][member]
                final_dict[due_member][member] = 0
            #if A->B is less than to B->A
            else:
                final_dict[due_member][member] -= final_dict[member][due_member]
                final_dict[member][due_member] = 0

            #again re-check if price is not pending anymore
            #if still price is there to submit for due member to member
            #then check third member price pending for due_member and all that amount it have to member side for third member
            list_members = list(final_dict.keys())
            list_members = [ele for ele in list_members if ele != member]
            list_members = [ele for ele in list_members if ele != due_member]
            # if an only if there is any third member in the contributions
            if (len(list_members)==1):
                member_uncovered = list_members[0]
                #check the third member exist in due member with some amount
                #if due member(B) holding any amount for member(A), then we can check if third member(C) also holding any amount for due member(B)
                #if some amount exist from C->B then we can directly send C->A
                if( (final_dict[member][due_member] > 0) and (final_dict[due_member][member_uncovered]>0) ):
                    #if C->B is less than equals to B->A
                    if(final_dict[due_member][member_uncovered]<= final_dict[member][due_member]):
                        #C->A increase
                        final_dict[member][member_uncovered] += final_dict[due_member][member_uncovered]
                        #B->A decrease with same amount
                        final_dict[member][due_member] -= final_dict[due_member][member_uncovered]
                        #as total amount have been transferred so we remain with 0 amount in B->C
                        final_dict[due_member][member_uncovered] = 0
                    #if C->B is greater than A->B
                    else:
                        #A->C increase with the amount it requires till A->B
                        final_dict[member][member_uncovered] += final_dict[member][due_member]
                        #C->B will decrease with same amount
                        final_dict[due_member][member_uncovered] -= final_dict[member][due_member]
                        #as total amount was cleared for so it will remain 0 amount in A->B
                        final_dict[member][due_member] = 0

def main():
    
    """
    Sample code to read inputs from the file

    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
    //Add your code here to process the input commands
    """
    #declaring dict to store the members and respective expensive

    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
    # path_input_file = "input2.txt"
    # with open('sample_input/' + path_input_file) as f:
    #     # contents = f.read()
    #     Lines = f.readlines()
    #     # print(Lines)

    for input_line in Lines:

        # MOVE IN SECTION
        if (input_line.__contains__("MOVE_IN")):
            #statement_type = "MOVE_IN"
            member_name = input_line.split(" ")[1].split("\n")[0]

            if( (len(final_dict) <3 ) and (member_name not in final_dict) ):
                #print("adding new member in list")
                final_dict[member_name] = {}
                print("SUCCESS")
            elif ((len(final_dict) == 3) and (member_name not in final_dict)):
                #print("already exist")
                print("HOUSEFUL")

            #adding all the members initial values if not exist in mapping
            for every_member in final_dict:
                list_other_members = [ele for ele in list(final_dict.keys()) if ele!= every_member]
                for other_member in list_other_members:
                    if(other_member not in final_dict[every_member]):
                        final_dict[every_member][other_member] = 0

        # SPEND SECTION
        elif (input_line.__contains__("SPEND")):
            # statement_type = "SPEND"
            split_line = input_line.split(" ")
            #second index is always amount
            amount = int(split_line[1])
            #third index is always giving member
            giving_member = split_line[2]
            #rest all further are taking members
            number_of_members = len(split_line[3:])
            check_members_exist = True
            #checking once each member whether exist in keys
            for index in range(number_of_members):
                # last index contains "\n"
                if (split_line[3 + index].__contains__("\n")):
                    member_name = split_line[3 + index].split("\n")[0]
                else:
                    member_name = split_line[3 + index]
                if(member_name not in final_dict):
                    check_members_exist = False
                    break
            if(check_members_exist):
                each_spends = amount//(number_of_members+1)
                for index in range(number_of_members):
                    #last index contains "\n"
                    if(split_line[3+index].__contains__("\n")):
                        member_name = split_line[3+index].split("\n")[0]
                    else:
                        member_name = split_line[3+index]

                    if(member_name in final_dict[giving_member]):
                        final_dict[giving_member][member_name] += each_spends
                    else:
                        final_dict[giving_member][member_name] = each_spends
                print("SUCCESS")
            else:
                print("MEMBER_NOT_FOUND")

            #print("check one time dictionary before", final_dict)
            # it will be good to evaluate all the dues at time of each spend for all the active members
            EvaluateFinalRemainingAmounts()
            #print("check one time dictionary after", final_dict)

        # DUES SECTION
        elif (input_line.__contains__("DUES")):
            # statement_type = "DUES"
            # print('statement_type = "DUES"')
            member_name = input_line.split(" ")[1].split("\n")[0]
            if (member_name in final_dict):
                set_amounts = set()
                dict_amount_givername= {}
                for member in final_dict:
                    if member_name in final_dict[member]:
                        if(final_dict[member][member_name] not in dict_amount_givername):
                            dict_amount_givername[final_dict[member][member_name]] = [member]
                        else:
                            dict_amount_givername[final_dict[member][member_name]].append(member)
                        #sort the list
                        dict_amount_givername[final_dict[member][member_name]].sort()
                        set_amounts.add(final_dict[member][member_name])
                    elif((member_name!= member) and (member_name not in final_dict[member])):
                        if(0 not in dict_amount_givername):
                            dict_amount_givername[0] = [member]
                        else:
                            dict_amount_givername[0].append(member)
                        set_amounts.add(0)
                        # sort the list
                        dict_amount_givername[0].sort()
                list_amounts = list(set_amounts)
                list_amounts.sort(reverse= True)
                for amount in list_amounts:
                    # print(amount)
                    for amount_member in dict_amount_givername[amount]:
                        print(amount_member, amount)
            else:
                print("MEMBER_NOT_FOUND")

        # CLEAR DUE SECTION
        elif (input_line.__contains__("CLEAR_DUE")):
            # statement_type = "CLEAR_DUE"
            split_input_line = input_line.split(" ")
            #second index is giver now
            giving_member = split_input_line[1]
            #third index is receiver now
            receiving_member = split_input_line[2]
            #fourth index is amount
            amount = int(split_input_line[3].split("\n")[0])

            if(final_dict[receiving_member][giving_member] >= amount):
                final_dict[giving_member][receiving_member] += amount
            else:
                print("INCORRECT_PAYMENT")
                continue
            # print("before final_dict", final_dict)
            # it will be good to evaluate all the dues at time of each spend for all the active members
            EvaluateFinalRemainingAmounts()
            # print("after final_dict", final_dict)
            print(final_dict[receiving_member][giving_member])
            # break

        # MOVE OUT SECTION
        elif (input_line.__contains__("MOVE_OUT")):
            # statement_type = "MOVE_OUT"
            input_line_split = input_line.split(" ")
            member_name = input_line_split[1].split("\n")[0]
            #second index contains member name
            if(member_name not in final_dict.keys()):
                print("MEMBER_NOT_FOUND")
            else:
                check_find_issue = False
                for member in final_dict:
                    if(member == member_name):
                        for sub_member in final_dict[member]:
                            if(final_dict[member][sub_member] != 0):
                                check_find_issue = True
                                break

                        if(check_find_issue):
                            break
                    else:
                        for sub_member in final_dict[member]:
                            if( (sub_member==member_name) and (final_dict[member][sub_member] != 0) ):
                                check_find_issue = True
                                break
                        if (check_find_issue):
                            break
                if(check_find_issue==False):
                    print("SUCCESS")
                else:
                    print("FAILURE")
        # print(statement_type)
        # print(final_dict)
if __name__ == "__main__":
    main()
