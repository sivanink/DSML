import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics


df = pd.read_csv('csvfile2.csv') 


X = df[['Sweetness', 'Crunchiness']]
y = df['Type'] 


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)


knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)


y_pred = knn.predict(X_test)
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))


print("Enter Sample Data")
a = float(input("Enter sweetness:"))
b = float(input("Enter crunchiness:"))


sample_df = pd.DataFrame([[a, b]], columns=['Sweetness', 'Crunchiness'])
pred = knn.predict(sample_df)

print("Predicted Type:", pred[0])






