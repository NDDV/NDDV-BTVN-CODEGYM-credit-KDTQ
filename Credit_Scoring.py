#%%
import matplotlib.pyplot as plt
import pandas as pd
import scipy 
import seaborn as sns

#%%
df = pd.read_csv("Credit_Scoring.csv")
df

# %%
df_1 = df[['age','MonthlyIncome']]
df_1 = df_1.dropna()
df_1.sort_values(by=['age'])
df_1
#%%
plt.plot(df_1['MonthlyIncome'],df_1['age'], linewidth = 2, marker = '*', markersize=2, markerfacecolor='red', markeredgecolor = 'blue', markeredgewidth=2)
plt.show()
# %%
r, p = scipy.stats.pearsonr(df_1.MonthlyIncome,df_1.age)
print("r =", r, "p =", p)

# %%
print("Nhận xét: Do pvalue << 0, và hệ số tương quan ~0 nên giữa độ tuổi và thu nhập trung bình theo tháng có mối tương quan không chặt chẽ với nhau")
# %%
df_2 = df[['age','NumberOfOpenCreditLinesAndLoans']]
df_2 = df_2.dropna()
df_2.sort_values(by=['age'])
df_2
#%%
plt.plot(df_2['NumberOfOpenCreditLinesAndLoans'],df_2['age'], linewidth = 2, marker = '*', markersize=2, markerfacecolor='red', markeredgecolor = 'blue', markeredgewidth=2)
plt.show()
# %%
r, p = scipy.stats.pearsonr(df_2.NumberOfOpenCreditLinesAndLoans,df_2.age)
print("r =", r, "p =", p)

# %%
print("Nhận xét: Do pvalue = 0, và hệ số tương quan =0.1 nên giữa giá nhà và diện tích có tương quan với nhau")
# %%
df_3 = df[['NumberOfDependents','MonthlyIncome']]
df_3 = df_3.dropna()
df_3.sort_values(by=['NumberOfDependents'])
df_3
#%%
plt.plot(df_3['MonthlyIncome'],df_3['NumberOfDependents'], linewidth = 2, marker = '*', markersize=2, markerfacecolor='red', markeredgecolor = 'blue', markeredgewidth=2)
plt.show()
# %%
r, p = scipy.stats.pearsonr(df_3.NumberOfDependents ,df_3.NumberOfDependents )
print("r =", r, "p =", p)

# %%
print("Nhận xét: Do pvalue 0 0, và hệ số tương quan = 1 nên giữa số lượng người phụ thuộc và thu nhập trung bình theo tháng có mối tương quan chặt chẽ với nhau")
