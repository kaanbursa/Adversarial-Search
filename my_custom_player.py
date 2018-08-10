import math
import random


from sample_players import DataPlayer

class CustomPlayer(DataPlayer):
  """ Implement your own agent to play knight's Isolation
  The get_action() method is the only required method for this project.
  You can modify the interface for get_action by adding named parameters
  with default values, but the function MUST remain compatible with the
  default interface.
  **********************************************************************
  NOTES:
  - The test cases will NOT be run on a machine with GPU access, nor be
    suitable for using any other machine learning techniques.
  - You can pass state forward to your agent on the next turn by assigning
    any pickleable object to the self.context attribute.
  **********************************************************************
  """




  def get_action(self, state):
    """ Employ an adversarial search technique to choose an action
    available in the current state calls self.queue.put(ACTION) at least
    This method must call self.queue.put(ACTION) at least once, and may
    call it as many times as you want; the caller will be responsible for
    cutting off the function after the search time limit has expired.
    See RandomPlayer and GreedyPlayer in sample_players for more examples.
    **********************************************************************
    NOTE:
    - The caller is responsible for cutting off search, so calling
      get_action() from your own code will create an infinite loop!
      Refer to (and use!) the Isolation.play() function to run games.
    **********************************************************************
    """
    # TODO: Replace the example implementation below with your own search
    #       method by combining techniques from lecture
    #
    # EXAMPLE: choose a random move without any search--this function MUST
    #          call self.queue.put(ACTION) at least once before time expires
    #          (the timer is automatically managed for you)


    if state.ply_count < 2:
      self.queue.put(random.choice(state.actions()))
    else:
      for depth in range(1, 100):
        action = self.alpha_beta_search(state, depth)
        if action is not None:
          self.queue.put(action)

  def alpha_beta_search(self, state, depth):
    """Alpha beta with iterative deepening"""
    beta = float("inf")
    best_score = float("-inf")
    best_move = None
    for a in state.actions():
        v = self.min_value(state.result(a), best_score, beta, depth - 1)
        if v > best_score:
            best_score = v
            best_move = a

    # f = open("analysis.csv", "a")
    # f.write(str(depth) + ", " + str(state.ply_count) + "\n")
    # f.close()
    return best_move

  def min_value(self, state, alpha, beta, depth):
    if depth <= 0:
      return self.heuristic_func(state)
    if state.terminal_test():
      return state.utility(self.player_id)

    v = float("inf")
    for a in state.actions():
      v = min(v, self.max_value(state.result(a), alpha, beta, depth - 1))
      if v <= alpha:
        return v
      beta = min(beta, v)
    return v

  def max_value(self, state, alpha, beta, depth):
    if depth <= 0:
      return self.heuristic_func(state)
    if state.terminal_test():
      return state.utility(self.player_id)

    v = float("-inf")
    for a in state.actions():
      v = max(v, self.min_value(state.result(a), alpha, beta, depth - 1))
      if v >= beta:
        return v
      alpha = max(alpha, v)
    return v

  def move_diff(self, state):
    """ own possible moves - opponent possible moves """
    own_loc = state.locs[self.player_id]
    opp_loc = state.locs[1 - self.player_id]
    own_liberties = state.liberties(own_loc)
    opp_liberties = state.liberties(opp_loc)
    return len(own_liberties) - len(opp_liberties)

  def heuristic_func(self, state):
    """ Heuristic for the game isolation to follow ."""
    own_loc = state.locs[self.player_id]
    opp_loc = state.locs[1 - self.player_id]
    player_distance = self.e_distance(self.coordinates(own_loc), self.coordinates(opp_loc))
    moves_diff = self.move_diff(state)

    if state.ply_count < 20:
      # Mimic opponent moves for the first 20 plays
      return moves_diff - player_distance
    elif state.ply_count < 35:
      # Get away for another from the opponent 15 moves
      return player_distance + moves_diff + self.distance_to_center(self.coordinates(own_loc))
    else:
      # Near the end get closer to the opponent and the center
      return 0 - player_distance + moves_diff - self.distance_to_center(self.coordinates(own_loc))


  def coordinates(self, loc):
       """ Gets x,y coordinates of location"""
       x = loc % 13 # get column
       y = math.floor(loc/13) # get row
       return x, y

  def distance_to_center(self, location):
       """ The distance to the center from location """
       return self.e_distance(location, (5, 4))

  def e_distance(self, loc1, loc2):
       """ Return the distance between the locations """
       xa = loc1[0]
       ya = loc1[1]
       xb = loc2[0]
       yb = loc2[1]

       return math.sqrt((xa - xb)**2 + (ya - yb)**2)
