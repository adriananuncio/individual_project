# individual_project

# Acquire and Prepare
### Original Data Set
__Shape:__ 
    
    (1000,9)
    (rows, columns)
    
__Stats:__ 
    
- Only statistics for column - Rank were given. 
- 'Rank' does not need stats. 
- Other stats can be attained from the below columns once cleaned to be numerical.

        - Subscribers Count 
        - Views. Avg
        - Likes. Avg 
        - Comments. Avg 
        - Shares. Avg
        
__Info__:

- 'Name' has 2 null values
- All columns except 'Rank' are objects
- These columns will be changed to a float because that is a usuable dtype.

        - Subscribers Count 
        - Views. Avg 
        - Likes. Avg
        - Comments. Avg 
        - Shares. Avg
- rename columns to be lowercase and snakecase

__Data Types:__

- All columns except 'Rank' are objects
- These columns will be changed to a float because that is a usuable dtype.

        - Subscribers Count
        - Views. Avg 
        - Likes. Avg 
        - Comments. Avg
        - Shares. Avg
        
__Null/ NA Values:__
    

- 'Name' contains 2 null values.


__Unique Value Count:__

    Rank                 1000
    Username              997 (3 DUPLICATES)
    Tiktok Link           997 (3 DUPLICATES)
    Name                  991 (7 DUPLICATES, 2 NULL)
    Subscribers Count     413
    Views. Avg            128
    Likes. Avg            879
    Comments. Avg         255
    Shares. Avg           376
    
    Because of the 1:1 identifying nature of 
        - Username 
        - Tiktok Link 
        - Name
    I am able to quickly see there are duplicates present in these columns. The remaining columns do not follow the same 1:1 nature thus the presence of duplicate values is not relevent.
    
    
__To Do for Data Cleaning:__
__X__ Convert these columns to be numerical.

        - Subscribers Count
        - Views. Avg
        - Likes. Avg 
        - Comments. Avg
        - Shares. Avg'
__X__ Rename columns to be formatted as all lowercase and in snakecase. Remove periods from names.
__X__ Format name to be all lowercase and in snakecase
__X__ Find and delete duplicate values in
    
        - Username
            - drop annajobling @ index 101
            - drop kanebrown @ index 102
            - drop nolaymex @ index 100
        ___________________________________   
        - Tiktok Link
            column dropped
        ___________________________________
        - Name
            Drop:
            - drop nolay @ index 100
            - drop annajobling @ index 101
            - drop kanebrown @ index 102
            ---------------------------------------------------------------
            Do not drop:
            - different tiktok accounts: fernanda @ index 22 and 191
            - different tiktok accounts: max_taylor @ index 92 and 195
            - different tiktok accounts: tommy @ index 288 and 785
            - different tiktok accounts: mikaela_testa @ index 210 and 949
            ---------------------------------------------------------------
            Look in to:
            - name 'NaN' probably refers to null values
            
            null values are located in column 'name' @ index 490 and 686. Because I do not plan to use name but am keeping it for identification and reference, these null values can remain as is
        ___________________________________________________________________
        Finalized Duplicates to Drop:
            - drop annajobling @ index 101
            - drop kanebrown @ index 102
            - drop nolaymex @ index 100

__X__ Remove tiktok link. The link format is below.

        https://www.tiktok.com/@Username
        
***ADDITIONAL DF CHANGE***
    
    I have created a column labeled engagement. This column is the sum of views, likes, comments, and shares in respect to each tiktok account. Subscribers was intentionally left out of the equation because I feel the metric is an unreliable indication of content and account performance, due to the nature of people to follow users they know in real life and/or admire like celebrities, but who do not necessarily post content. In other words, people have a tendency to follow people because of who they are.
    
*Question to get second opinion on:*

    Currently engagement is:
    
       df['engagement'] = (avg.views + avg.likes + avg.comments + avg.shares)
    
    Instead of engagement being the sum of those metrics, should engagement be their average, since the metrics are averages themselves? AKA:
    
    df['engagement'] = (avg.views + avg.likes + avg.comments + avg.shares)/4

# Exploratory Analysis
### __Questions:__

- **Is it best to remove outliers or keep them?**
   
        The outliers in this dataset are above the IQR, I have no outliers below the IQR. Do to the nature of social media success being a bit of an above IQR outlier itself, I will keep the outliers in the dataset and use them as a sort of indication for viral success. I will remove these outliers if my models have difficulty replicating their numbers.
            I could possibly classify the data using IQR
                - 0%-25%: underperformers
                - 25%-75%: average
                - 75%-100%: who is she
                - outliers: viral
                
- **Does subscribers have influence over shares?**

        It appears a large subscriber count does not correlate to high shares.
        
- **Does views have influence over shares?**

        There may be a correlation. Statistic testing is necessary to confirm.
        
- **Does likes have influence over shares?**

        There may be a correlation. Statistic testing is necessary to confirm.
        
- **Does comments have influence over shares?**

        It does not appear there is a correlation but I will perform statistic test to be sure.
    
- **How does subscribers compare to engagement(likes, views, comments, and shares)**

        There is a clear correlation between engagement and subscribers. Will perform stats testing to find line of best fit.
        
- **How does views compare to engagement(likes, views, comments, and shares)**

        There seems to be a correlation but I need statistic testing to verify
        
- **How does likes compare to engagement(likes, views, comments, and shares)**

        There might be a correlation but stats testing is needed
    
- **How does comments compare to engagement(likes, views, comments, and shares)**

        If there is a correlation it is not obvious but it looks like something is happing. Stats tests needed.
    
- **How does shares compare to engagement(likes, views, comments, and shares)**

        They look like inverses of one another. Stats testing.
        
- **What does the data look like if I remove views from engagement and added shares?**

        It does not look significantly different. I will keep views in 

- **Is total engagement, shares, or views the best indication of success?**
        
        Engagement had a smaller p value for all stats testing commpared to Shares. Because a smaller p-value indicates a stronger correlation, I am choosing to move foreward with Engagement as my y value.


- **What does the data look like if I classify by the iqr?**

__Statistic Testing__
    
    - views X shares
        There is a statistically significant relationship between views and shares.
        
    - likes X shares
        There is a statistically significant relationship between likes and shares.
        
    - comments X shares
        There is a statistically significant relationship between likes and shares.
        
    - subscribers X engagement
        There is a statistically significant relationship.
        
    - views X engagement
        There is a statistically significant relationship.
    
    - likes X engagement
        There is a statistically significant relationship.
    
    - comments X engagement
        There is a statistically significant relationship.
        
    - shares X engagement
        There is NOT a statistically significant relationship.