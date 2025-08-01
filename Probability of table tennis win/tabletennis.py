from random import random
from scipy.stats import binom

def will_win(p_win: float, win_score: float) -> bool:
    p1 = 0
    p2 = 0
    while True:
        if random() < p_win:
            p1 += 1
        else:
            p2 += 1
        if p1 >= win_score and p2 + 2 <= p1:
            return True
        if p2 >= win_score and p1 + 2 <= p2:
            return False


def win_probability(p_win: float, win_score: float) -> float:
    p_loss = 1 - p_win
    tie_score = win_score - 1
    p_win_overall = 1 - binom.cdf(tie_score, 2 * tie_score, p_win)
    p_tie = binom.pmf(tie_score, 2 * tie_score, p_win)
    p_win_from_equal = p_win * p_win / (p_win * p_win + p_loss * p_loss)
    p_win_overall += p_tie * p_win_from_equal
    return p_win_overall
