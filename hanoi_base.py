import math
from search import Problem


class Hanoi(Problem):
    def __init__(self):
        super().__init__((1,2,3), [(3,2,1),(3,2,1)])
        pass

    def actions(self, state):
        acts = []

        
        inf_set={math.inf}
        for i in range(3):
            for j in range(3):
                if i != j:
                    for k in range(1,4):
                        if k== min(state[i].union(inf_set)) and k<min(state[j].union(inf_set)):
                            acts.append("o {} {}".format(i+1,j+1,k))

        

        return acts

    def result(self, state, action):
        i, j, k = action.split(' ')[1:]
        i,j,k = int(i),int(j),int(k)
        new_state=state

        for l in range(1,4):
            if l == j:
                new_state[l-1]=state[l-1].union({k})
            else:
                new_state[l-1]=state[l-1].difference({k})


        return new_state



        # calculate and return new state here
        
        

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
