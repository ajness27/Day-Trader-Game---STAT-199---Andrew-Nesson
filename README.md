# Day Trader: A Day in the Life

## About the game

You start the trading day with $150,000 and choose from 15 fictional stocks. Your goal is to finish with at least $150,000. The game randomly picks a bullish or bearish market at the start, and that condition stays the same all day.

## Project Files

- `DayTradeGame.py` starts the game and runs the main trading loop.
- `DayTrade_Functions.py` handles player input, calculates trade results, and displays the closing summary.
- `Stock_Data.py` stores the game rules, stock lists, news events, and trading times.

## How to play

1. Keep the three Python files in the same folder. Open `DayTradeGame.py` in VS Code and click **Run Python File**.
2. Read the market outlook and pick a ticker from the stock list. Uppercase and lowercase both work. If you enter an unknown ticker, the game asks you to choose again.
3. Enter an amount from $1 up to your current balance. The game asks again if the amount is invalid.
4. Read the market news, the chance of success, and how much you gained or lost. The trading session advances after each completed trade.
5. After two completed trades, you can enter `STOP` at the ticker prompt to end the day. The game ends automatically after seven completed trades.
6. Review your trade history and final balance. You win if you finish with at least $150,000.

## Risk and randomness

The base chance of a successful trade is 60% in a bullish market and 40% in a bearish market. After you enter a valid investment, a random news event adjusts that chance by 3 or 5 percentage points in either direction. The game then uses the adjusted chance to determine the result.

| Stock risk | Gain if successful | Loss if unsuccessful |
| --- | ---: | ---: |
| High | 40% | 30% |
| Moderate | 20% | 15% |
| Low | 8% | 5% |

These percentages apply to the amount you invest. Three functions use Python's `random` module. `choose_market_condition()` picks the market, `choose_market_event()` picks the news, and `complete_trade()` determines the trade result.

## Player state

I used a dictionary called `state` to keep the player's information together and pass it between functions. The keys make it clear what each value represents.

- `money` stores the current balance as a float.
- `trade_count` stores the number of completed trades and determines which trading session to display.
- `market_condition` stores whether the market is bullish or bearish.
- `history` stores each trade's ticker, investment, and gain or loss. A list keeps the trades in the order they happened.

At the end of the day, `player_won()` calls `get_account_value()` to get the balance and compares it with the starting balance.

## Control flow

The game shows the market outlook and stock list, then the main `while` loop calls `play_trade()` as long as the player has completed fewer than seven trades and has at least $1 available. An unknown ticker or a `STOP` entered before two completed trades brings the player back to the ticker prompt. After a valid ticker, a separate `while` loop asks for an investment until the player enters a valid amount. The game then shows a market news event, determines the trade result, and updates the player's balance, trade count, and history. When the game ends, a `for` loop prints the trade history, and the game shows the number of completed trades, the final balance, and whether the player won or lost.

## Changes after peer review

- Finished the trade history so the closing summary shows each ticker, the amount invested, and the gain or loss.
- Expanded the function docstrings to describe what each function does, its inputs, and its outputs.
- Organized the code into three files and moved the input and trade logic for each turn into `play_trade()`.
- Fixed investment validation so the game rejects `nan` and `inf` and asks for another amount.
- Added trading-session labels, random market news, and a market-closing message.