import pandas as pd
# df = pd.read_csv("diabetes_dataset.csv")
df = pd.read_csv("https://raw.githubusercontent.com/ardianff/Alpro-RMIK/master/Pertemuan%2014%20-%2015/diabetes_dataset.csv")
# print(df.head())

x = df.drop(['Outcome'], axis=1)
# print(x)

y = df.Outcome
# print(y)

from sklearn.tree import DecisionTreeClassifier #mengimport rumus klasifikasi menggunakan decision tree
from sklearn.model_selection import train_test_split # fungsi untuk mengsplit data
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state =1)

# membuat object decision tree
model = DecisionTreeClassifier()
# train data decision trree
model = model.fit(x_train,y_train)
# prediksi respon dari data testing
y_pred = model.predict(x_test)

# evaluasi skor akurasi data
from sklearn import metrics #modul untuk mencari akurasi
print("Akurasi : ", metrics.accuracy_score(y_test, y_pred)*100)

# evaluasi menggunakan confussion matrix
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_pred))

print("Akurasi : ", ((81+28)/81+28+27+18))

# evaluasi klasifikasi menggunakan nilai report
from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))

features = x.columns
# print(features)


#Import modules for Visualizing Decision trees
from sklearn.tree import export_graphviz
from six import StringIO 
from IPython.display import Image  
import pydotplus

dot_data = StringIO()
export_graphviz(model, out_file=dot_data,filled=True, rounded=True,special_characters=True,feature_names = features,class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('diabetes_set_export.png')
Image(graph.create_png())