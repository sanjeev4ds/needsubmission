class CalculateAmounts:
    # re-calculating for third member also
    def connected_amount(self, giver, receiver, remain):
        try:
            if ((self.giver_receiver[giver][receiver] > 0) and (self.giver_receiver[receiver][remain] > 0)):
                if (self.giver_receiver[receiver][remain] <= self.giver_receiver[giver][receiver]):
                    self.giver_receiver[giver][remain] += self.giver_receiver[receiver][remain]
                    self.giver_receiver[giver][receiver] -= self.giver_receiver[receiver][remain]
                    self.giver_receiver[receiver][remain] = 0
                else:
                    self.giver_receiver[giver][remain] += self.giver_receiver[giver][receiver]
                    self.giver_receiver[receiver][remain] -= self.giver_receiver[giver][receiver]
                    self.giver_receiver[giver][receiver] = 0
            return True
        except:
            return False

    # calcualte the ramaining amounts for every member
    def evaluate_amounts(self):
        for giver in self.giver_receiver:
            for receiver in self.giver_receiver[giver]:
                if (self.giver_receiver[giver][receiver] >= self.giver_receiver[receiver][giver]):
                    self.giver_receiver[giver][receiver] -= self.giver_receiver[receiver][giver]
                    self.giver_receiver[receiver][giver] = 0
                else:
                    self.giver_receiver[receiver][giver] -= self.giver_receiver[giver][receiver]
                    self.giver_receiver[giver][receiver] = 0

                if (len(self.giver_receiver[giver]) > 1):
                    remain = [ele for ele in list(self.giver_receiver[giver].keys()) if ele != receiver][0]
                    self.connected_amount(giver, receiver, remain)

    #calculate all the dues pending for member
    def calculate_dues(self, member):
        set_amount = set()
        amount_giver = {}
        for giver in self.giver_receiver:
            if member in self.giver_receiver[giver]:
                if (self.giver_receiver[giver][member] not in amount_giver):
                    amount_giver[self.giver_receiver[giver][member]] = [giver]
                else:
                    amount_giver[self.giver_receiver[giver][member]].append(giver)

                amount_giver[self.giver_receiver[giver][member]].sort()
                set_amount.add(self.giver_receiver[giver][member])
            elif ((member != giver) and (member not in self.giver_receiver[giver])):
                if (0 not in amount_giver):
                    amount_giver[0] = [giver]
                else:
                    amount_giver[0].append(giver)
                set_amount.add(0)
                amount_giver[0].sort()
        list_amounts = list(set_amount)
        list_amounts.sort(reverse=True)
        return list_amounts, amount_giver