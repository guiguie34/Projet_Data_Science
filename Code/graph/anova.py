# lien de cet exemple anova : https://www.reneshbedre.com/blog/anova.html
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


def load_data():
    # load data file
    with open("../../Generated Data/dataForAnova5.json") as f:
        data = json.load(f)
        df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in data.items()]))
        df = pd.melt(df, value_vars=list(df.columns), var_name='theme', value_name='time')
        df = df[df['time'].notna()]
    return df

def box_plot(df,n=None):
    if n != None:
        df = df.head(n=10)
    return px.box(df, x='theme', y='time')


plt.show()

import statsmodels.api as sm
from statsmodels.formula.api import ols

# # #
# # # # Ordinary Least Squares (OLS) model
# model = ols('time ~ C(theme)', data=df).fit()
# anova_table = sm.stats.anova_lm(model, typ=2)
# print(anova_table)

# from scipy.stats import bartlett
# #print(df.groupby('theme').count())
# tuk = {}
# for index, row in df.iterrows():
#     if row["theme"] not in tuk:
#         tuk[row["theme"]]= list()
#     tuk[row["theme"]].append(row["time"])
#
# tuk2=[]
# for k,v in tuk.items():
#     tuk2.append(v)
#
# #print(tuk2)
# print([x for x in tuk2])
# stat, p = bartlett(tuk2[0],tuk2[1])
# print(p)
# # ANOVA table using bioinfokit v1.0.3 or later (it uses wrapper script for anova_lm)
# from bioinfokit.analys import stat
#
# res = stat()
# res.anova_stat(df=df_melt, res_var='value', anova_model='value ~ C(treatments)')
# print(res.anova_summary)
#
#
# # note: if the data is balanced (equal sample size for each group), Type 1, 2, and 3 sums of squares
# # (typ parameter) will produce similar results.
#
# # QQ-plot
# import statsmodels.api as sm
# import matplotlib.pyplot as plt
# # res.anova_std_residuals are standardized residuals obtained from ANOVA (check above)
# sm.qqplot(res.anova_std_residuals, line='45')
# plt.xlabel("Theoretical Quantiles")
# plt.ylabel("Standardized Residuals")
# plt.show()
#
# # histogram
# plt.hist(res.anova_model_out.resid, bins='auto', histtype='bar', ec='k')
# plt.xlabel("Residuals")
# plt.ylabel('Frequency')
# plt.show()