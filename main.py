import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
unique_values = data['whoAmI'].unique()

for value in unique_values:
    data[f'whoAmI_{value}'] = (data['whoAmI'] == value).astype(int)

data = data.drop('whoAmI', axis=1)
data.head()