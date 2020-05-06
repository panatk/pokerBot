# from treys import Card, Deck
from treys import Evaluator


class Hand():
    """
    Hand class for each round of the game.

    Args: 
        - holdings: dict of each players hand
            - each hand is a list of two integers created using treys.Card.new()
        - board: list of cards on the board (also treys integers)

    """
    def __init__(self, holdings, board):
        self.holdings = holdings
        self.board = board
        self.ranks = self._add_hand_ranks()
        #TODO: error handling
        # check duplicates in deck
        # check number of cards in hand
        # number of cards in board

    def _add_hand_ranks(self):
        ranks = {}
        for player, holding in self.holdings.items():
            ranks[player] = Evaluator().evaluate(self.board, self.holdings[player])
        return ranks

    def get_holding(self):
        return self.holdings
    
    def get_ranks(self):
        return self.ranks
    
    def get_winner(self):
        #TODO: handle ties
        return min(self.ranks, key = lambda x:self.ranks[x])
        
        


        
