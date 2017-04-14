import pandas as pd

dataset = pd.read_csv('beer_reviews/beer_reviews.csv')
size, features = dataset.shape

print("\nEl dataset completo consta de {} registros y {} caracteristicas.".format(size, features))
ls
dataset.all
dataset.drop('brewery_id', 1, inplace=True)
dataset.drop('brewery_name', 1, inplace=True)
dataset.drop('review_time', 1, inplace=True)
dataset.drop('review_profilename', 1, inplace=True)
dataset.drop('beer_style', 1, inplace=True)
dataset.drop('beer_name', 1, inplace=True)
dataset.drop('beer_beerid', 1, inplace=True)
import pandas as pd

dataset = pd.read_csv('beer_reviews/beer_reviews.csv')
size, features = dataset.shape

print("\nEl dataset completo consta de {} registros y {} caracteristicas.".format(size, features))
dataset
dataset.info()
dataset.beer_style
dataset.beer_style.consolidate
dataset.beer_style.unique()
len(dataset.beer_style.unique())
dataset.info()
len(dataset.brewery_name.unique())
dataset.info()
len(dataset.beer_name.unique())
dataset.beer_name.unique()
dataset
dataset
type(dataset)
dataset.beer_style.unique()
dataset.groupby('beer_style')
dataset.groupby('beer_style').unique()
dataset.beer_name.unique()
dataset.beer_name.unique()
dataset.beer_style()
dataset.beer_style.unique()
dataset.groupby('beer_style')['beer_style'].count()
dataset.groupby('beer_style')['beer_style'].count()
styles = dataset.groupby('beer_style')['beer_style'].count()
type(styles)
styles.sort()
styles.sort_values()
styles.sort_values()
styles.sort_values(inplace=True)
styles
styles[:-5]
styles[1:2]
styles[:-5]
styles
styles[-5:]
styles[-5:]
styles[-10:]
top_styles = list(styles[-10:])
top_styles
top_styles = styles[-10:]
top_styles
top_styles.to_dict
top_styles.to_dict()
top_styles.to_dict().keys()
top_styles = list(top_styles.to_dict().keys())
top_styles
dataset['beer_style']
top_styles
dataset['beer_style'].isin(top_styles)
dataset[dataset['beer_style'].isin(top_styles)]
top_styles = styles[-5:]
top_styles = list(top_styles.to_dict().keys())
dataset[dataset['beer_style'].isin(top_styles)]
sample = dataset[dataset['beer_style'].isin(top_styles)]
sample
sample.fillna()
sample.fillna(0, inplace=True)
sample.fillna(0)
sample = sample.fillna(0)
sample
sample.to_csv("sample.csv", sep='\t', encoding='utf-8')
sample.to_csv("sample.csv", sep=',', encoding='utf-8')
sample
dataset[dataset['beer_style'].isin(top_styles)]
beer_brands = dataset.groupby('beer_style')['beer_style'].count()
sample.info
sample.info()
beer_brands = sample.groupby('brewery_name')['brewery_name'].count()
beer_brands
beer_brands.order()
beer_brands.order()[:-20]
beer_brands.order()[-20:]
top_brands = beer_brands.order()[-20:]
top_brands = beer_brands.sort_values()[-20:]
top_brands
top_brands.to_dict
top_brands.to_dict.values
top_brands.to_dict
top_brands.to_dict().values
top_brands.to_dict().values()
sum(top_brands.to_dict().values())
sum(top_brands.to_dict().values())
top_brands = beer_brands.sort_values()[-10:]
sum(top_brands.to_dict().values())
top_brands = top_brands.to_dict().values()
top_brands
top_brands = list(top_brands)
ls
top_brands
sample = dataset[dataset['beer_style'].isin(top_styles)]
top_brands = top_brands.to_dict().keys()
top_brands = beer_brands.sort_values()[-10:]
top_brands = top_brands.to_dict().keys()
top_brands = list(top_brands)
top_brands
sample.info()
sample2 = dataset[dataset['brewery_name'].isin(top_brands)]
sample2.info()
sample2 = sample[sample['brewery_name'].isin(top_brands)]
sample2.info()
sample2.to_csv("sample2.csv", sep=',', encoding='utf-8')

