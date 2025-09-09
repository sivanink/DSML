import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics


df = pd.read_csv('csvfile2.csv') 


print(df.head())


print("Enter Sample Data:")
X = df[['Sweetness', 'Crunchiness']]
y = df['Type']  


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)


clf = GaussianNB()
clf.fit(X_train, y_train)


y_pred = clf.predict(X_test)
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))


a = float(input("Enter sweetness: "))
b = float(input("Enter crunchiness: "))

sample_df = pd.DataFrame([[a, b]], columns=['Sweetness', 'Crunchiness'])


pred = clf.predict(sample_df)
print("Predicted Type:", pred[0])

