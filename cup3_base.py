from search import Problem, Trial_Error


class Cup3(Problem):
    def __init__(self):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal. Your subclass's constructor can add
        other arguments."""

        super().__init__((5, 0, 0),[(4,1,0),(4,0,1)])
        self.h1=[0,1,2,3,4,5]
        self.h2=[0,1,2,3]
        self.h3=[0,1,2]
        self.H=[self.h1,self.h2,self.h3]

        



    def actions(self, state):
        """Return all the actions that can be executed in the given
        state"""
        acts = []
        cup1,cup2,cup3=state
        if cup1>0 and cup2<3:
            acts.append("o 1 2")
        elif cup1>0 and cup3<2:
            acts.append("o 1 3")
        elif cup3>0 and cup1<5:
            acts.append("o 3 1")
        elif cup2>0 and cup3<2:
            acts.append("o 2 3")
        elif cup2>0 and cup1<5:
            acts.append("o 2 1")
        elif cup3>0 and cup2<3:
            acts.append("o 3 2")
        
        return acts


        # for i in range(3):
        #     for j in range(3):
        #         if i!=j:
        #             if state[i] >0 and state[j]<self.cup
        #             acts.append()

    def actions2(self,state):
        acts=[]
        for i in range(1,4):
            for j in range(1,4):
                if i!=j:
                    if state[i-1]>0 and state[j-1]<max(self.H[j-1]):
                        acts.append("o {} {}".format(i,j))
        return acts

    def result1(self, state, action):
        """Return the state that results from executing the given
        action in the given state. Assume that the action is one of
        self.actions(state)."""
        cup1,cup2,cup3=state
       

        if action == "o 1 2":
            m=min(cup1,max(self.h2)-cup2)
            return (cup1-m,cup2+m,cup3)
        elif action == "o 1 3":
            m=min(cup1,max(self.h3)-cup3)
            return (cup1-m,cup2,cup3+m)
        elif action == "o 2 1":
            m=min(cup2,max(self.h1)-cup1)
            return (cup1+m,cup2-m,cup3)
        elif action == "o 2 3":
            m=min(cup2,max(self.h3)-cup3)
            return (cup1,cup2-m,cup3+m)
        elif action == "o 3 1":
            m=min(cup3,max(self.h1)-cup1)
            return (cup1+m,cup2,cup3-m)
        elif action == "o 3 2":
            m=min(cup3,max(self.h2)-cup2)
            return (cup1,cup2+m,cup3-m)

    def result(self, state, action):
        cups = list(state)  # convert tuple → list
        cup_from, cup_to = map(int, action.split()[1:])

        # convert to 0-based index
        i = cup_from - 1
        j = cup_to - 1

        capacity_j = max(self.H[j])

        # amount we can pour
        m = min(cups[i], capacity_j - cups[j])

        # update cups
        cups[i] -= m
        cups[j] += m

        return tuple(cups)



def main():
    c = Cup3()
    print(c.actions((5, 0, 0)))
    print(c.result((5, 0, 0), "o 1 2"))

    print(c.result1((5, 0, 0), "o 1 3"))
    print(c.result((5, 0, 0), "o 1 3"))
  

main()
