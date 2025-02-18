# Spam-Ham Classification using Naive Bayes

This repository contains a Spam-Ham classification project using Naive Bayes classifiers (`MultinomialNB` and `BernoulliNB`) from `scikit-learn`.

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model](#model)
- [Evaluation](#evaluation)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Spam detection is a common NLP problem where emails, messages, or text data are classified as either spam or ham (not spam). This project implements a simple classifier using Naive Bayes algorithms.

## Dataset
The dataset used for training and testing consists of labeled text messages indicating whether they are spam or ham. A common dataset used for this task is the [SMS Spam Collection](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset).

## Installation
Clone the repository and install the dependencies:

```bash
git clone https://github.com/your-username/spam-ham-classifier.git
cd spam-ham-classifier
pip install -r requirements.txt
```

## Usage
Run the classification script:

```bash
python spam_ham_classifier.py
```

## Model
This project uses two types of Naive Bayes classifiers:
1. **MultinomialNB** - Best suited for text classification problems with term frequency features.
2. **BernoulliNB** - Works well with binary term occurrence features.

The text data is processed using the following steps:
- Tokenization
- Stopword removal
- TF-IDF vectorization

## Evaluation
The model is evaluated using common metrics such as:
- Accuracy
- Precision
- Recall
- F1-score

Results are printed at the end of the script.

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License
This project is licensed under the MIT License.
