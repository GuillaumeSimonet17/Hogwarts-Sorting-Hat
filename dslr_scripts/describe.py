import sys
import pandas as pd
import statistic_lib as st


def describe_dataset(df_numeric):
    titles = (df_numeric.columns[1:])
    labels = ['Count', 'Mean', 'Std', 'Min', '25%', '50%', '75%', 'Max']
    df_stats = pd.DataFrame(index=labels, columns=titles)

    for col in titles:
        df_stats.at['Count', col] = st.count(df_numeric[col])
        df_stats.at['Mean', col] = st.mean(df_numeric[col])
        df_stats.at['Std', col] = st.std(df_numeric[col])
        df_stats.at['Min', col] = st.min(df_numeric[col])
        df_stats.at['25%', col] = st.first_quartile(df_numeric[col])
        df_stats.at['50%', col] = st.median(df_numeric[col])
        df_stats.at['75%', col] = st.third_quartile(df_numeric[col])
        df_stats.at['Max', col] = st.max(df_numeric[col])

    print()
    print(df_stats)

def main(argv):
    df = pd.read_csv(argv)
    df_numeric = df.select_dtypes(include=['number'])
    describe_dataset(df_numeric)

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ValueError('Please, enter one file.')
        main(sys.argv[1])
    except ValueError as e:
        print(e)