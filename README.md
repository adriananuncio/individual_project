# Determining TikTok Success

---
## Executive Summary
For the purpose of this project, TikTok success will be defined as a user generating engagement in the top 25% of total engagement.
- #### Project Goal
    - Determine drivers for Tiktok Success
    - Develope a regression machine learning model that can determine a trend in Tiktok success.
- #### Key Findings
    - views, likes, and comments had a statistically significant relationship with shares
    - subscribers, views, likes, and comments have a statistically significant relationship with engagement.
    - Regression modeling overfit the data.
- #### Next Steps
    - Moving foreward I will continue to classification modeling and feature engineering to see if a model can be created that determines the most important features of predicting Tiktok success.
    
## Project Description

PR firm, ExoPublic, has noticed the immense success generated through popular social media app - Tiktok. In 2023, the social media app has over 1.53 billion users, with over 1 billion videos watched daily (1). Celebrities, politicians, social media influencers, and most notibly, average, everyday people, have all been able to successfuly generate support for and/or promote their agenda through Tiktok. 
   ExoPublic wants to fill their client's audience gap by begining to direct their clients to generate a presence on Tiktok. However, the firm has limited knowledge of the app and does not know how to guide clients or what constitutes Tiktok success.
   ExoPublic has asked for the help of data scientist to determine how to generate success on Tiktok. The objective of the analysis of the dataset "Top 1000 Tiktokers all over the world" is to determine drivers and models for success on Tiktok.



## Project Goal
--- 
- Determine drivers for Tiktok success
- Develope a regression machine learning model that can determine a trend in Tiktok success.


## Initial Thoughts
---
While all variables are important to Tiktok success, I wonder if there is one variable that is more important than the others. For example I do no foresee subscribers having a huge impact because it is not guaranteed the subscriber will see the users content. However, I can see shares having a large impact on success because when a video is shared it is being sent to more people and increaseing user engagement.



## Planning
---
- ### Acquire data 
    - Data acquired from kaggle (link in Steps to Reproduce)
    - 1000 rows
    - 9 columns
- ### Prep/clean the data 
    - Format columns for exploration
    - Split data into train, validate, and test
- ### Explore the data
    - visualize distribution of variables
    - visualize variable relationships against shares and engagement to determine which will be target variable
    - stats testing
- ### Create Models for determining Tiktok success
    - Use models on train and validate
    - evaluate models
- ### Make Conclusions 


## Recreate
To recreate this repository:
- Clone repo
- Download the data set from Kaggle https://www.kaggle.com/datasets/syedjaferk/top-1000-tiktokers
- Run 'final_notebook'

## Conclusion
My OLS model was my top performing model with RMSE: 1.697643e-08 and R2: 1. Both my models outperformed the baseline model, however I believe both models are overfitting the data because their R2 values are 1, indicating the model explains all variance in dependent variables.
Knowing this, I will move forward with feature engineering and classification modeling to determine if a model that can determine the most important features for predicting TikTok success data can be made. In hindsight I wish I would have started with classification modeling because I feel the regression modeling would be more meaninful with classification context and feature engineering.

Moving foreward I recommend further data collection to include variables like the time the video was posted and the genre category of the video.

    
 