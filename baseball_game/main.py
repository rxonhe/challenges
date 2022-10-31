class Score:
    def __init__(self):
        self.value = 0
        self.history = []


def plus_rule(element, current_score):
    to_add = current_score.history[-1] + current_score.history[-2]
    current_score.value += to_add
    current_score.history.append(to_add)
    return current_score


def double_rule(element, current_score):
    to_add = current_score.history[-1] * 2
    current_score.value += to_add
    current_score.history.append(to_add)
    return current_score


def cancel_rule(element, current_score):
    previous = current_score.history[-1]
    current_score.value += - previous
    current_score.history = current_score.history[:-1]


def integer_rule(element, current_score):
    element = int(element)
    current_score.value += element
    current_score.history.append(element)
    return current_score


def calc_by_rule(element, current_score):
    score_calc_options = {
        "+": plus_rule,
        "D": double_rule,
        "C": cancel_rule
    }
    return score_calc_options.get(element, integer_rule)(element, current_score)


if __name__ == "__main__":
    ops = [5, 2, "C", "D"]
    current_score = Score()
    for element in ops:
        current_score = calc_by_rule(element, current_score)
