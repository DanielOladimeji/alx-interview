#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    def calculate_primes(n):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return [num for num in range(n + 1) if primes[num]]

    def get_winner(round_nums):
        num_primes = calculate_primes(max(round_nums))
        xor_sum = 0
        for num in round_nums:
            if num in num_primes:
                xor_sum ^= num_primes.index(num) % 2

        return "Maria" if xor_sum != 0 else "Ben"

    winners = []
    for i in range(x):
        round_winner = get_winner(list(range(1, nums[i] + 1)))
        winners.append(round_winner)

    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
