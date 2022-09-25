import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt


class Manipulation:
    @staticmethod
    def counter(z, sep, delm):
        try:
            sv = []
            for i in z:
                for i in i.split(sep):
                    if i not in delm:
                        sv.append(i)
            return dict(sorted(dict(Counter(sv)).items(), key=lambda item: item[1], reverse=True))
        except Exception as e:
            print("ERROR : " + str(e))

    @staticmethod
    def getDigits(z):
        try:
            x = ''
            if type(z) == str:
                for i in z:
                    if i.isdigit():
                        x += i
                return int(x)
            elif type(z) == list:
                print(z, 'list')
                for i in z[0]:
                    if i.isdigit():
                        x += i
                return int(x)
            else:
                return np.nan
        except Exception as e:
            print("ERROR : " + str(e))


class Describe:
    @staticmethod
    def describeDf(a):
        try:
            df = pd.read_excel(a)
            print(df.info())
            print(df.describe())
            return df
        except Exception as e:
            print("ERROR : " + str(e))

    @staticmethod
    def allUnique(df,selected):
        for i in selected:
            print(i)
            print(df[i].unique())
            print("*" * 80)


class FeatureEngineering:
    @staticmethod
    def binary_encoding(Series, keywords):
        binarySeries = []
        try:
            if Series == np.nan:
                return pd.Series([np.nan for i in keywords])
            for i in keywords:
                if i in Series:
                    binarySeries.append(1)
                else:
                    binarySeries.append(0)
            return pd.Series(binarySeries)
        except Exception as e:
            print(e)
            binarySeries = [np.nan for i in keywords]
            return pd.Series(binarySeries)

    @staticmethod
    def CatOutLiers(df, cols, count):
        retCols = dict()
        try:
            for i in cols:
                cat_outliers = []
                for k, v in df[i].value_counts().items():
                    if v <= count:
                        cat_outliers.append(k)
                    retCols.update({i: df[df[i].isin(cat_outliers)].index})
            return retCols
        except Exception as e:
            print(e)


class Visualization:
    @staticmethod
    def printOutlier(df,col):
        from seaborn import boxplot
        from seaborn import stripplot
        from seaborn import distplot
        # fig, axs = plt.subplots(1, 1, sharey=True)
        boxplot(data=df, x=col)
        stripplot(data=df, x=col)
        plt.show()
        distplot(df['Price'])


    @staticmethod
    def catsCount(catgoricalColumns, df):
        try:
            from seaborn import countplot
            for i in catgoricalColumns[4:]:
                temp_series = df[i].value_counts(normalize=True)
                print(temp_series)
                countplot(x=i, data=df)
                plt.show()
        except Exception as e:
            print(e)

    @staticmethod
    def catsStatistics(df,catgorical_columns,col):
        from seaborn import boxplot
        from seaborn import violinplot

        for column_name in catgorical_columns:
            print('=' * 80)

            fig, axs = plt.subplots(1, 2, sharey=True)
            boxplot(data=df, x=col, y=column_name, ax=axs[0])
            violinplot(data=df, x=col, y=column_name, ax=axs[1])
            plt.show()

            means = df.groupby(column_name)[col].mean()
            medians = df.groupby(column_name)[col].median()

            statsicates = pd.DataFrame()
            statsicates['Mean'] = means
            statsicates['Median'] = medians
            statsicates[['Mean', 'Median']] = statsicates[['Mean', 'Median']].astype(int)
            print(statsicates)
