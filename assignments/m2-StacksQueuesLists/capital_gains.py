#!/usr/bin/env python3

"""
Objective:
The goal of this assignment is to ensure your understanding and application of the Stack and
Queue data structures. You'll solve a problem scenario requiring the use of either Stack,
Queue, or both. By the end of this assignment, you should be familiar with these abstract data
types, their usage, and implementation. You might be surprised to learn how frequently these
data structures are used in computer systems!

Problem Scenario:
Consider a scenario where shares of a company's common stock are bought and sold. The capital
gain (or sometimes loss) is the difference between the selling price and the original purchase
price. This is straightforward for a single share, but if multiple shares are sold, which were
bought over a period of time, identifying the shares sold becomes challenging.

A common accounting principle for this situation is the FIFO (First In, First Out) protocol,
meaning the shares sold are those held for the longest time. For example, if 100 shares are
bought at $20 each on day 1, 20 shares at $24 on day 2, 200 shares at $36 on day 3, and 150
shares are sold on day 4 at $30 each, the FIFO protocol implies that out of the 150 shares sold,
100 were bought on day 1, 20 on day 2, and 30 on day 3. The capital gain would therefore be
100 * 10 + 20 * 6 + 30 * (-6), or $940.

Tasks:
Your task is to write a Python program that takes a sequence of transactions as input. Each
transaction will be in the form of "buy x share(s) at y each" or "sell x share(s) at y each,"
with the assumption that the transactions occur on consecutive days and the values x and y are
integers. The output should be the total capital gain (or loss) for the entire sequence, using
the FIFO protocol to identify shares.

Sample runs:
    Input:
    buy 100 shares at 20 each
    buy 20 shares at 24 each
    buy 200 shares at 36 each
    sell 150 shares at 30 each

    Output:
    The total capital gain is $940


    Input:
    buy 50 shares at 10 each
    buy 30 shares at 15 each
    buy 100 shares at 20 each
    sell 70 shares at 18 each

    Output:
    The total capital gain is $460
"""

from ast import (
    literal_eval,
)  # https://stackoverflow.com/questions/74665788/how-to-convert-string-to-number-in-python
from collections import deque
from typing import Union


def calculate_capital_gain(transactions: str) -> Union[int, float]:
    """Calculate capital gain for a daily series of transactions.

    Implementation should include a stack, a queue, or both.

    Parameters
    ----------
    transactions: string

    Examples
    --------
    Input:\n
    buy 100 shares at 20 each\n
    buy 20 shares at 24 each\n
    buy 200 shares at 36 each\n
    sell 150 shares at 30 each\n

    Output:\n
    The total capital gain is $940\n


    Input:\n
    buy 50 shares at 10 each\n
    buy 30 shares at 15 each\n
    buy 100 shares at 20 each\n
    sell 70 shares at 18 each\n

    Output:\n
    The total capital gain is $460\n
    """
    buy_queue = deque()
    sold_queue = deque()
    prepped = [
        tuple(transaction.split(" ")) for transaction in transactions.split("\n")
    ]
    logged = [transaction[0:2] + transaction[4:5] for transaction in prepped]
    [
        buy_queue.extend(int(shares) * [literal_eval(price)])
        if action == "buy"
        else sold_queue.extend(
            [literal_eval(price) - buy_queue.popleft() for _ in range(int(shares))]
        )
        for action, shares, price in logged
    ]
    return round(sum(sold_queue), 4)


def gains_are(transactions: str) -> str:
    """Pretty print capital gain."""
    capital_gain = calculate_capital_gain(transactions)
    print(
        f"The total capital gain is {
            f"-${abs(capital_gain)}" if capital_gain < 0 else f"${capital_gain}"
            }"
    )


def test():
    """Execute test cases for task."""

    ins = {
        """buy 5 shares at 10.76 each
buy 3 shares at 15.1 each
buy 10 shares at 20.2 each
sell 7 shares at 18.99 each""": "$48.93",
        """buy 40 shares at 5 each # +120
buy 50 shares at 6 each # +60 +160
sell 70 shares at 8 each
buy 10 shares at 10 each # +40
sell 30 shares at 14 each""": "$380",
        """buy 10 shares at 100 each
sell 10 shares at 0 each""": "-$1000",
        """buy 100 shares at 10 each
sell 100 shares at 10 each""": "$0",
        """buy 50 shares at 2 each
sell 50 shares at 22 each""": "$1000",
        """buy 100 shares at 20 each
buy 20 shares at 24 each
buy 200 shares at 36 each
sell 150 shares at 30 each""": "$940",
        """buy 50 shares at 10 each
buy 30 shares at 15 each
buy 100 shares at 20 each
sell 70 shares at 18 each""": "$460",
    }

    [
        (
            print("\nIf you:"),
            print(window),
            gains_are(window),
            print(f"The correct answer is:\t  {answer}"),
        )
        for window, answer in ins.items()
    ]


if __name__ == "__main__":
    test()
