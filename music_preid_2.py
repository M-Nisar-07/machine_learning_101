import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

music_data = pd.read_excel('musicc.xlsx')

y = music_data["genre"]

x = music_data.drop(columns = "genre")

x_train , x_test , y_train, y_test  = train_test_split(x,y, test_size = 0.8)

model = DecisionTreeClassifier()

model.fit(x_train,y_train)

predictions = model.predict(x_test)

score = accuracy_score(y_test,predictions)
print(predictions , score)
