from treys import Evaluator, Card


class Street():
    def __init__(self, cards):
        self.cards = [Card.new(x) for x in cards]

    def get_card_str(self):
        return [Card.int_to_str(x) for x in self.cards]


class Flop(Street):
    def __init__(self, *args):
        super().__init__(args)
        self.flop = list(args)

    @property
    def flop(self):
        return self._flop

    @flop.setter
    def flop(self, flop):
        assert len(flop) == 3, "Error: Incorrect number of cards on the flop"
        self._flop = flop


class Turn(Street):
    def __init__(self, *args):
        super().__init__(args)
        self.turn = list(args)

    @property
    def turn(self):
        return self._turn

    @turn.setter
    def turn(self, turn):
        self._turn = turn


class River(Street):
    def __init__(self, *args):
        super().__init__(args)
        self.river = list(args)

    @property
    def river(self):
        return self._river

    @river.setter
    def river(self, river):
        self._river = river


class Board():
    """
    Object that holds the community cards.

    Args:
        - flop (Flop), turn (Turn), river (River)
    """

    def __init__(self, flop, turn=None, river=None):
        self.flop = flop.flop
        self.turn = turn.turn if turn is not None else []
        self.river = river.river if river is not None else []
        self._board = self._get_total_board()
        self.cards = [Card.new(x) for x in self._board]

    def _get_total_board(self):
        total_board = self.flop + self.turn + self.river
        assert len(set(total_board)) == len(
            total_board), "Error: Duplicates exist on the board"
        return total_board

    def get_card_str(self):
        return self._board