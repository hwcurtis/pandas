import pandas as pd
mydataset = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

mydataset = {
    'cars': ['Ford', 'Volvo', 'BMW'],
    'passings': [3, 7, 2], }

myvar = pandas.Dataframe(mydataset)

print(myvar)
print(mydataset)
