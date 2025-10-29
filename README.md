# Spam Mail Prediction
A machine learning-based web app to classify emails/messages as Spam or Ham (not spam) using Logistic Regression and TF-IDF vectorization, deployed with Streamlit.

## Project Overview
This project is a spam mail classifier that:
 - Takes a user’s email/message input.
 - Converts the text into numerical features using TF-IDF vectorization.
 - Predicts whether the message is Spam or Ham using a trained Logistic Regression model.
 - Provides a simple web interface using Streamlit.

## Model Details
 - Algorithm: Logistic Regression
 - Feature Extraction: TF-IDF Vectorization (min_df=1, stop_words='english', lowercase=True)
 - Label Encoding: Spam = 0, Ham = 1
 - Training/Test Split: 80% training, 20% testing
 - Evaluation Metric: Accuracy

## Results
The Logistic Regression model achieved an accuracy score of approximately 0.9676 on training data and 0.9668 on testing data.

## Example

<img width="512" height="250" alt="ham" src="https://github.com/user-attachments/assets/9fda25a3-cc3b-495f-a9b9-e85e586eec2d" />
<img width="502" height="266" alt="spam" src="https://github.com/user-attachments/assets/6b0774d9-3973-42f9-a7ee-143f7dea43ad" />
