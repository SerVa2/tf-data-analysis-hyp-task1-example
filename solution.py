import pandas as pd
import numpy as np

from scipy.stats import norm
chat_id = 1633714108 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, x_cnt: int, y_success: int, y_cnt: int) -> bool:
    p_control_op = x_success / x_cnt
    p_test_op = y_success / y_cnt
    p_control_robot = p_test_robot = (x_success + y_success) / (x_cnt + y_cnt)
    z_stat = (p_test_robot - p_test_op) / np.sqrt(p_test_robot * (1 - p_test_robot) * (1 / x_cnt + 1 / y_cnt))
    z_crit = norm.ppf(0.95)
    return z_stat > z_crit
