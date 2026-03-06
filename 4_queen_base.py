from search import Problem, Trial_Error

def convert_to_list(state):
    return [list(x) for x in state]

def convert_to_tuple(state):
    return tuple(tuple(x) for x in state)


def print_matrix(matrix):
    for row in matrix:
        print(row)

class FourQueensProblem(Problem):
    def __init__(self):
        # Fill out the __init__ call with only the initial state of the problem (in tuple of tuples format)
        super().__init__(((0,0,0,0)
                        (0,0,0,0)
                        (0,0,0,0)
                        (0,0,0,0)))


    def actions(self, state):
        # Return a list of possible actions in "o i j" format where
        # i is the row (from 1 to 4) and j is the column (from 1 to 4)
        acts=[]
        for i in range(4):
            for j in range(4):
                if state[i][j]==0:
                    acts.append("o {} {}".formate(i+1,j+1))

        return acts


    def result(self, state, action):
        # Return with the new state of the result of the action parameter used in the state parameter.
        # Tip: don't forget to convert state to list of lists and then convert the result back to tuple of tuples
        i,j=action.split(' ')[1:]
        i,j=int(i),int(j)
        new_state=convert_to_list(state)
        
        for l in range(4):
            for k in range(4):
                if l==i and k==j :
                    new_state[l][k]=1
                elif l==i or k==j or l+k==i+j or l-k==i-j:
                    new_state[l][k]=1
                else:
                    new_state[l][k]=0

        return convert_to_tuple(new_state)

    def goal_test(self,state):
        # For a given state parameter check if it is a goal state.
        # Tip 1: don't forget conversions; Tip 2: you can use any() or all() for easier implementation
        
        bool_state = convert_to_list(state)
        for i in range(4):
            for j in range(4):
                 bool_state[i][j]=state[i][j]==1

        return  all([any(bool_state[i]) for i in range(4)])



def main():
    # Test every method that you created: actions, result, goal_test.
    # Also try to solve the problem using the Trial_Error method (found in the search library)
    f_queen=FourQueensProblem()
    print(f_queen.actions(((0,0,0,0)
                        (0,0,0,0)
                        (0,0,0,0)
                        (0,0,0,0))))

    my_goal_state


    main()

