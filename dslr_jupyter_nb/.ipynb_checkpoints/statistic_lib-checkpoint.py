import numpy as np
import pandas as pd

def is_nan(value):
    return value != value

def sum_custom(data):
    total = 0
    for i in data:
        if not is_nan(i):
            total += i
    return total

def count(data):
    return len([x for x in data if not is_nan(x)])

def mean(data):
    n = count(data)
    if n == 0:
        return None
    return sum_custom(data) / n

def var(data):
    n = count(data)
    if n < 2:
        return None
    mean_val = mean(data)
    return sum((x - mean_val)**2 for x in data if not is_nan(x)) / (n - 1)

def std(data):
    variance = var(data)
    if variance is None:
        return None
    return square_root(variance)

def square_root(n, precision=0.0001):
    if n < 0:
        raise ValueError("La racine carrée d'un nombre négatif est indéfinie")
    if n == 0:
        return 0
    x = n / 2
    while True:
        root = 0.5 * (x + n / x)
        if abs(root - x) < precision:
            return root
        x = root

def min_custom(data):
    df_non_nan = [x for x in data if not is_nan(x)]
    if not df_non_nan:
        return None
    min_val = df_non_nan[0]
    for i in df_non_nan[1:]:
        if min_val > i:
            min_val = i
    return min_val

def max_custom(data):
    df_non_nan = [x for x in data if not is_nan(x)]
    if not df_non_nan:
        return None
    max_val = df_non_nan[0]
    for i in df_non_nan[1:]:
        if max_val < i:
            max_val = i
    return max_val

def first_quartile(data):
    df_non_nan = [x for x in data if not is_nan(x)]
    df_sorted = sorted(df_non_nan)
    index = 0.25 * (len(df_sorted) - 1)
    return df_sorted[int(index)] if index.is_integer() else (df_sorted[int(index)] + df_sorted[int(index) + 1]) / 2

def median(data):
    df_non_nan = [x for x in data if not is_nan(x)]
    df_sorted = sorted(df_non_nan)
    index = 0.5 * (len(df_sorted) - 1)
    return df_sorted[int(index)] if index.is_integer() else (df_sorted[int(index)] + df_sorted[int(index) + 1]) / 2

def third_quartile(data):
    df_non_nan = [x for x in data if not is_nan(x)]
    df_sorted = sorted(df_non_nan)
    index = 0.75 * (len(df_sorted) - 1)
    return df_sorted[int(index)] if index.is_integer() else (df_sorted[int(index)] + df_sorted[int(index) + 1]) / 2

def skewness(df):
    df_non_nan = [x for x in df if not is_nan(x)]
    n = len(df_non_nan)
    mean_val = mean(df_non_nan)
    std_val = std(df_non_nan)
    if std_val == 0:
        return 0
    skew_sum = sum(((x - mean_val) / std_val)**3 for x in df_non_nan)
    return (n / ((n-1) * (n-2))) * skew_sum

def kurtosis(df):
    df_non_nan = [x for x in df if not is_nan(x)]
    n = len(df_non_nan)
    mean_val = mean(df_non_nan)
    std_val = std(df_non_nan)
    if std_val == 0:
        return 0
    kur_sum = sum(((x - mean_val) / std_val)**4 for x in df_non_nan)
    kurt = (n * (n + 1) / ((n - 1) * (n - 2) * (n - 3))) * kur_sum - (3 * (n - 1)**2 / ((n - 2) * (n - 3)))
    return kurt
