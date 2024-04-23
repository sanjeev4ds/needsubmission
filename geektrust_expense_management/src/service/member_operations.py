class MemberOperations:

    def add_new_member(self):
        for giver in self.giver_receiver:
            list_receivers = [ele for ele in list(self.giver_receiver.keys()) if ele != giver]
            for receiver in list_receivers:
                if (receiver not in self.giver_receiver[giver]):
                    self.giver_receiver[giver][receiver] = 0
        return True

    # remove the member from final dict
    def remove_member(self, member):
        try:
            if member in self.giver_receiver:
                del self.giver_receiver[member]

            for giver in self.giver_receiver:
                if(member in self.giver_receiver[giver]):
                    del self.giver_receiver[giver][member]
            return True
        except:
            return False