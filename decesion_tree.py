import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

from sklearn import tree

music_data = pd.read_excel('music.xlsx')

y = music_data["genre"]

x = music_data.drop(columns = "genre")

model = DecisionTreeClassifier()

model.fit(x,y)

tree.export_graphviz(model, out_file = 'music-reommender.dot', feature_names = ['age', 'gender'],
                     class_names = sorted(y.unique()),
                     label = 'all', rounded = True, filled = True )

 # install dot (graphviz(dot) language support)
