import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest

chat_id = 1633714108 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.05
    stats, p_value = proportions_ztest(np.array([x_success, y_success]), np.array([x_cnt, y_cnt]), alternative = 'smaller')
    return p_value < alpha
