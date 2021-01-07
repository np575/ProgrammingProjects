#cs370 project
#Nisarg Patel- np575
#Shubham Gohel- smg56

class node:

    @staticmethod
    def get_h_cost(state, goal, function):

        heuristic_cost = 0

        # the number of puzzle pieces out of place
        if function == 'out_of_position':
            for x in zip(state, goal):
                if x[0] != x[1]:
                    heuristic_cost += 1
                else:
                    continue

        # manhattan distance of the puzzle pieces
        # to their goal state
        elif function == 'manhattan_distance':
            for x in goal:
                heuristic_cost += abs(goal.index(x) - state.index(x))

        # euclidean distance of the puzzle pieces to their
        # goal state
        else:
            for x in goal:
                heuristic_cost += (goal.index(x) - state.index(x))**2

        return heuristic_cost

    def __init__(self, key, state, parent, g_of_n, depth, h_function, goal, move):

        self.key = key
        self.state = state
        self.parent = parent
        self.g_of_n = g_of_n
        self.depth = depth
        self.h_function = h_function
        self.goal = goal
        self.move = move
        self.h_of_n = node.get_h_cost(self.state , self.goal , self.h_function)
        self.total_cost = self.g_of_n + self.h_of_n
        self.get_moves()

    def get_moves(self):

        # returns a list of possible moves in the current state
        
        self.moves = []

        # possible moves were hard coded depending on the state
        if self.state.index(0) == 0:  self.moves.extend(('left','up'))
        elif self.state.index(0) == 1:  self.moves.extend(('left','right','up'))
        elif self.state.index(0) == 2:  self.moves.extend(('right','up'))
        elif self.state.index(0) == 3:  self.moves.extend(('up','down', 'left'))
        elif self.state.index(0) == 4:  self.moves.extend(('up','down','left','right',))
        elif self.state.index(0) == 5:  self.moves.extend(('right','up', 'down'))
        elif self.state.index(0) == 6:  self.moves.extend(('down','left'))
        elif self.state.index(0) == 7:  self.moves.extend(('left','right', 'down'))
        else:  self.moves.extend(('right','down'))
    
    def move_piece(self, move):

        #returns the list item representing new node state, an integer representing the cost
        
        new_node = self.state[:]
        zero_idx = new_node.index(0)

        if move == 'left':  rep_idx = zero_idx + 1
        elif move == 'right':  rep_idx = zero_idx - 1
        elif move == 'up':  rep_idx = zero_idx + 3
        else:  rep_idx = zero_idx - 3

      
        rep_val = self.state[rep_idx]
        new_node[zero_idx] = rep_val
        new_node[rep_idx] = 0
        return new_node , rep_val

class queue:

    def __init__(self, search_algorithm, goal_state):

        # class to create a queue for a search tree
       
        self.search_algorithm = search_algorithm
        self.queue = []

    def return_node(self):

        #returns a object of class node
        
        if self.search_algorithm == 'breadth_first':  return self.queue[0] # first in first out
        elif self.search_algorithm == 'depth_first':  return self.queue[-1] # last in first out
        elif self.search_algorithm == 'uniform_cost':  return sorted(self.queue, key=lambda x: x.g_of_n)[0]  # return node with the lowest cost
        elif self.search_algorithm == 'a_star':  return sorted(self.queue, key=lambda x: x.total_cost)[0] # return node with the lowest total cost
        elif self.search_algorithm == 'best_first':  return sorted(self.queue, key=lambda x: x.h_of_n)[0] # return node with the lowest heuristic cost
        elif self.search_algorithm == 'iterative_deepening': return sorted(self.queue, key=lambda x: x.depth)[0]

class searchTreeSolver:

    def __init__(self, node_init, goal_state, search_algorithm, iterative_deep):

        self.goal_state = node_init.goal
        self.current_node = node_init
        self.root = node_init
        self.search_algorithm = search_algorithm
        self.heuristic_function = node_init.h_function
        self.iterative_deep = iterative_deep
        self.key = 0
        self.move_counter = 0
        self.tree = {}
        self.queue = queue(self.search_algorithm, self.goal_state)
        self.queue.queue.append(self.root)
        self.visited_states = []
        self.depth_counter = 0
        self.limit = 0
        self.tree[0] = self.root
        self.solver()

    def solver(self):

        import time
        start_time = time.time()
        self.current_node = self.queue.return_node()

        while self.queue:

            que_len = []
            que_len.append(len(self.queue.queue))

            if self.current_node.state != self.goal_state:

                if self.iterative_deep:
                    if self.depth_counter > self.limit:
                        self.limit += 1
                        self.key = 0
                        self.move_counter = 0
                        self.tree = {}
                        self.queue = queue(self.search_algorithm, self.goal_state)
                        self.queue.queue.append(self.root)
                        self.visited_states = []
                        self.depth_counter = 0
                        self.current_node = self.root
                    else:  pass
                else:  pass


                if self.current_node.state not in self.visited_states:
                    self.visited_states.append(self.current_node.state[:])
                    self.move_counter+=1

                    
                    for move in self.current_node.moves:
                        self.key += 1
                        new_state , g_of_n = self.current_node.move_piece(move)
                        g_of_n += self.current_node.g_of_n
                        new_node = node(key=self.key,state=new_state,parent=self.current_node.key,g_of_n = g_of_n,depth=self.depth_counter+1,\
                                        h_function=self.heuristic_function,goal=self.goal_state,move=move)
                        self.tree[self.key] = new_node

                        # checking to see if the cost of these existing nodes is more, if it isn't we leave the node in the queue
                      
                        if self.search_algorithm in ['uniform_cost', 'a_star', 'best_first']:
                            c = 0
                            if self.search_algorithm == 'uniform_cost':  sort = 'g_of_n'
                            elif self.search_algorithm == 'a_star':  sort = 'total_cost'
                            else:  sort = 'h_of_n'

                            for i in self.queue.queue:
                                    if i.state == new_node.state:
                                        if getattr(i,sort) > getattr(new_node,sort):
                                            del self.queue.queue[c]
                                        else:  c+=1
                                    else:  c += 1

                        else:  pass

                        self.queue.queue.append(new_node)

                    self.depth_counter+=1
                    self.current_node = self.queue.return_node()

                else:
                    
                    if self.search_algorithm == 'depth_first':  idx = -1
                    else:  idx = 0

                    if self.search_algorithm == 'uniform_cost':  self.queue.queue = sorted(self.queue.queue, key=lambda x: x.g_of_n)
                    elif self.search_algorithm == 'best_first':  self.queue.queue = sorted(self.queue.queue, key=lambda x: x.h_of_n)
                    elif self.search_algorithm == 'a_star':  self.queue.queue = sorted(self.queue.queue, key=lambda x: x.total_cost)
                    else:  pass

                    # we now delete an item from the queue based on the index defined above
                    del self.queue.queue[idx]
                    self.current_node = self.queue.return_node()

            else:
                # the puzzle has been solved so we can break the while loop and end the madness
                break


        end_time = time.time()
        for k,v in self.tree.items():
            if v.state == self.goal_state:
                kinit = k
                break
            else:  continue

        path_list = [kinit]
        while kinit != 0:
            path_list.insert(0, self.tree[kinit].parent)
            kinit = path_list[0]

        for i in path_list:
            print ('Move:', self.tree[i].move, '\n', 'Heuristic Cost:', self.tree[i].h_of_n, '\n', 'Total Cost:',self.tree[i].g_of_n,\
                '\n', self.tree[i].state[0:3], '\n', self.tree[i].state[3:6], '\n', self.tree[ i].state[6:], '\n')
        print ('Total Moves Made: ', len(path_list) - 1 )
        print ('8 Puzzle Solved', '\n', '~~Max Queue Length:', max(que_len), '\n', '~~Nodes Popped:', self.move_counter, '\n',\
            '~~Runtime:', end_time - start_time, '\n', '~~Total Moves:', self.move_counter, '\n')


goal = [1,2,3,8,0,4,7,6,5]
easy = [1,3,4,8,6,2,7,0,5]
medium = [2,8,1,0,4,3,7,6,5]
hard = [5,6,7,4,0,8,3,2,1]
tester = [1,0,3,8,2,4,7,6,5]
hfun = 'manhattan_distance'
salgo = 'a_star'
ideep = False
test_node = node(key=0,state=easy,parent=0,g_of_n=0,depth=0,h_function=hfun,goal=goal,move='Initial State')
test = searchTreeSolver(test_node,goal_state=goal,search_algorithm=salgo,iterative_deep=ideep)

