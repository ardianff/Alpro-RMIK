import numpy as np 
# pip install numpy
import pandas as pd 
# pip install pandas
import seaborn as sns
# pip install seaborn
import matplotlib.pyplot as plt
# pip install matplotlib

cases = pd.read_csv("Covid/cases.csv")
confirmed_acc = pd.read_csv("Covid/confirmed_acc.csv")
keywordtrend = pd.read_csv("Covid/keywordtrend.csv")
patient = pd.read_csv("Covid/patient.csv")

# menampilkan 5 data teratas
print(patient.head())
# menampilkan 5 data terbawah
print(cases.tail())

# grafik distribusi usia yang terkonfirmasi
plt.figure(figsize=(10,6))
sns.set_style("darkgrid")
plt.title("Age distribution of the confirmed")
sns.kdeplot(data=patient['age'], fill=True)

plt.figure(figsize=(10,40))
plt.title('Number patients in province')
patient.province.value_counts().plot.bar();


plt.show()
