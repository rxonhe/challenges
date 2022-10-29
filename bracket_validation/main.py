class Element:
    def __init__(self, color, tipo):
        self.color = color
        self.tipo = tipo


class Classifier:
    ...


class StackController:
    ...


class StackValidator:
    ...


def orchestrator(test_case):
    classifier = Classifier()
    stack_controller = StackController()
    stack_validator = StackValidator()
    stack = []
    is_valid = True
    for e in test_case:
        element = classifier.classify(e)
        stack_controller.add(element, stack)
        is_valid = stack_validator.check(stack)
        if not is_valid:
            break
    if is_valid:
        is_valid = stack_validator.check(stack)
    return is_valid


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
