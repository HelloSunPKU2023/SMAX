from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline


# create a scikit-learn transformer to remove the title with less than 3 words or more than 20 words
class TitleLengthFilter(BaseEstimator, TransformerMixin):
    def __init__(self, min_words=0, max_words=999):
        self.min_words = min_words
        self.max_words = max_words
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        df = X.copy()
        df = df[df['Length'] >= self.min_words]
        df = df[df['Length'] <= self.max_words]
        df = df.reset_index(drop=True)
        return df

# create a scikit-learn transformer to combine the products which are not in the top_products list into one product
class OtherProductsCombiner(BaseEstimator, TransformerMixin):
    def __init__(self, top_products, target_col):
        self.top_products = top_products 
        self.target_col = target_col
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        df = X.copy()
        mask = ~df[self.target_col].isin(self.top_products)
        df.loc[mask, self.target_col]=f'Others Products (not in top {len(self.top_products)})'
        return df

# create a scikit-learn transformer to cap the number of samples for each product
class SampleCapper(BaseEstimator, TransformerMixin):
    def __init__(self, target_col, max_samples=None):
        self.max_samples = max_samples
        self.target_col = target_col
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        df = X.copy()
        if self.max_samples is None:
            return df
        counts = df[self.target_col].value_counts()
        over_sampled = counts.index[counts > self.max_samples]
        for item in over_sampled:
            size = len(df[df[self.target_col]==item])
            df = df.drop(df[df[self.target_col]==item].sample(frac=1-self.max_samples/size, random_state=42).index)
        return df

# create a scikit-learn transformer to lower case the text
class TextLower(BaseEstimator, TransformerMixin):
    def __init__(self, text_col):
        self.text_col = text_col
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        df = X.copy()
        df[self.text_col] = df[self.text_col].str.lower()
        return df
