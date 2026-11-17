"""Run the final version of Day Trader: A Day in the Life."""

from DayTrade_Functions import (
    create_initial_state,
    display_end_of_day,
    display_intro,
    display_stocks,
    play_trade,
)

from Stock_Data import MAXIMUM_TRADES, MINIMUM_INVESTMENT

def __main__():
    """What it does: Creates the game state and runs the trading day.
    Inputs: None.
    Outputs: None.
    """
    state = create_initial_state()
    display_intro(state)
    display_stocks()

    while (state["trade_count"] < MAXIMUM_TRADES and state["money"] >= MINIMUM_INVESTMENT):
        keep_trading = play_trade(state)
        if not keep_trading:
            break

    display_end_of_day(state)

if __name__ == "__main__":
    __main__()