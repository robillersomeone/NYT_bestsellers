# New York Times Best Sellers

## Goal

To predict a New York Times Best Seller using natural language processing and publishing features.

## Structure
- [Data](#Data)
- [EDA](#EDA)
- [Text Feature Engineering](#Text-Feature-Engineering)
- [Modeling](#Modeling)


## <a name="Data"></a>Data

The initial dataset is from Goodreads list of Goodreads choice awards of best fiction books in 2016, 2017, 2018 and list of NYT notable books from 2016, 2017, and 2018.

Publishing features include
- author
- number of pages
- genre
- format

Other data collected
- Goodreads rating (user generated)
- book description

## <a name="EDA"></a>EDA

The books were categorized as a binary on the New York Times Best Seller list or not.
Goodreads is user driven, with metadata about the books, a short description, and ratings and comments from users.

The mean rating for books on the Best Seller list is slightly lower than those not on the list.

<img width="600" height="450" alt="Screen Shot 2019-03-18 at 4 22 52 PM" src="https://user-images.githubusercontent.com/39356742/54561159-5ddbfc00-499a-11e9-9180-9ca78da33443.png">


Best Sellering Books mean rating **3.92 out of 5**.

Non-Best Selling Books mean rating **4.09 out of 5**.

**Nonfiction** and **Fiction** are most prevalent genres, with only 21 of the 33 total genres appear in the Best Seller list.

<img width="675" height="450" alt="Screen Shot 2020-02-17 at 4 37 55 PM" src="https://user-images.githubusercontent.com/39356742/74688056-49087980-51a4-11ea-9a59-a022a76557fe.png">


<img width="675" height="450" alt="Screen Shot 2020-02-17 at 4 38 05 PM" src="https://user-images.githubusercontent.com/39356742/74688198-c8964880-51a4-11ea-90f8-40011d9f77a3.png">


Genres that don't appear on the NYT Best Seller list include

 >'New Adult', 'Contemporary', 'Science Fiction', 'Childrens', 'Food and Drink', 'Humor', 'Thriller', 'Polyamorous', 'Media Tie In', 'Paranormal', 'Dark', 'Business', 'Religion', 'Christian', 'Sports and Games'

 There are 955 unique authors of 1098 books, with most authors (844) having one book. Sarah j. Maas and Stephen King are the most prolific, both with 6 books.

## <a name="Text-Feature-Engineering"></a> Text Feature Engineering

Using Natural Language Toolkit the book descriptions were pre-processed then lemmatized with the NLTK implementation of the Word Net Lemmatizer.

Custom stop words are included to prevent data leakage in the description. Specifically words relating to NYT Best Seller list.

There are two scripts to process the text data.

```shell
text_feature_engineering_helper.py
```

Does preprocessing, taking out HTML tags, numbers, punctuation, and uppercase.

```shell
text_feature_engineering.py
```
Implements the lemmatizer and removes stop words.


The scikit learn `CountVectorizer` produced the sparse text matrix for modeling.

After cleaning the text the most common words in the description are

<img width="675" height="450" alt="Screen Shot 2020-02-26 at 2 59 01 PM" src="https://user-images.githubusercontent.com/39356742/75382611-ccaf1e00-58a8-11ea-9e7d-c9ca92980bcd.png">


## <a name="Modeling"></a> Modeling

Two initial models are implemented

- A Numerical model with the number of pages and Goodeads rating of each book
- A text model with the vectorized book descriptions

### Baseline Modeling

The numerial baseline model the scikit-learn implementation a Dummy Classifier solved with `strategy= 'stratified’` highlighting the class balance in the dataset.

with a `mean training accuracy of 0.66`


<img width="350" alt="Screen Shot 2020-02-17 at 5 20 11 PM" src="https://user-images.githubusercontent.com/39356742/74690173-f92db080-51ab-11ea-985c-5428a7099103.png">

The confusion matrix for the test set is

<img width="350" alt="Screen Shot 2020-02-21 at 10 52 39 AM" src="https://user-images.githubusercontent.com/39356742/75049587-7dc44b80-5498-11ea-949b-31c333316e10.png">

Due to the class balance of the data set only 17 samples are correctly classified as Best Sellers, the `mean training accuracy is 0.66` as well.

### Random Forest

Numerical Model performance on the test set with the default parameters of the scikit-learn random forest.

`crterion='gini'`

`max_leaf_nodes` , `max_samples` , and `min_impurity_split` are all set to `None`

With a  `mean testing accuracy of 0.77`

<img width="350" alt="Screen Shot 2020-02-19 at 4 30 59 PM" src="https://user-images.githubusercontent.com/39356742/74878514-7cc6d900-5335-11ea-85d3-8d9e7a57395a.png">

Text Modeling performance on the test set with the default parameters of the scikit-learn random forest.

`crterion='gini'`

`max_leaf_nodes` , `max_samples` , and `min_impurity_split` are all set to `None`

With a `mean testing accuracy of 0.81`

<img width="350" alt="Screen Shot 2020-02-19 at 4 31 15 PM" src="https://user-images.githubusercontent.com/39356742/74878488-70428080-5335-11ea-89d4-41b93804a108.png">

#### Random search

Using random search the mean testing accuracy performs the same as the initial text random forest model with a different distribution of misclassified instances.

The hyperparameters found using random search are

`criterion='entropy'`

`n_estimators=240`

`max_features='log2'`

`criterion='entropy'`

With a `mean testing accuracy of 0.81`

<img width="350" alt="Screen Shot 2020-02-24 at 4 16 30 PM" src="https://user-images.githubusercontent.com/39356742/75192792-f8080080-5722-11ea-9220-ce2d8ded745d.png">

### Predictions

To classify a book call the `modeling.py` script from the command line with a description of a book in string format.

```shell
$ python modeling.py 'The full inside story of the breathtaking rise and shocking collapse of Theranos, \
 the multibillion-dollar biotech startup, by the prize-winning journalist who first broke the story and pursued it to the end, \
  despite pressure from its charismatic CEO and threats by her lawyers. '

Bestseller
```
The model classifies the first paragraph the description of "Bad Blood: Secrets and Lies in a Silicon Valley Startup" by John Carreyrou as a NYT bestseller.

An important note is that most descriptions will be classified and not bestsellers (even when they are on the besteller list), this is due to the training data and current model used in classification, a RandomForestClassifier trained only on book descriptions.

## Next Steps

Compare the feature weights in logistic and tree based models.
