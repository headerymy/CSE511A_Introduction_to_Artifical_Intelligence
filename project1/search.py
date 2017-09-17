# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first
    [2nd Edition: p 75, 3rd Edition: p 87]

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    stack = util.Stack()
    discovered_node = set()
    result = []

    stack.push((problem.getStartState(), []))

    while not stack.isEmpty():
        (vertex, tmp_path) = stack.pop()
        if problem.isGoalState(vertex):
            return tmp_path
        if vertex not in discovered_node:
            discovered_node.add(vertex)
            for successors in problem.getSuccessors(vertex):
                result = list(tmp_path)
                result.append(successors[1])
                stack.push((successors[0], result))
    return result

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    [2nd Edition: p 73, 3rd Edition: p 82]
    """
    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    discovered_node = set()
    result = []

    queue.push((problem.getStartState(), []))
    if problem.isGoalState(problem.getStartState()):
        return []

    while not queue.isEmpty():
        (vertex, tmp_path) = queue.pop()
        if vertex not in discovered_node:
            discovered_node.add(vertex)
            for successors in problem.getSuccessors(vertex):
                result = list(tmp_path)
                if problem.isGoalState(vertex):
                    return tmp_path
                result.append(successors[1])
                queue.push((successors[0], result))
    return result

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    priority_queue = util.PriorityQueue()
    discovered_node = set()
    result = []

    priority_queue.push((problem.getStartState(), []), 0)

    while not priority_queue.isEmpty():
        (vertex, tmp_path) = priority_queue.pop()
        if problem.isGoalState(vertex):
            return tmp_path
        discovered_node.add(vertex)
        for successors in problem.getSuccessors(vertex):
            if successors[0] not in discovered_node:
                priority = problem.getCostOfActions(tmp_path) + successors[2]
                result = list(tmp_path)
                result.append(successors[1])
                priority_queue.push((successors[0], result),priority)
    return result

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    priority_queue = util.PriorityQueue()
    discovered_node = set()
    result = []
    g_n = 0
    h_n = heuristic(problem.getStartState(), problem)
    f_n = g_n + h_n

    priority_queue.push((problem.getStartState(), []), f_n)

    while not priority_queue.isEmpty():
        (vertex, tmp_path) = priority_queue.pop()
        if problem.isGoalState(vertex):
            return tmp_path
        discovered_node.add(vertex)
        for successors in problem.getSuccessors(vertex):
            if successors[0] not in discovered_node:
                g_n = problem.getCostOfActions(tmp_path) + heuristic(vertex, problem)
                result = list(tmp_path)
                result.append(successors[1])
                priority_queue.push((successors[0], result), g_n)
    return result

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
