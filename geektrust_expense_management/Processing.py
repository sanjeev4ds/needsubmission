class Process:
    def __init__(self):
        self.Dict_GivingMember_RecevingMember = {}
        self.final_output = []
    def EvaluateFinalRemainingAmounts(self):
        # it will be good to evaluate all the dues at time of each spend for all the active members
        for giving_member in self.Dict_GivingMember_RecevingMember:
            for receiving_member in self.Dict_GivingMember_RecevingMember[giving_member]:
                # if A->B is greater than or equals to B->A
                if (self.Dict_GivingMember_RecevingMember[giving_member][receiving_member] >=
                        self.Dict_GivingMember_RecevingMember[receiving_member][giving_member]):
                    self.Dict_GivingMember_RecevingMember[giving_member][receiving_member] -= \
                        self.Dict_GivingMember_RecevingMember[receiving_member][giving_member]
                    self.Dict_GivingMember_RecevingMember[receiving_member][giving_member] = 0
                # if A->B is less than to B->A
                else:
                    self.Dict_GivingMember_RecevingMember[receiving_member][giving_member] -= \
                        self.Dict_GivingMember_RecevingMember[giving_member][receiving_member]
                    self.Dict_GivingMember_RecevingMember[giving_member][receiving_member] = 0

                # again re-check if price is not pending anymore
                # if still price is there to submit for due member to member
                # then check third member price pending for receiving_member and all that amount it have to member side for third member
                list_members = list(self.Dict_GivingMember_RecevingMember.keys())
                # removing giving_member from list
                list_members = [ele for ele in list_members if ele != giving_member]
                # removing receiving_member from list
                list_members = [ele for ele in list_members if ele != receiving_member]

                # if an only if there is any third member in the contributions
                if (len(list_members) == 1):
                    member_uncovered = list_members[0]
                    # check the third member exist in due member with some amount
                    # if due member(B) holding any amount for member(A), then we can check if third member(C) also holding any amount for due member(B)
                    # if some amount exist from C->B then we can directly send C->A
                    if ((self.Dict_GivingMember_RecevingMember[giving_member][receiving_member] > 0)
                            and (self.Dict_GivingMember_RecevingMember[receiving_member][member_uncovered] > 0)):
                        # if C->B is less than equals to B->A
                        if (self.Dict_GivingMember_RecevingMember[receiving_member][member_uncovered]
                                <= self.Dict_GivingMember_RecevingMember[giving_member][receiving_member]):
                            # C->A increase
                            self.Dict_GivingMember_RecevingMember[giving_member][member_uncovered] += \
                                self.Dict_GivingMember_RecevingMember[receiving_member][member_uncovered]
                            # B->A decrease with same amount
                            self.Dict_GivingMember_RecevingMember[giving_member][receiving_member] -= \
                                self.Dict_GivingMember_RecevingMember[receiving_member][member_uncovered]
                            # as total amount have been transferred so we remain with 0 amount in B->C
                            self.Dict_GivingMember_RecevingMember[receiving_member][member_uncovered] = 0
                        # if C->B is greater than A->B
                        else:
                            # A->C increase with the amount it requires till A->B
                            self.Dict_GivingMember_RecevingMember[giving_member][member_uncovered] += self.Dict_GivingMember_RecevingMember[giving_member][receiving_member]
                            # C->B will decrease with same amount
                            self.Dict_GivingMember_RecevingMember[receiving_member][member_uncovered] -= self.Dict_GivingMember_RecevingMember[giving_member][receiving_member]
                            # as total amount was cleared for so it will remain 0 amount in A->B
                            self.Dict_GivingMember_RecevingMember[giving_member][receiving_member] = 0

    #this function will add keys in each member if not already exist
    def AddEveryNewMember(self):
        # adding all the members initial values if not exist in mapping
        for every_member in self.Dict_GivingMember_RecevingMember:
            list_other_members = [ele for ele in list(self.Dict_GivingMember_RecevingMember.keys()) if ele != every_member]
            for other_member in list_other_members:
                if (other_member not in self.Dict_GivingMember_RecevingMember[every_member]):
                    self.Dict_GivingMember_RecevingMember[every_member][other_member] = 0

    def MOVE_IN(self, input_line):
        # statement_type = "MOVE_IN"
        member_name = input_line.split(" ")[1].split("\n")[0]

        if(member_name not in self.Dict_GivingMember_RecevingMember):
            if (len(self.Dict_GivingMember_RecevingMember) < 3):
                self.Dict_GivingMember_RecevingMember[member_name] = {}
                # adding all the members initial values if not exist in mapping
                self.AddEveryNewMember()
                self.final_output.append("SUCCESS")
                #return True for SUCCESS case only
                return True
            elif (len(self.Dict_GivingMember_RecevingMember) == 3):
                self.final_output.append("HOUSEFUL")
        # return False for other cases
        return False

    def SPEND(self, input_line):
        split_line = input_line.split(" ")
        # second index is always amount
        amount = int(split_line[1])
        # third index is always giving member
        giving_member = split_line[2]
        # rest all further are taking members
        number_of_members = len(split_line[3:])
        check_members_exist = True
        # checking once each member whether exist in keys
        for index in range(number_of_members):
            # last index contains "\n"
            if (split_line[3 + index].__contains__("\n")):
                member_name = split_line[3 + index].split("\n")[0]
            else:
                member_name = split_line[3 + index]
            if (member_name not in self.Dict_GivingMember_RecevingMember):
                check_members_exist = False
                break
        if (check_members_exist):
            each_spends = amount // (number_of_members + 1)
            for index in range(number_of_members):
                # last index contains "\n"
                if (split_line[3 + index].__contains__("\n")):
                    member_name = split_line[3 + index].split("\n")[0]
                else:
                    member_name = split_line[3 + index]

                if (member_name in self.Dict_GivingMember_RecevingMember[giving_member]):
                    self.Dict_GivingMember_RecevingMember[giving_member][member_name] += each_spends
                else:
                    self.Dict_GivingMember_RecevingMember[giving_member][member_name] = each_spends
            self.final_output.append("SUCCESS")
            # it will be good to evaluate all the dues at time of each spend for all the active members
            self.EvaluateFinalRemainingAmounts()
            #returning True for SUCCESS
            return True
        else:
            self.final_output.append("MEMBER_NOT_FOUND")
            # returning False for MEMBER_NOT_FOUND
            return False
    def DUES(self, input_line):
        member_name = input_line.split(" ")[1].split("\n")[0]
        if (member_name in self.Dict_GivingMember_RecevingMember):
            set_amounts = set()
            dict_amount_givername = {}
            for member in self.Dict_GivingMember_RecevingMember:
                if member_name in self.Dict_GivingMember_RecevingMember[member]:
                    if (self.Dict_GivingMember_RecevingMember[member][member_name] not in dict_amount_givername):
                        dict_amount_givername[self.Dict_GivingMember_RecevingMember[member][member_name]] = [member]
                    else:
                        dict_amount_givername[self.Dict_GivingMember_RecevingMember[member][member_name]].append(member)
                    # sort the list
                    dict_amount_givername[self.Dict_GivingMember_RecevingMember[member][member_name]].sort()
                    set_amounts.add(self.Dict_GivingMember_RecevingMember[member][member_name])
                elif ((member_name != member) and (member_name not in self.Dict_GivingMember_RecevingMember[member])):
                    if (0 not in dict_amount_givername):
                        dict_amount_givername[0] = [member]
                    else:
                        dict_amount_givername[0].append(member)
                    set_amounts.add(0)
                    # sort the list
                    dict_amount_givername[0].sort()
            list_amounts = list(set_amounts)
            list_amounts.sort(reverse=True)
            for amount in list_amounts:
                for amount_member in dict_amount_givername[amount]:
                    String_AmountMember_Amount = amount_member + " " + str(amount)
                    self.final_output.append(String_AmountMember_Amount)
            #As member is there and have dues as well
            return True
        else:
            self.final_output.append("MEMBER_NOT_FOUND")
            # As member is not found
            return False

    def ClEAR_DUE(self, input_line):
        split_input_line = input_line.split(" ")
        # second index is giver
        giving_member = split_input_line[1]
        # third index is receiver
        receiving_member = split_input_line[2]
        # fourth index is amount
        amount = int(split_input_line[3].split("\n")[0])

        if (self.Dict_GivingMember_RecevingMember[receiving_member][giving_member] >= amount):
            self.Dict_GivingMember_RecevingMember[giving_member][receiving_member] += amount
            # it will be good to evaluate all the dues at time of each spend for all the active members
            self.EvaluateFinalRemainingAmounts()
            self.final_output.append(str(self.Dict_GivingMember_RecevingMember[receiving_member][giving_member]))
            return True
        else:
            self.final_output.append("INCORRECT_PAYMENT")
            return False

    def MOVE_OUT(self, input_line):
        input_line_split = input_line.split(" ")
        member_name = input_line_split[1].split("\n")[0]
        # second index contains member name
        if (member_name not in self.Dict_GivingMember_RecevingMember.keys()):
            self.final_output.append("MEMBER_NOT_FOUND")
        else:
            check_find_issue = False
            for member in self.Dict_GivingMember_RecevingMember:
                if (member == member_name):
                    for sub_member in self.Dict_GivingMember_RecevingMember[member]:
                        if (self.Dict_GivingMember_RecevingMember[member][sub_member] != 0):
                            check_find_issue = True
                            break

                    if (check_find_issue):
                        break
                else:
                    for sub_member in self.Dict_GivingMember_RecevingMember[member]:
                        if ((sub_member == member_name) and (self.Dict_GivingMember_RecevingMember[member][sub_member] != 0)):
                            check_find_issue = True
                            break
                    if (check_find_issue):
                        break
            if (check_find_issue == False):
                self.final_output.append("SUCCESS")
                return True
            else:
                self.final_output.append("FAILURE")
                return False