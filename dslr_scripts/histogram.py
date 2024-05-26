import matplotlib
matplotlib.use('TkAgg')

import sys
import statistic_lib as st
import pandas as pd
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

    df_numeric = scale(df.select_dtypes(include=['number']))

    slytherin = df_numeric[df['Hogwarts House'] == 'Slytherin']
    ravenclaw = df_numeric[df['Hogwarts House'] == 'Ravenclaw']
    gryffindor = df_numeric[df['Hogwarts House'] == 'Gryffindor']
    hufflepuff = df_numeric[df['Hogwarts House'] == 'Hufflepuff']
    
    courses = df_numeric.drop(columns=['Index']).columns
    fig, axes = plt.subplots(nrows=int(len(courses)/3)+1, ncols=3, figsize=(12, 6*len(courses)), sharex=False)
    plt.subplots_adjust(hspace=0.5)

    homogeneous_courses = []

    for i, course in enumerate(courses):

        data = [slytherin[course], ravenclaw[course], gryffindor[course], hufflepuff[course]]
        labels = ['Slytherin', 'Ravenclaw', 'Gryffindor', 'Hufflepuff']
        colors = ['green', 'blue', 'red', 'yellow']

        if abs((slytherin[course].std() - df_numeric[course].std())) < 0.2 and \
            abs((ravenclaw[course].std() - df_numeric[course].std())) < 0.2 and \
            abs((gryffindor[course].std() - df_numeric[course].std())) < 0.2 and \
            abs((hufflepuff[course].std() - df_numeric[course].std())) < 0.2:
            homogeneous_courses.append(course)

        ax = axes[i // 3, i % 3]
        ax.hist(data, bins=10, label=labels, color=colors)
        ax.set_title(course)

        if i == 0:
            ax.legend()
    
    if len(homogeneous_courses) == 1:
        print(f'{homogeneous_courses} is a course who has a homogeneous score distribution between all four houses')
    if len(homogeneous_courses) == 0:
        print('No courses has a score distribution homogeneous between all four houses')
    if len(homogeneous_courses) > 1:
        print('The courses who has a homogeneous score distribution between all four houses are :')
        for course in homogeneous_courses:
            print('- ', course)

    fig.text(0.5, 0.04, 'Notes', ha='center', va='center')
    fig.text(0.06, 0.5, 'Nombre d\'élèves', ha='center', va='center', rotation='vertical')

    plt.show()

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ValueError('Please, enter one file.')
        main(sys.argv[1])
    except ValueError as e:
        print(e)