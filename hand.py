
class Hand():
    """
    Hand class for each round of the game.

    Args: 
        - holdings: dict of each players holding
            - each one a is a Holding object from above
        - board: list of cards on the board (Board object)

    """

    def __init__(self, holdings, board):
        # TODO: assert type of holdings and board
        self.holdings = holdings
        self.board = board
        self.ranks = self._add_hand_ranks()
        # TODO: error handling
        # check duplicates in deck
        # check number of cards in hand
        # number of cards in board

    def _add_hand_ranks(self):
        ranks = {}
        for player, holding in self.holdings.items():
            ranks[player] = Evaluator().evaluate(
                self.board.cards, self.holdings[player].cards)
        return ranks

    def get_holding(self):
        return self.holdings

    def get_ranks(self):
        return self.ranks

    def who_won(self):
        # TODO: handle ties
        return min(self.ranks, key=lambda x: self.ranks[x])
