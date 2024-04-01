# My Data
I did a few transformations to my data when I got it. That can all be found in the [initial_exploration](https://github.com/44-566-Machine-Learning-F23/ml-project-cmcclintock01/blob/master/initial_exploration.ipynb) file. 
# My Transformations
First, I made copies of the data and took out every player in both data sets that didn't have more than 100 at bats to ensure that the players I was looking at had enough data. Second, I grouped by the player name on both sides so that players that were traded and had two instances were combined. After that I used the train_test_split.
I added a new feature into the data named 'AVG_group'. I used this feature to split my data into 10 separate groups based on the players AVG. This is what I will try to predict using all of the other features.
# My Visualizations
You can see visualizations of my data in [linear_regression](https://github.com/44-566-Machine-Learning-F23/ml-project-cmcclintock01/blob/master/linear_regression.ipynb) and you can find the confusion matrix of my DecisionTree and SVM predicitons in [classification](https://github.com/44-566-Machine-Learning-F23/ml-project-cmcclintock01/blob/master/classification.ipynb).
