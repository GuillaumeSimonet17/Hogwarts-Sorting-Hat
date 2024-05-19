def is_nan(value):
    return value != value

def sum(df):
    sum = 0
    for i in df:
        if not is_nan(i):
            sum += i
    return sum

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

def count(df):
    count = 0
    for i in df:
        if not is_nan(i):
            count += 1
    return count

def mean(df):
    return sum(df / count(df))

def var(df):
    return 1/count(df) * sum((df - mean(df))**2)

def std(df):
    return square_root(var(df), precision=0.0001)

def min(df):
    min = df[0]
    for i in df[1:]:
        if min > i:
            min = i
    return min

def max(df):
    max = df[0]
    for i in df[1:]:
        if max < i:
            max = i
    return max

def first_quartile(df):
    df_non_nan = [x for x in df if not is_nan(x)]
    df_sorted = sorted(df_non_nan)
    index = 0.25 * len(df_sorted)
    if index == int(index):
        return df_sorted[int(index)]
    else:
        return (df_sorted[int(index)] + df_sorted[int(index) + 1]) / 2

def median(df):
    df_non_nan = [x for x in df if not is_nan(x)]
    df_sorted = sorted(df_non_nan)
    index = 0.5 * len(df_sorted)
    if index == int(index):
        return df_sorted[int(index)]
    else:
        return (df_sorted[int(index)] + df_sorted[int(index) + 1]) / 2


def third_quartile(df):
    df_non_nan = [x for x in df if not is_nan(x)]
    df_sorted = sorted(df_non_nan)
    index = 0.75 * len(df_sorted)
    if index == int(index):
        return df_sorted[int(index)]
    else:
        return (df_sorted[int(index)] + df_sorted[int(index) + 1]) / 2

