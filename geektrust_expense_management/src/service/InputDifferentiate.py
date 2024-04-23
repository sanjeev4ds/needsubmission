from src.dao.Expenses import Expenses

class InputDifferentiate(Expenses):
    def __init__(self):
        super().__init__()

    def process_line(self, line):
        # MOVE_IN section
        if (line.__contains__("MOVE_IN")):
            output = super().move_in(line)
        # SPEND section
        elif (line.__contains__("SPEND")):
            output = super().spend(line)
        # DUES section
        elif (line.__contains__("DUES")):
            output = super().dues(line)
        # ClEAR_DUE section
        elif (line.__contains__("CLEAR_DUE")):
            output = super().clear_due(line)
        # MOVE_OUT section
        elif (line.__contains__("MOVE_OUT")):
            output = super().move_out(line)

        return output