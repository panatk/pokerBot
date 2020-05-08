
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
