import pandas as pd
import numpy as np


# df_rates = pd.DataFrame({"Year0":[0.06,0.06,0.06,0.06,0.06],
#                     "Year1":[0.07,0.05,0.06,0.05,0.09],
#                     "Year2":[0.08,0.03,0.07,0.05,0.13],
#                     "Year3":[0.06,0.02,0.07,0.04,0.10],
#                     "Year4":[0.07,0.05,0.08,0.04,0.09],
#                     "Year5":[0.08,0.04,0.08,0.05,0.10]})



df_rates = pd.DataFrame({"Year0":[0.0450,0.0450,0.0450,0.0450,0.0450,0.0450,0.0450,0.0450,0.0450,0.0450],
                    "Year1":[0.0516,0.0998,0.0415,0.0399,0.0196,0.0442,0.0995,0.0387,0.0547,0.0582],
                    "Year2":[0.0601,0.0964,0.0865,0.0264,0.0107,0.0445,0.1183,0.0445,0.0543,0.0551],
                    "Year3":[0.0713,0.0991,0.0840,0.0366,0.0014,0.0450,0.0783,0.0452,0.0564,0.0607],
                    "Year4":[0.0707,0.0642,0.1155,0.0378,0.0014,0.0397,0.1145,0.0491,0.0483,0.0587],
                    "Year5":[0.0737,0.0343,0.1031,0.0595,0.0049,0.0316,0.0674,0.0424,0.0502,0.0620]})

# df=df_rates.copy()
# sec='cap'
def calc_price(df, sec, strike_price):
    df_copy = df.copy()

    for i in df_copy.columns:
        if (sec == 'cap'):
            df_copy[i] = np.where(df_copy[i]-strike_price>0,df_copy[i]-strike_price,0)
        else:
            df_copy[i] = np.where(df_copy[i]-strike_price<0,strike_price-df_copy[i],0)
        

    df_copy = df_copy[['Year1','Year2','Year3','Year4']]
    df_copy.columns = ['Year2','Year3','Year4','Year5']



    df_trans = df.transpose()
    for i in df_trans.columns:
        df_trans[i] = df_trans[i].expanding().mean()

    df_avg = df_trans.transpose()
   
    # print("*********")
    # print(df_avg)
    
    # print(df_avg)
    for j in df_copy.columns:
        df_copy["PV_"+j] = (df_copy[j]*100)/np.exp(df_avg[j]*int(j[-1]))

    df_copy['sum']=df_copy[['PV_Year2','PV_Year3','PV_Year4','PV_Year5']].sum(axis=1)
    price = df_copy['sum'].mean()
    # print(df_copy)
    # print(df)
    # print(df_copy)
    return price


# 2.
strike_price = 0.033
print("##")
print("q2: cap 0.033")
print(calc_price(df_rates, 'cap', strike_price))
# print(df_rates)
# 3.
df_rates = pd.DataFrame({"Year0":[0.0450,0.0450,0.0450,0.0450,0.0450,0.0450,0.0450,0.0450,0.0450,0.0450],
                    "Year1":[0.0516,0.0998,0.0415,0.0399,0.0196,0.0442,0.0995,0.0387,0.0547,0.0582],
                    "Year2":[0.0601,0.0964,0.0865,0.0264,0.0107,0.0445,0.1183,0.0445,0.0543,0.0551],
                    "Year3":[0.0713,0.0991,0.0840,0.0366,0.0014,0.0450,0.0783,0.0452,0.0564,0.0607],
                    "Year4":[0.0707,0.0642,0.1155,0.0378,0.0014,0.0397,0.1145,0.0491,0.0483,0.0587],
                    "Year5":[0.0737,0.0343,0.1031,0.0595,0.0049,0.0316,0.0674,0.0424,0.0502,0.0620]})

strike_price = 0.044
print("##")
print("q3: floor 0.044")
print(calc_price(df_rates, 'floor', strike_price))

# 4.
df_rates = pd.DataFrame({"Year0":[0.0450,0.0450,0.0450,0.0450,0.0450,0.0450,0.0450,0.0450,0.0450,0.0450],
                    "Year1":[0.0516,0.0998,0.0415,0.0399,0.0196,0.0442,0.0995,0.0387,0.0547,0.0582],
                    "Year2":[0.0601,0.0964,0.0865,0.0264,0.0107,0.0445,0.1183,0.0445,0.0543,0.0551],
                    "Year3":[0.0713,0.0991,0.0840,0.0366,0.0014,0.0450,0.0783,0.0452,0.0564,0.0607],
                    "Year4":[0.0707,0.0642,0.1155,0.0378,0.0014,0.0397,0.1145,0.0491,0.0483,0.0587],
                    "Year5":[0.0737,0.0343,0.1031,0.0595,0.0049,0.0316,0.0674,0.0424,0.0502,0.0620]})

strike_price = 0.035
print("##")
print("q4: cap 0.035, floor 0.035")
print(calc_price(df_rates, 'cap', strike_price))

df_rates = pd.DataFrame({"Year0":[0.0450,0.0450,0.0450,0.0450,0.0450,0.0450,0.0450,0.0450,0.0450,0.0450],
                    "Year1":[0.0516,0.0998,0.0415,0.0399,0.0196,0.0442,0.0995,0.0387,0.0547,0.0582],
                    "Year2":[0.0601,0.0964,0.0865,0.0264,0.0107,0.0445,0.1183,0.0445,0.0543,0.0551],
                    "Year3":[0.0713,0.0991,0.0840,0.0366,0.0014,0.0450,0.0783,0.0452,0.0564,0.0607],
                    "Year4":[0.0707,0.0642,0.1155,0.0378,0.0014,0.0397,0.1145,0.0491,0.0483,0.0587],
                    "Year5":[0.0737,0.0343,0.1031,0.0595,0.0049,0.0316,0.0674,0.0424,0.0502,0.0620]})

strike_price = 0.035
print(calc_price(df_rates, 'floor', strike_price))


# 5.
df_rates = pd.DataFrame({"Year0":[0.0450,0.0450,0.0450,0.0450,0.0450,0.0450,0.0450,0.0450,0.0450,0.0450],
                    "Year1":[0.0516,0.0998,0.0415,0.0399,0.0196,0.0442,0.0995,0.0387,0.0547,0.0582],
                    "Year2":[0.0601,0.0964,0.0865,0.0264,0.0107,0.0445,0.1183,0.0445,0.0543,0.0551],
                    "Year3":[0.0713,0.0991,0.0840,0.0366,0.0014,0.0450,0.0783,0.0452,0.0564,0.0607],
                    "Year4":[0.0707,0.0642,0.1155,0.0378,0.0014,0.0397,0.1145,0.0491,0.0483,0.0587],
                    "Year5":[0.0737,0.0343,0.1031,0.0595,0.0049,0.0316,0.0674,0.0424,0.0502,0.0620]})

strike_price = 0.035
print("##")
print("q5: cap 0.035, cap avg 0.035")
print(calc_price(df_rates, 'cap', strike_price))


df_rates = pd.DataFrame({"Year0":[0.0450,0.0450,0.0450,0.0450,0.0450,0.0450,0.0450,0.0450,0.0450,0.0450],
                    "Year1":[0.0516,0.0998,0.0415,0.0399,0.0196,0.0442,0.0995,0.0387,0.0547,0.0582],
                    "Year2":[0.0601,0.0964,0.0865,0.0264,0.0107,0.0445,0.1183,0.0445,0.0543,0.0551],
                    "Year3":[0.0713,0.0991,0.0840,0.0366,0.0014,0.0450,0.0783,0.0452,0.0564,0.0607],
                    "Year4":[0.0707,0.0642,0.1155,0.0378,0.0014,0.0397,0.1145,0.0491,0.0483,0.0587],
                    "Year5":[0.0737,0.0343,0.1031,0.0595,0.0049,0.0316,0.0674,0.0424,0.0502,0.0620]})

strike_price = 0.035
df_avg_s = df_rates[['Year0','Year1','Year2','Year3','Year4','Year5']]
df_trans = df_avg_s.transpose()
for i in df_trans.columns:
    df_trans[i] = df_trans[i].expanding().mean()

df_avg = df_trans.transpose()


for i in df_avg.columns:
        df_avg[i+"_payoff"] = np.where(df_avg[i]-strike_price>0,df_avg[i]-strike_price,0)


df_payoff = df_avg[['Year1_payoff','Year2_payoff','Year3_payoff','Year4_payoff']]
df_payoff.columns = ['Year2','Year3','Year4','Year5']


for j in ['Year2','Year3','Year4','Year5']:
    df_avg["PV_"+j] = (df_payoff[j]*100)/np.exp(df_avg[j]*int(j[-1]))

df_avg['sum']=df_avg[['PV_Year2','PV_Year3','PV_Year4','PV_Year5']].sum(axis=1)
price = df_avg['sum'].mean()
print(price)


