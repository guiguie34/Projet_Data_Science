# lien de cet exemple anova : https://www.reneshbedre.com/blog/anova.html
import json
import numpy as np
import pandas as pd

# load data file
from statsmodels.stats.multicomp import pairwise_tukeyhsd

with open("Generated Data/dataForAnova5.json") as f:
    data = json.load(f)
    df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in data.items()]))
    #print(df.head(n=10))
    df = pd.melt(df,value_vars=list(df.columns),var_name='theme', value_name='time')

    #print(df.head(n=10))

# # reshape the d dataframe suitable for statsmodels package
# df_melt = pd.melt(df.reset_index(), id_vars=['index'], value_vars=df.item())
# # replace column names
# df_melt.columns = ['index', 'treatments', 'value']
#
# # generate a boxplot to see the data distribution by treatments. Using boxplot, we can
# # easily detect the differences between different treatments
import matplotlib.pyplot as plt
import seaborn as sns
# #

# # # load package
import scipy.stats as stats
#
# df.dropna(axis = 0, how = 'any')
# print(df)
df = df[df['time'].notna()]
for index, row in df.iterrows():
    df.at[index,'time'] = row["time"]/86400
time_filter = df['time']<182.5
df=df[time_filter]
df = df[df['theme'].map(df['theme'].value_counts()) > 100]

# number_filter= df['theme'].count()>3
# df=df[number_filter]
sns.barplot(data=df, x='theme', y='time')
plt.xticks(rotation=90)
plt.ylim(0, 50)
plt.title("Temps de réponse moyen pour les thèmes les plus fréquents (>100) issus des conversations",fontsize=9)
plt.ylabel("Temps (en jours)")
plt.show()

grouped_df = df.groupby("theme")
mean_df = grouped_df.mean()
mean_df = mean_df.reset_index()
print(mean_df)
#print(df.groupby(['theme'])['time'].mean().to_frame())
#print((df.groupby(['theme']).mean()).plot().bar(x='theme', y='time'))
# df.to_csv("Generated Data/dataForAnova6.csv",header=True,index=True)
# df.info()
#df[1] = df[1].astype('float', errors='ignore')
ax = sns.boxplot(x='theme', y='time', data=df, color='#99c2a2')
#ax = sns.swarmplot(x="theme", y="time", data=df, color='#7d0013')
plt.show()
#print(df)
# for i in df.index:
#     if np.isnan(df["time"][i]):
#         #print(df["time"][i])
#         np.delete(df,i,0)
    #print(df["theme"][i] + " " + str(df["time"][i]))
#print(df)
#data = [df[col].dropna() for col in df]
#data[1] = data[1].astype('int64', errors='ignore')
#print(data)
#
# f_val, p_val = stats.f_oneway(*df)
# print(p_val,f_val)
# # # stats f_oneway functions takes the groups as input and returns F and P-value
# fvalue, pvalue = stats.f_oneway(*df)
# print(fvalue, pvalue)
# # 17.492810457516338 2.639241146210922e-05
#
# # # get ANOVA table as R like output
import statsmodels.api as sm
from statsmodels.formula.api import ols
# # #
# # # # Ordinary Least Squares (OLS) model
model = ols('time ~ C(theme)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)

tukey = pairwise_tukeyhsd(endog=df['time'],
                          groups=df['theme'],
                          alpha=0.05)

# f = open("tukey_filter.txt", "w")
# f.write(str(tukey))
# f.close()
#display results
#print(tukey)


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