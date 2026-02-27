import math
from search import Problem


class Hanoi(Problem):
    def __init__(self):
        # super().__init__(write initial state here, [write goal states here])
        pass

    def actions(self, state):
        acts = []

        # Calculate possible actions here

        return acts

    def result(self, state, action):
        i, j, k = action.split(' ')[1:]

        # calculate and return new state here
        pass


def main():
    h = Hanoi()

    # Test if actions works correctly
    print(h.actions([{1, 2, 3}, set(), set()]))
    print(h.actions([{1}, {2, 3}, set()]))

    # Test if result works correctly
    print(h.result(
        state=[{1}, {2, 3}, set()],
        action="o 2 3 2"
    ))


main()
