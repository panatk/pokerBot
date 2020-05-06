from treys import Evaluator

class Holding():
    """
    Object that holds players cards. 

    Args:
        - cards (list of treys ints)
    """

    def __init__(self, cards):
        self._cards = cards

    @property
    def cards(self):
        return self._cards
    
    @cards.setter
    def cards(self, cards):
        assert len(self.cards) == 2, "Error: Incorrect number of cards in holding"
        assert self.cards[0] != self.cards[1], "Error: Duplicates exist in the holding"
        self._cards = cards


class Board():
    """
    Object that holds the community cards.

    Args:
        - flop (list of treys ints), turn (treys int), river (treys int)
    """

    def __init__(self, flop, turn, river):
        self.flop = flop
        self.turn = turn
        self.river = river
        self._cards = self._get_total_board()
    
    def _get_total_board(self):
        total_board = self.flop + [self.turn] + [self.river]
        assert len(set(total_board)) == len(total_board), "Error: Duplicates exist on the board"
        return total_board

    @property
    def flop(self):
        return self._flop

    @property
    def turn(self):
        return self._turn
    
    @property
    def river(self):
        return self._river
    
    @property
    def cards(self):
        return self._cards

    @flop.setter
    def flop(self, flop):
        if len(flop) != 3:
            raise ValueError("Error: Incorrect number of cards on the flop")
        self._flop = flop

    @turn.setter
    def turn(self, turn):
        self._turn = turn

    @river.setter
    def river(self, river):
        self._river = river



class Hand():
    """
    Hand class for each round of the game.

    Args: 
        - holdings: dict of each players holding
            - each one a is a Holding object from above
        - board: list of cards on the board (Board object)

    """

    def __init__(self, holdings, board):
        #TODO: assert type of holdings and board
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
