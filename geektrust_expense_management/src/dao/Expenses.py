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

from src.service.calculate_amounts import CalculateAmounts
from src.service.member_operations import MemberOperations
class Expenses(CalculateAmounts, MemberOperations):
    # # re-calculating for third member also
    # def connected_amount(self, giver, receiver, remain):
    #     try:
    #         if ((self.giver_receiver[giver][receiver] > 0) and (self.giver_receiver[receiver][remain] > 0)):
    #             if (self.giver_receiver[receiver][remain] <= self.giver_receiver[giver][receiver]):
    #                 self.giver_receiver[giver][remain] += self.giver_receiver[receiver][remain]
    #                 self.giver_receiver[giver][receiver] -= self.giver_receiver[receiver][remain]
    #                 self.giver_receiver[receiver][remain] = 0
    #             else:
    #                 self.giver_receiver[giver][remain] += self.giver_receiver[giver][receiver]
    #                 self.giver_receiver[receiver][remain] -= self.giver_receiver[giver][receiver]
    #                 self.giver_receiver[giver][receiver] = 0
    #         return True
    #     except:
    #         return False
    # def evaluate_amounts(self):
    #     '''
    #     calcualte the ramaining amounts for every member
    #     :return: update the giver_receiver object
    #     '''
    #     for giver in self.giver_receiver:
    #         for receiver in self.giver_receiver[giver]:
    #             if (self.giver_receiver[giver][receiver] >= self.giver_receiver[receiver][giver]):
    #                 self.giver_receiver[giver][receiver] -= self.giver_receiver[receiver][giver]
    #                 self.giver_receiver[receiver][giver] = 0
    #             else:
    #                 self.giver_receiver[receiver][giver] -= self.giver_receiver[giver][receiver]
    #                 self.giver_receiver[giver][receiver] = 0
    #
    #             if(len(self.giver_receiver[giver])>1):
    #                 remain = [ele for ele in list(self.giver_receiver[giver].keys()) if ele != receiver][0]
    #                 self.connected_amount(giver, receiver, remain)

    # #this function will add keys in each member if not already exist
    # def add_every_newmember(self):
    #     for giver in self.giver_receiver:
    #         list_receivers = [ele for ele in list(self.giver_receiver.keys()) if ele != giver]
    #         for receiver in list_receivers:
    #             if (receiver not in self.giver_receiver[giver]):
    #                 self.giver_receiver[giver][receiver] = 0
    #     return True

    def move_in(self, input_line):
        member_name = input_line.split(" ")[1]
        if (len(self.giver_receiver) == 3):
            return "HOUSEFUL"
        elif( (len(self.giver_receiver) < 3) and (member_name not in self.giver_receiver)):
            self.giver_receiver[member_name] = {}
            super().add_new_member()
            return "SUCCESS"
        return "HOUSEFUL"
    def spend(self, input_line):
        words = input_line.split(" ")
        amount = int(words[1])
        giver = words[2]
        members_count = len(words[3:])

        check_members_exist = True
        for index in range(members_count):
            member_name = words[3 + index]
            if (member_name not in self.giver_receiver):
                check_members_exist = False
                break

        if (check_members_exist):
            each_spends = amount // (members_count + 1)
            for index in range(members_count):
                member_name = words[3 + index]

                if (member_name in self.giver_receiver[giver]):
                    self.giver_receiver[giver][member_name] += each_spends
                else:
                    self.giver_receiver[giver][member_name] = each_spends
            # it will be good to evaluate all the dues at time of each spend for all the active members
            super().evaluate_amounts()
            return "SUCCESS"
        else:
            return "MEMBER_NOT_FOUND"

    # #calculate all the dues pending for member
    # def calculate_dues(self, member):
    #     set_amount = set()
    #     amount_giver = {}
    #     for giver in self.giver_receiver:
    #         if member in self.giver_receiver[giver]:
    #             if (self.giver_receiver[giver][member] not in amount_giver):
    #                 amount_giver[self.giver_receiver[giver][member]] = [giver]
    #             else:
    #                 amount_giver[self.giver_receiver[giver][member]].append(giver)
    #
    #             amount_giver[self.giver_receiver[giver][member]].sort()
    #             set_amount.add(self.giver_receiver[giver][member])
    #         elif ((member != giver) and (member not in self.giver_receiver[giver])):
    #             if (0 not in amount_giver):
    #                 amount_giver[0] = [giver]
    #             else:
    #                 amount_giver[0].append(giver)
    #             set_amount.add(0)
    #             amount_giver[0].sort()
    #     list_amounts = list(set_amount)
    #     list_amounts.sort(reverse=True)
    #     return list_amounts, amount_giver
    def dues(self, input_line):
        person_amount = []
        member = input_line.split(" ")[1]
        if (member in self.giver_receiver):
            list_amounts, amount_giver = super().calculate_dues(member)
            for amount in list_amounts:
                for amount_member in amount_giver[amount]:
                    string_member_amount = amount_member + " " + str(amount)
                    person_amount.append(string_member_amount)
            return person_amount
        else:
            return "MEMBER_NOT_FOUND"

    def clear_due(self, input_line):
        split_input_line = input_line.split(" ")
        giver = split_input_line[1]
        if(giver not in self.giver_receiver):
            return "MEMBER_NOT_FOUND"
        receiver = split_input_line[2]
        if (receiver not in self.giver_receiver):
            return "MEMBER_NOT_FOUND"
        amount = int(split_input_line[3])
        if (self.giver_receiver[receiver][giver] >= amount):
            self.giver_receiver[giver][receiver] += amount
            # it will be good to evaluate all the dues at time of each spend for all the active members
            super().evaluate_amounts()
            return str(self.giver_receiver[receiver][giver])
        else:
            return "INCORRECT_PAYMENT"
    def remaining_dues(self, member_name):
        check_find_issue = False
        for member in self.giver_receiver:
            if (member == member_name):
                for receiver in self.giver_receiver[member]:
                    if (self.giver_receiver[member][receiver] != 0):
                        check_find_issue = True
                        break
                if (check_find_issue):
                    break
            else:
                for receiver in self.giver_receiver[member]:
                    if ((receiver == member_name) and (self.giver_receiver[member][receiver] != 0)):
                        check_find_issue = True
                        break
                if (check_find_issue):
                    break
        return check_find_issue

    # # remove the member from final dict
    # def remove_member(self, member):
    #     try:
    #         if member in self.giver_receiver:
    #             del self.giver_receiver[member]
    #
    #         for giver in self.giver_receiver:
    #             if(member in self.giver_receiver[giver]):
    #                 del self.giver_receiver[giver][member]
    #         return True
    #     except:
    #         return False

    def move_out(self, input_line):
        input_line_split = input_line.split(" ")
        member_name = input_line_split[1]

        if (member_name not in self.giver_receiver.keys()):
            return "MEMBER_NOT_FOUND"
        else:
            check_find_issue = super().calculate_dues(member_name)
            if (check_find_issue == False):
                # remove the member from final dict
                super().remove_member(member_name)
                return "SUCCESS"
            else:
                return "FAILURE"