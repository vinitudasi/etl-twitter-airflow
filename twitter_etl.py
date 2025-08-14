import os
from dotenv import load_dotenv

import tweepy
import pandas as pd

# Load environment variables from .env file
load_dotenv()

def run_twitter_etl():
    # Retrieve Twitter API credentials from environment variables
    consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
    consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
    access_key = os.getenv("TWITTER_ACCESS_KEY")
    access_secret = os.getenv("TWITTER_ACCESS_SECRET")

    # Authenticate with the Twitter API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # Fetch the last 100 tweets from Elon Musk
    tweets = api.user_timeline(
        screen_name='@elonmusk',
        count=100,
        include_rts=False,
        tweet_mode='extended'
    )

    # Extract and structure relevant tweet data
    tweet_list = []
    for tweet in tweets:
        text = tweet._json["full_text"]

        refined_tweet = {
            "user": tweet.user.screen_name,
            "text": text,
            "favorite_count": tweet.favorite_count,
            "retweet_count": tweet.retweet_count,
            "created_at": tweet.created_at
        }

        tweet_list.append(refined_tweet)

    # Convert to pandas DataFrame
    df = pd.DataFrame(tweet_list)

    # Save DataFrame to S3 (URL should be in form s3://bucket-name/path/)
    s3_bucket = os.getenv("S3_BUCKET")
    output_path = os.path.join(s3_bucket, "elonmusk_twitter_data.csv")
    df.to_csv(output_path, index=False)

    print(f"Data saved to {output_path}")
