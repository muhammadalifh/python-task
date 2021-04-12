# harus punya akun developer di twitter.com
# akses developer.twitter.com
import tweepy
import csv
import pandas as pd 

access_token = "" # dapat dari twitter developer
access_token_secret = "" # dapat dari twitter developer
api_key = "" # dapat dari twitter developer
api_key_secret = "" # dapat dari twitter developer

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
search_key = "" # input search key

csvFile = open(search_key+".csv","a+",newline="",encoding="utf-8")
csvWriter = csv.writer(csvFile)
c = []
i = []
u = []
t = []

for tweet in tweepy.Cursor(api.search,q=search_key,count=1000,lang="id",since="2021-01-01",until="2021-04-12").items():
	print(tweet.created_at,tweet.id,tweet.user.name,tweet.text)
	c.append(tweet.created_at)
	i.append(tweet.id)
	u.append(tweet.user.name)
	t.append(tweet.text.encode("utf-8"))
	tweets = [tweet.created_at,tweet.id,tweet.user.name,tweet.text.encode("utf-8")]
	csvWriter.writerow(tweets)

dictTweets = {"waktu":c,"id":i,"username":u,"teks":t}
df = pd.DataFrame(dictTweets,columns=["waktu","id","username","teks"])
df
