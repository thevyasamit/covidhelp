from flask import Flask, render_template
import tweepy

app =Flask(__name__)

# def twitter():
data_global = []
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

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
    return render_template('home.html', data = data_global)


if __name__ == '__main__':
    app.run(debug=True)