# New York Times Best Sellers

## Goal

To predict a New York Times Best Sellers using natural language processing and publishing features.

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

<img width="350" alt="Screen Shot 2019-03-18 at 4 22 52 PM" src="https://user-images.githubusercontent.com/39356742/54561159-5ddbfc00-499a-11e9-9180-9ca78da33443.png">


Best Sellering Books mean rating **3.92 out of 5**.

Non-Best Selling Books mean rating **4.09 out of 5**.

**Nonfiction** and **Fiction** are most prevalent genres, with only 21 of the 33 total genres appear in the Best Seller list.

<img width="450" alt="Screen Shot 2020-02-17 at 4 37 55 PM" src="https://user-images.githubusercontent.com/39356742/74688056-49087980-51a4-11ea-9a59-a022a76557fe.png">


<img width="450" alt="Screen Shot 2020-02-17 at 4 38 05 PM" src="https://user-images.githubusercontent.com/39356742/74688198-c8964880-51a4-11ea-90f8-40011d9f77a3.png">


Genres that don't appear on the NYT Best Seller list include
  
 >'New Adult', 'Contemporary', 'Science Fiction', 'Childrens', 'Food and Drink', 'Humor', 'Thriller', 'Polyamorous', 'Media Tie In', 'Paranormal', 'Dark', 'Business', 'Religion', 'Christian', 'Sports and Games'
 
 There are 955 unique authors of 1098 books, with most authors (844) having one book. Sarah j. Maas and Stephen King are the most prolific, both with 6 books.

## <a name="Text-Feature-Engineering"></a> Text Feature Engineering

Using Natural Language Toolkit the book descriptions were pre-processed then lemmatized with the NLTK implementation of the Word Net Lemmatizer.

Custom stop words are included to prevent data leakage in the description. Specifically words relating to NYT Best Seller list.

The scikit learn `CountVectorizer` produced the sparse text matrix for modeling.

## <a name="Modeling"></a> Modeling 

Two initial models are implemented 

- A Numerical model with the number of pages and rating or each book
- A text model with the vectorized book descriptions

### Baseline Modeling 

The numerial baseline model the scikit-learn implementation a Dummy Classifier solved with `strategy= 'stratified’` highlighting the class balance in the dataset. 

with a `mean training accuracy of 0.66`


<img width="350" alt="Screen Shot 2020-02-17 at 5 20 11 PM" src="https://user-images.githubusercontent.com/39356742/74690173-f92db080-51ab-11ea-985c-5428a7099103.png">

### Random Forest 

Numerical Model performance on the test set

<img width="350" alt="Screen Shot 2020-02-19 at 4 30 59 PM" src="https://user-images.githubusercontent.com/39356742/74878514-7cc6d900-5335-11ea-85d3-8d9e7a57395a.png">

Text Modeling performance on the test set

<img width="350" alt="Screen Shot 2020-02-19 at 4 31 15 PM" src="https://user-images.githubusercontent.com/39356742/74878488-70428080-5335-11ea-89d4-41b93804a108.png">
