import sys
import pandas as pd
from sklearn import linear_model

if __name__ == '__main__':
    timeCharged = float(input().strip())

    dataset = pd.read_csv('trainingdata.txt', header=None)
    dataset = dataset[dataset.iloc[:,1] < 8]

    dataset.insert(0, len(dataset.columns), 0)

    X = dataset.iloc[:,0:2]
    Y = dataset.iloc[:,2]

    model = linear_model.LinearRegression()
    model.fit(X, Y)
    
    result = model.predict([[0, timeCharged]])
    if result[0] > 8:
        print (8.0)
    else:
        print (round(result[0],2))
