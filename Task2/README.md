## Task2

* `Get Historical Trends.ipynb`: collect trends as seeding topics
* `twitter_trends.json`: a list of trends in 2022 (it was replaced by v2)
* `twitter_trends_v2.json`: a list of trends in 2022


* `Get Tweets from Trends.ipynb`: load tweets and coversations by trends
* `tweets_v1`: all tweets based on `twitter_trends.json`
* `tweets_v2`: all tweets based on `twitter_trends_v2.json`
* `twarc2_conversation.jsonl`: all conversations from `tweets_v2`
* `tweets.jsonl`: all tweets in the conversations (including some missing tweets from the first collection)
* `unannotated`: unnotated data
* `label_config_*.json`: labels configs


* `Get User Followers & Following.ipynb`: collect tweet's followers and followings 
* `followers`: lists of followers by user id
* `followings`: lists of followings by user id
* `Run Heuristic.ipynb`: attempt to predict people's relationship by using number of followers and followings


* `Data Exploration.ipynb`: transform annotated data into a proper format and explore its distribution
* `Inter-Annotator Agreement.ipynb`: determine Weighted IAA from pilot setting


#### Ignore
* `names.txt`: a list of Thai popular nichnames