import random
import math
from scipy.stats import chisquare

def frequency_test(data):
    p_value = chisquare(data)[1]
    return p_value

def runs_test(data):
    runs = [1 if data[i] > data[i-1] else 0 for i in range(1, len(data))]
    p_value = chisquare(runs)[1]
    return p_value


def poker_test(data):
    hands = [len(set(str(x))) for x in data]
    p_value = chisquare(hands)[1]
    return p_value

random_stream = [random.randint(0, 1) for _ in range(1000)]

# Apply randomness tests
print("Frequency Test p-value:", frequency_test(random_stream))
print("Runs Test p-value:", runs_test(random_stream))
print("Poker Test p-value:", poker_test(random_stream))