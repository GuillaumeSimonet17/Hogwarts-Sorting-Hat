import matplotlib
matplotlib.use('TkAgg')

import sys
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt


def main(argv):
    df = pd.read_csv(argv)
    df_numeric = df.select_dtypes(include=['number']).drop(columns='Index')

    # sn.pairplot(df_numeric)

    # sn.pairplot(df_numeric.iloc[:, 1:5])
    # sn.pairplot(df_numeric.iloc[:, 5:9])
    # sn.pairplot(df_numeric.iloc[:, 9:14])
    
    # plt.show()

    print('We\'re gonna use all of courses but :')
    print('- Care of Magical Creatures')
    print('- Potions')
    print('- Arithmancy')
    print('- Astronomy')

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ValueError('Please, enter one file.')
        main(sys.argv[1])
    except ValueError as e:
        print(e)