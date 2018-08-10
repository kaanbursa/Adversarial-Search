
# Build an Adversarial Game Playing Agent

![Example game of isolation on a square board](viz.gif)

## Synopsis

In this project, you will experiment with adversarial search techniques by building an agent to play knights Isolation.  Unlike the examples in lecture where the players control tokens that move like chess queens, this version of Isolation gives each agent control over a single token that moves in L-shaped movements--like a knight in chess.

### Isolation

In the game Isolation, two players each control their own single token and alternate taking turns moving the token from one cell to another on a rectangular grid.  Whenever a token occupies a cell, that cell becomes blocked for the remainder of the game.  An open cell available for a token to move into is called a "liberty".  The first player with no remaining liberties for their token loses the game, and their opponent is declared the winner.

In knights Isolation, tokens can move to any open cell that is 2-rows and 1-column or 2-columns and 1-row away from their current position on the board.  On a blank board, this means that tokens have at most eight liberties surrounding their current location.  Token movement is blocked at the edges of the board (the board does not wrap around the edges), however, tokens can "jump" blocked or occupied spaces (just like a knight in chess).

Finally, agents have a fixed time limit (150 milliseconds by default) to search for the best move and respond.  The search will be automatically cut off after the time limit expires, and the active agent will forfeit the game if it has not chosen a move.

### Heuristics

In addition to Minimax algorithm which is the default agents playing strategy. My agent play with Alpha-Beta-Prunning and its own heuristic Isolation game strategy. Which is following the opponent when the game starts, after when the midgame reaches (which is calculated after playing several times) Mid game the agent tries to get away from the opponent. Near the end keep the around the center and near opponent.

### Results

%80 + percent winning ratio within limited calculation time for the agent.





