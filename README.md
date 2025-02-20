# **STAT W5243: Applied Data Science - Project 1: Korean Drama Analysis**
**Group 12:** Mengyan Li (ml4779), Zishun Shen (zs2695), Zhisheng Yang (zy2675), Shayan Chowdhury (sc4040)
**Spring 2025 - February 19, 2025**

## Project Overview
This project analyzes Korean drama data from 2015-2023, examining factors contributing to their success and audience reception. We combine multiple datasets, perform extensive data cleaning, and conduct statistical analyses to understand relationships between production characteristics, viewer ratings, and commercial success.

## Repository Structure
```
Applied-Data-Science-Project-One/
├── data/
│ ├── raw/ # Original datasets
│ │ ├── korean_drama.csv # Main K-drama dataset (2015-2023)
│ │ ├── kdrama_list.csv # Top ~1500 K-dramas
│ │ ├── top_100_kdrama.csv # Top 100 K-dramas of 2023
│ │ ├── reviews.csv # User reviews dataset
│ │ └── statistic_id831717_movie-industry-sales-revenue-in-south-korea-2014-2023.xlsx
│ └── processed/ # Cleaned and transformed datasets
│ ├── kdramas_merged.csv # Merged drama datasets
│ ├── UpdatedNew.csv # Cleaned korean_drama.csv
│ ├── newreview.csv # Cleaned reviews.csv
│ └── CLeaned Merged Dataset.csv # Final merged dataset
├── notebooks/
│ ├── final_report.ipynb # Final project report and analysis
│ ├── EDA and Feature Engineering.ipynb
│ ├── MergeData(1).ipynb # Data merging process
│ ├── Project One DateNew.ipynb # Date format standardization
│ ├── Project One New(1).ipynb # Initial data cleaning
│ ├── BarPlotAndBoxPlot.ipynb # Visualization notebooks
│ ├── Visualization1.qmd # Linear regression visualizations
│ └── info_reg.ipynb # Linear regression analysis
├── scripts/
│ ├── classify_sentiment.py # Sentiment analysis of reviews
│ └── scrape_mydramalist.py # Web scraping script for missing data
├── APSProjectOneReportFinalRevised.md # Final written report (Markdown)
└── APSProjectOneReportFinalRevised.pdf # Final written report (PDF)
```

## Usage
- Most of the main code is in the [`final_report.ipynb`](final_report.ipynb) notebook, which you can run. 
- Further analysis and feature engineering are in the other notebooks in the [`notebooks`](notebooks/) folder.


## Changelog
2.11

Project One DateNew.ipynb---Uploaded by Mengyan Li--Fix some mismatch in data(unify the date format to M-D-Y)

Dropping some data with incomplete dates (only contains month and year)

Using strftime('%m-%d-%Y') to unify the format of the start date and the end date

Project One New(1).ipynb---Uploaded by Mengyan Li--Remove outliers in review.csv and korean_drama.csv

Building boxplot using the interquartile range

removing any outliers above the upper limit and below the lower limit.

UpdatedNew.csv---Uploaded by Mengyan Li--The cleaned version of korean_drama.csv by fixing the date and removing outliers

newreview.csv---Uploaded by Mengyan Li--The cleaned version of review.csv by removing outliers


2.12 

Visualization.ipynb---Created By Zishun Shen

2.13

Final Cleaning Data(1).csv---Uploaded by Mengyan Li--Final cleaned version of korean_drama.csv by changing missing values to Others and dropping some missing values in numeric variables. 

2.16

MergeData(1).ipynb--Uploaded by Mengyan Li--Merged Final Cleaning Data(1) and newreview.csv

Using groupby function in pandas and grouped the review.csv by drama names

Calculating the mean of the scores by the users who marked the same drama

Using the mean score as the score for this specific drama

Doing this for Score for Story, Score for acting, Score for music, Score for rewatch value and Overall Score

CLeaned Merged Dataset.csv--Uploaded by Mengyan Li--The cleaned version of merged datasets (Final Cleaning Data(1) and newreview.csv)

Visualization1.qmd--Uploaded by Mengyan Li--The linear regresion visualization of newreview.csv(dependent variable: overall score) and the linear regression visualization of CLeaned Merged Dataset.csv (dependent variable: poplarity)

Visualizing the regression line and the plotting

EDA and Feature Engineering.ipynb--Uploaded by Mengyan Li--Some EDA and feature engineering to the merged dataset

Summary statistics of all numerical features 

Correlation heatmap of all numerical features

Histogram of all numerical features

Zero Variance/ Near zero variance checking

Missing value heatmap to check the pattern of all missing values

Box-Cox Transformation and one-hot encoding

Standardization/Normalization to necessary features

2.17

info_reg.ipynb--Uploaded by Zhisheng--Linear regression–y: pop, Standardization/Normalization on info numericals

2.18 -- Shayan

[final_report.ipynb](final_report.ipynb)
- Final report for the project
- Merged 3 kdrama datasets (Datasets 1-3): 
    - Dataset 1: [korean_drama.csv](data/raw/korean_drama.csv), source: [Korean Drama from 2015-2023 with Actors & Reviews by Chanon Charuchinda - Kaggle](https://www.kaggle.com/datasets/chanoncharuchinda/korean-drama-2015-23-actor-and-reviewmydramalist)
    - Dataset 2: [kdrama_list.csv](data/raw/kdrama_list.csv), source: [Top Korean Drama List (~1500) by Noor Rizki - Kaggle](https://www.kaggle.com/datasets/noorrizki/top-korean-drama-list-1500)
    - Dataset 3: [top_100_kdrama.csv](data/raw/top_100_kdrama.csv), source: [🏯 Top 100 KDrama 2023 by Gianina-Maria Petrascu - Kaggle](https://www.kaggle.com/datasets/gianinamariapetrascu/top-100-k-drama-2023)
- Merged merged-kdrama dataset (Datasets 1-3) with: 
    - Dataset 4: [statistic_id831717_movie-industry-sales-revenue-in-south-korea-2014-2023.xlsx](data/raw/statistic_id831717_movie-industry-sales-revenue-in-south-korea-2014-2023.xlsx), source: [Movie Industry Sales Revenue in South Korea 2014-2023 by ID831717 - Statista](https://www.statista.com/statistics/831717/south-korea-film-industry-sales-revenue/)
- Merged merged-kdrama dataset (Datasets 1-3) with: 
    - Dataset 5: [review.csv](data/raw/reviews.csv) dataset, source: [Korean Drama from 2015-2023 with Actors & Reviews by Chanon Charuchinda - Kaggle](https://www.kaggle.com/datasets/chanoncharuchinda/korean-drama-2015-23-actor-and-reviewmydramalist)
- Wrote functions to web scrape missing info (director, writer, synopsis, etc.) from [mydramalist.com](https://mydramalist.com) using Selenium and BeautifulSoup (but it's very slow...)
- Classified sentiment of reviews using Hugging Face's `transformers` library and a custom distilbert model
- Combined: 
    - [Visualization.ipynb](Visualization.ipynb)
    - ["Project One DateNew.ipynb"](Project One DateNew.ipynb)
    - ["EDA and Feature Engineering(2)(1).ipynb"](EDA and Feature Engineering(2)(1).ipynb) + plotted log probabilites from class

[data](./data/) -- folder containing all data files
[scripts](./scripts/) -- folder containing scripts
    - [classify_sentiment.py](./scripts/classify_sentiment.py): script to classify sentiment of reviews
    - [scrape_mydramalist.py](./scripts/scrape_mydramalist.py): script to web scrape missing info (director, writer, synopsis, etc.) from [mydramalist.com](https://mydramalist.com) using Selenium and BeautifulSoup

2.19
APSProjectOneReportFinalRevised.pdf--Uploaded by Mengyan Li--draft of the report

Visualization.ipynb---Updated and renamed as BarPlotAndBoxPlot.ipynb by Zishun

EDA and Feature Engineering.ipynb---Modified by Zishun---included additional one-hot encoded categorical columns:

1. Keep `year` and reverting it to `int` type

2. Drop `org_net` since it's too troublesome to handle

3. Drop all 10 original num_columns, keep StandardScaler and MinMaxScaler of `pop` and `n_helpful`

4. In addition multiple-hot encoded `air_on`

5. Modified numerical variables transformation