"""
Stack implementation

"""
from enum import Enum, auto


class TypeOptions(Enum):
    OPEN = auto()
    CLOSE = auto()


class Classifier:
    @staticmethod
    def classify(element):
        current_options = {
            "{": ("r_brackets", TypeOptions.OPEN),
            "[": ("s_brackets", TypeOptions.OPEN),
            "(": ("parenthesis", TypeOptions.OPEN),
            "}": ("r_brackets", TypeOptions.CLOSE),
            "]": ("s_brackets", TypeOptions.CLOSE),
            ")": ("parenthesis", TypeOptions.CLOSE)
        }
        return Element(*current_options.get(element))


class Element:
    def __init__(self, name, type):
        self.type = type
        self.name = name


def orchestrator(test_case):
    stack = []
    classifier = Classifier()
    for element in test_case:
        element = classifier.classify(element)
        if element.type == TypeOptions.OPEN:
            stack.append(element)
        if element.type == TypeOptions.CLOSE:
            last_element = stack.pop()
            if last_element.name != element.name:
                return False
    if len(stack) != 0:
        return False
    return True


if __name__ == "__main__":
    test_cases = {
        "(){}[]": True,
        "{()}": True,
        "{(": False,
        "{(})": False
    }

    for k, v in test_cases.items():
        if orchestrator(k) != v:
            raise Exception("Error")
