from flask import Flask, render_template
import tweepy

app =Flask(__name__)

# def twitter():
data_global = []
consumer_key = "0j5LAWSdPMxAerJP26vxkCDux"
consumer_secret = "U16Bt03DeT9LYnrIRxAEr37jNssjKTEm05oYITI7Q59ydQ56Md"
access_token = "965616465536692225-JDTVvWzNx27QwK4D8L2gwDCP6w89P83"
access_token_secret = "tALagRVgXrGfp90bqSui9dXdCHmu1XM8oD5lMcS3Hcc7b"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)
hashtags = ' #CovidHelp #Verified #CovidIndia'
tweet_data = tweepy.Cursor(api.search ,since = '2021-04-11',q= hashtags , lang= "en", tweet_mode = "extended", wait_on_rate_limit = True, wait_on_rate_limit_notify = True).items(200)
tweet_list= [t for t in tweet_data]
data = []
for tweet in tweet_list:
    dict={
        'username' : tweet.user.screen_name,
        'location' : tweet.user.location,
        'text' : tweet.full_text,
        'url' : "https://twitter.com/"+str(tweet.user.screen_name)+"/status/"+str(tweet.id)
    }
    
    data_global.append(dict)

@app.route('/')
def home():
    # consumer_key = "0j5LAWSdPMxAerJP26vxkCDux"
    # consumer_secret = "U16Bt03DeT9LYnrIRxAEr37jNssjKTEm05oYITI7Q59ydQ56Md"
    # access_token = "965616465536692225-JDTVvWzNx27QwK4D8L2gwDCP6w89P83"
    # access_token_secret = "tALagRVgXrGfp90bqSui9dXdCHmu1XM8oD5lMcS3Hcc7b"

    # auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    # auth.set_access_token(access_token,access_token_secret)
    # api = tweepy.API(auth)
    # hashtags = ' #CovidHelp #Covid19 #CovidIndia'
    # tweet_data = tweepy.Cursor(api.search ,since = '2021-04-11',q= hashtags , lang= "en", tweet_mode = "extended", wait_on_rate_limit = True, wait_on_rate_limit_notify = True).items(200)

    # tweet_list= [t for t in tweet_data]
    # data = []
    # for tweet in tweet_list:
    #     dict={
    #         'username' : tweet.user.screen_name,
    #         'location' : tweet.user.location,
    #         'text' : tweet.full_text,
    #         'url' : "https://twitter.com/"+str(tweet.user.screen_name)+"/status/"+str(tweet.id)
    #     }
        
    #     data.append(dict)
    return render_template('home.html', data = data_global)


if __name__ == '__main__':
    app.run(debug=True)