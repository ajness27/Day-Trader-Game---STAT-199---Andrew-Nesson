"""Simple functions for the Day Trader game."""

import random
from math import isfinite

from Stock_Data import (
    ALL_STOCKS,
    HIGH_RISK_STOCKS,
    LOW_RISK_STOCKS,
    MARKET_EVENTS,
    MINIMUM_INVESTMENT,
    MINIMUM_TRADES,
    MODERATE_RISK_STOCKS,
    STARTING_MONEY,
    TRADING_TIMES,
)


def choose_market_condition():
    """What it does: Randomly chooses the market condition.
    Inputs: None.
    Outputs: The string "bullish" or "bearish".
    """
    return random.choice(["bullish", "bearish"])


def create_initial_state():
    """What it does: Creates the player's starting state.
    Inputs: None.
    Outputs: A dictionary containing the starting game information.
    """
    return {
        "money": STARTING_MONEY,
        "trade_count": 0,
        "market_condition": choose_market_condition(),
        "history": [],
    }


def display_intro(state):
    """What it does: Displays the title and rules.
    Inputs: The player's state dictionary.
    Outputs: None.
    """
    print("=" * 50)
    print("DAY TRADER: A DAY IN THE LIFE")
    print("=" * 50)
    print(f"Starting money: ${state['money']:,.2f}")
    print("The market is", state["market_condition"])
    print("Make at least 2 trades and no more than 7 trades.")
    print("You can only buy stocks. You cannot short stocks.")


def display_stocks():
    """What it does: Displays the stocks in each risk category.
    Inputs: None.
    Outputs: None.
    """
    print("\nTODAY'S STOCKS")
    print("High risk:", HIGH_RISK_STOCKS)
    print("Moderate risk:", MODERATE_RISK_STOCKS)
    print("Low risk:", LOW_RISK_STOCKS)


def get_risk_category(stock_choice):
    """What it does: Finds the risk category of a stock.
    Inputs: The chosen stock ticker.
    Outputs: The string "high", "moderate", or "low".
    """
    if stock_choice in HIGH_RISK_STOCKS:
        return "high"
    elif stock_choice in MODERATE_RISK_STOCKS:
        return "moderate"
    else:
        return "low"


def choose_market_event(market_condition):
    """What it does: Randomly chooses a market news event.
    Inputs: The day's market condition.
    Outputs: A tuple containing the event and its chance adjustment.
    """
    return random.choice(MARKET_EVENTS[market_condition])


def complete_trade(investment, risk_category, market_condition, event_change):
    """What it does: Randomly decides whether a trade gains or loses money.
    Inputs: Investment, risk category, market condition, and event change.
    Outputs: The money change and chance of success.
    """
    if risk_category == "high":
        gain_percent = 0.40
        loss_percent = 0.30
    elif risk_category == "moderate":
        gain_percent = 0.20
        loss_percent = 0.15
    else:
        gain_percent = 0.08
        loss_percent = 0.05

    if market_condition == "bullish":
        success_chance = 0.60
    else:
        success_chance = 0.40

    success_chance = success_chance + event_change

    if random.random() < success_chance:
        money_change = investment * gain_percent
    else:
        money_change = -(investment * loss_percent)

    return money_change, success_chance


def play_trade(state):
    """What it does: Runs one trade and updates the player's state.
    Inputs: The player's state dictionary.
    Outputs: True to continue playing or False to stop.
    """
    print()
    print(TRADING_TIMES[state["trade_count"]])
    print("Trade number:", state["trade_count"] + 1)
    print(f"Money available: ${state['money']:,.2f}")
    stock_choice = input("Choose a ticker or enter STOP: ").strip().upper()

    if stock_choice == "STOP":
        if state["trade_count"] >= MINIMUM_TRADES:
            return False
        print("You need to make at least 2 trades.")
        return True

    if stock_choice not in ALL_STOCKS:
        print("That stock is not available.")
        return True

    valid_investment = False
    while not valid_investment:
        try:
            investment = float(input("Amount to invest: $"))
        except ValueError:
            print("Please enter the amount as a number.")
        else:
            if not isfinite(investment) or not (
                MINIMUM_INVESTMENT <= investment <= state["money"]
            ):
                print("That investment amount is not allowed.")
            else:
                valid_investment = True

    risk_category = get_risk_category(stock_choice)
    event, event_change = choose_market_event(state["market_condition"])
    print("Market update:", event)

    money_change, success_chance = complete_trade(
        investment,
        risk_category,
        state["market_condition"],
        event_change,
    )

    state["money"] = state["money"] + money_change
    state["trade_count"] = state["trade_count"] + 1
    state["history"].append([stock_choice, investment, money_change])

    print(f"Chance of success: {success_chance:.0%}")
    if money_change >= 0:
        print(f"You gained ${money_change:,.2f}.")
    else:
        print(f"You lost ${abs(money_change):,.2f}.")

    return True


def get_account_value(state):
    """What it does: Gets the player's current account value.
    Inputs: The player's state dictionary.
    Outputs: The current amount of money.
    """
    return state["money"]


def player_won(state):
    """What it does: Decides whether the player won the game.
    Inputs: The player's state dictionary.
    Outputs: True for a win or False for a loss.
    """
    return get_account_value(state) >= STARTING_MONEY


def display_end_of_day(state):
    """What it does: Displays the trade history and final result.
    Inputs: The player's state dictionary.
    Outputs: None.
    """
    print("\nTRADE HISTORY")

    for number in range(len(state["history"])):
        trade = state["history"][number]
        print(
            number + 1,
            trade[0],
            f"invested ${trade[1]:,.2f}",
            f"change ${trade[2]:,.2f}",
        )

    print("\nTHE MARKET IS CLOSED")
    print("Trades completed:", state["trade_count"])
    print(f"Final money: ${get_account_value(state):,.2f}")

    if player_won(state):
        print("You won the game!")
    else:
        print("You lost the game.")
