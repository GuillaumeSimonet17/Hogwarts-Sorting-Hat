import matplotlib
matplotlib.use('TkAgg')

import sys
import pandas as pd
import numpy as np
import statistic_lib as st
import matplotlib.pyplot as plt


def scale(df):
    titles = df.columns[1:]
    for col in titles:
        arr = df[col]
        X_std = st.std(arr)
        mean_X = st.mean(arr)
        if X_std != 0:
            scaled_X = (arr - mean_X) / X_std
        df[col] = scaled_X
    return df

def main(argv):
    df = pd.read_csv(argv)

    df_numeric = scale(df.select_dtypes(include=['number']).drop(columns=['Index']).dropna())

    corr_course = []

    for col_a in df_numeric:
        A = df_numeric[col_a]
        for col_b in df_numeric:
            if col_a != col_b:
                B = df_numeric[col_b]
                X = df_numeric[col_a] - st.mean(df_numeric[col_a])
                Y = df_numeric[col_b] - st.mean(df_numeric[col_b])
                cov = np.dot(X, Y) / len(df_numeric[col_a])
                corr = cov / ((st.std(df_numeric[col_a]) * st.std(df_numeric[col_b])))
                if abs(corr) >= 0.98:
                    if col_a not in corr_course:
                        corr_course.append(col_a)
                        corr_course.append(col_b)
    print('The courses that are similar are :')
    print(corr_course[0], end=' and ')
    print(corr_course[1])

    plt.scatter(df_numeric[corr_course[0]], df_numeric[corr_course[1]])
    plt.xlabel(corr_course[0])
    plt.ylabel(corr_course[1])

    plt.show()

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ValueError('Please, enter one file.')
        main(sys.argv[1])
    except ValueError as e:
        print(e)