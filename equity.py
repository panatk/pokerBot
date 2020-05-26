
import holdem_calc

from player_cards import Holding


def calculate_equities(board, holdings, num_sims):
    # HACK to make it work with holdem_calculate
    # TODO:relies on dict ordering, change ASAP
    holding_list = [val for sublist in [x.get_card_str()
                                        for x in holdings.values()] for val in sublist]
    sim_output = holdem_calc.calculate(
        board, False, num_sims, None, holding_list, False)

    players = list(holdings.keys())
    equities = {}
    equities['tie'] = sim_output[0]

    i = 1
    for player in players:
        equities[player] = round(sim_output[i], 3)
        i += 1

    return equities