from treys import Evaluator
from community_cards import Board


class Hand():
    """
    Hand class for each round of the game. Logic for game evaluation to be built here.

    Args: 
        - holdings: dict of each players holding
            - each one a is a Holding object from above
        - board: list of cards on the board (Board object)

    """

    def __init__(self, holdings, board):
        self.holdings = holdings
        self.board = board
        self.ranks = self._add_hand_ranks()
        # TODO: check if board + holdings have duplicates

    def get_ranks(self):
        return self.ranks

    def who_won(self):
        # TODO: handle ties
        return min(self.ranks, key=lambda x: self.ranks[x])

    @property
    def holdings(self):
        return self._holdings

    @holdings.setter
    def holdings(self, holdings):
        # TODO: handle holdings type here
        self._holdings = holdings

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, board):
        assert isinstance(
            board, Board), "Error: board must be a community_cards.Board object"
        self._board = board

    def _add_hand_ranks(self):
        ranks = {}
        for player, holding in self.holdings.items():
            ranks[player] = Evaluator().evaluate(
                self.board.cards, self.holdings[player].cards)
        return ranks
