import pandas as pd
import numpy as np

from scipy.stats import norm
chat_id = 1633714108 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.05 # уровень значимости
    
    p_control = x_success / x_cnt # вероятность успеха на выборке из контроля
    p_test = y_success / y_cnt # вероятность успеха на выборке из теста
    
    p_combined = (x_success + y_success) / (x_cnt + y_cnt) # объединенная вероятность успеха
    se = np.sqrt(p_combined * (1 - p_combined) * (1/x_cnt + 1/y_cnt)) # стандартная ошибка разности
    
    z_score = (p_test - p_control) / se # Z-оценка
    
    if z_score > 0 and z_score > alpha/2: # если Z-оценка больше уровня значимости и положительна
        return True # отклоняем нулевую гипотезу
    elif z_score < 0 and abs(z_score) > alpha/2: # если Z-оценка меньше уровня значимости и отрицательна
        return True # отклоняем нулевую гипотезу
    else:
        return False # не отклоняем нулевую гипотезу
