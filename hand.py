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
        self._ranks_eval_done = False
        # TODO: check if board + holdings have duplicates

    def get_ranks(self):
        self.ranks = self._add_hand_ranks()
        self._ranks_eval_done = True
        return self.ranks

    def get_winner(self):
        # TODO: handle ties
        if self._ranks_eval_done is False:
            self.get_ranks() 
        return min(self.ranks, key=lambda x: self.ranks[x])

    def get_hand_classes(self):
        if self._ranks_eval_done is False:
            self.get_ranks()
        hand_classes = {}
        for player, rank in self.ranks.items():
            hand_classes[player] = Evaluator().class_to_string(Evaluator().get_rank_class(rank))
        return hand_classes
        

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
