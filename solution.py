import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest
import math

chat_id = 1633714108 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, x_cnt: int, y_success: int, y_cnt: int) -> bool:
    alpha = 0.05
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    p = (x_success + y_success) / (x_cnt + y_cnt)
    se = math.sqrt(p * (1 - p) * (1/x_cnt + 1/y_cnt))
    z = (p1 - p2) / se
    z_critical = abs(norm.ppf(alpha / 2))  # посчитаем z-критическое значение
    return abs(z) > z_critical
