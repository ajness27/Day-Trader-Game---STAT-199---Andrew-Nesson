"""Constants and data used by the Day Trader game.

This module stores the game rules separately from the game functions so the
rules are easy to find and change.
"""


STARTING_MONEY = 150_000.00
MINIMUM_TRADES = 2
MAXIMUM_TRADES = 7
MINIMUM_INVESTMENT = 1.00

HIGH_RISK_STOCKS = ["AERX", "BIOZ", "CYBX", "NANQ", "RCKX"]
MODERATE_RISK_STOCKS = ["CEDR", "HLNX", "METR", "ORBA", "VANT"]
LOW_RISK_STOCKS = ["BANK", "FOOD", "HLTH", "UTIL", "WATR"]

ALL_STOCKS = HIGH_RISK_STOCKS + MODERATE_RISK_STOCKS + LOW_RISK_STOCKS

MARKET_EVENTS = {
    "bullish": [
        ("A strong jobs report gives buyers confidence.", 0.05),
        ("Several companies report better-than-expected earnings.", 0.03),
        ("Some traders take profits after the morning rally.", -0.03),
    ],
    "bearish": [
        ("New inflation data makes investors nervous.", -0.05),
        ("A major company lowers its earnings forecast.", -0.03),
        ("Value buyers step in after the early selloff.", 0.03),
    ],
}

TRADING_TIMES = [
    "9:30 a.m. - Opening Bell",
    "10:15 a.m. - Morning Session",
    "11:30 a.m. - Late Morning",
    "12:30 p.m. - Lunch Hour",
    "1:45 p.m. - Afternoon Session",
    "3:00 p.m. - Power Hour",
    "3:45 p.m. - Closing Trades",
]

