# standard imports
import numpy as np
import pandas as pd
# visualization
import matplotlib.pyplot as plt
import seaborn as sns
# notebook formatting
from pprint import pprint
import warnings
warnings.filterwarnings("ignore")


def var_distributions(X_train):
    # view variable distributions
    plt.figure(figsize=[10,15])
    plt.subplot(421)
    plt.title('Subscribers Count Distribution')
    sns.histplot(X_train.subscribers)
    plt.subplot(422)
    plt.title('Subscribers Count Distribution')
    sns.boxplot(X_train.subscribers)
    plt.subplot(423)
    plt.title('Views Count Distribution')
    sns.histplot(X_train.views)
    plt.subplot(424)
    plt.title('Views Count Distribution')
    sns.boxplot(X_train.views)
    plt.subplot(425)
    plt.title('Likes Count Distribution')
    sns.histplot(X_train.likes)
    plt.subplot(426)
    plt.title('Likes Count Distribution')
    sns.boxplot(X_train.likes)
    plt.subplot(427)
    plt.title('Comments Count Distribution')
    sns.histplot(X_train.comments)
    plt.subplot(428)
    plt.title('Comments Count Distribution')
    sns.boxplot(X_train.comments)
    plt.tight_layout()
    plt.show()

def var_distributions_2(X_train, y_train):
    # view variable distribution
    plt.figure(figsize=[10,15])
    plt.subplot(421)
    plt.title('Engagement Count Distribution')
    sns.histplot(y_train.engagement)
    plt.subplot(422)
    plt.title('Engagement Count Distribution')
    sns.boxplot(y_train.engagement)
    plt.subplot(423)
    plt.title('Shares Count Distribution')
    sns.histplot(X_train.shares)
    plt.subplot(424)
    plt.title('Shares Count Distribution')
    sns.boxplot(X_train.shares)
    plt.tight_layout()
    plt.show()

def x_var_by_shares(X_train):  
    # view X_train variables against y_train
    plt.figure(figsize=[10,15])
    plt.subplot(421)
    plt.title('Shares x Subscribers')
    sns.scatterplot(X_train.shares, X_train.subscribers, hue=X_train.subscribers)
    plt.subplot(422)
    plt.title('Shares x Subscribers')
    sns.scatterplot(X_train.shares, X_train.subscribers, hue=X_train.shares)
    plt.subplot(423)
    plt.title('Shares x Views')
    sns.scatterplot(X_train.shares, X_train.views, hue=X_train.views)
    plt.subplot(424)
    plt.title('Shares x Views')
    sns.scatterplot(X_train.shares, X_train.views, hue=X_train.shares)
    plt.subplot(425)
    plt.title('Shares x Likes')
    sns.scatterplot(X_train.shares, X_train.likes, hue=X_train.likes)
    plt.subplot(426)
    plt.title('Shares x Likes')
    sns.scatterplot(X_train.shares, X_train.likes, hue=X_train.shares)
    plt.subplot(427)
    plt.title('Shares x Comments')
    sns.scatterplot(X_train.shares, X_train.comments, hue=X_train.comments)
    plt.subplot(428)
    plt.title('Shares x Comments')
    sns.scatterplot(X_train.shares, X_train.comments, hue=X_train.shares)
    plt.tight_layout()
    plt.show()

def x_var_by_engage(X_train, y_train):
    # view X_train variables against X_train.engagement
    plt.figure(figsize=[10,15])
    plt.subplot(421)
    plt.title('Engagement x Subscribers')
    sns.scatterplot(y_train.engagement, X_train.subscribers, hue=X_train.subscribers)
    plt.subplot(422)
    plt.title('Engagement x Subscribers')
    sns.scatterplot(y_train.engagement, X_train.subscribers, hue=y_train.engagement)
    plt.subplot(423)
    plt.title('Engagement x Views')
    sns.scatterplot(y_train.engagement, X_train.views, hue=X_train.views)
    plt.subplot(424)
    plt.title('Engagement x Views')
    sns.scatterplot(y_train.engagement, X_train.views, hue=y_train.engagement)
    plt.subplot(425)
    plt.title('Engagement x Likes')
    sns.scatterplot(y_train.engagement, X_train.likes, hue=X_train.likes)
    plt.subplot(426)
    plt.title('Engagement x Likes')
    sns.scatterplot(y_train.engagement, X_train.likes, hue=y_train.engagement)
    plt.subplot(427)
    plt.title('Engagement x Comments')
    sns.scatterplot(y_train.engagement, X_train.comments, hue=X_train.comments)
    plt.subplot(428)
    plt.title('Engagement x Comments')
    sns.scatterplot(y_train.engagement, X_train.comments, hue=y_train.engagement)
    plt.tight_layout()
    plt.show()

def shares_x_engage(X_train, y_train):
    # view y_train variables against X_train.engagement
    plt.figure(figsize=[10,15])
    plt.subplot(421)
    plt.title('Engagement x Shares')
    sns.scatterplot(y_train.engagement, X_train.shares, hue=X_train.shares)
    plt.subplot(422)
    plt.title('Engagement x Shares')
    sns.scatterplot(y_train.engagement, X_train.shares, hue=y_train.engagement)
    plt.tight_layout()
    plt.show()





