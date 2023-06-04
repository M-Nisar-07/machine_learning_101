import pandas as pd
from sklearn.tree import DecisionTreeClassifier

music_data = pd.read_excel('music.xlsx')

y = music_data["genre"]

x = music_data.drop(columns = "genre")

model = DecisionTreeClassifier()

model.fit(x,y)
predictions = model.predict([ [2,1] , [22,0] ])

print(predictions)
