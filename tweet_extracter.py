import tweepy
def func_auth():
    api_key="#############"
    api_secret_key="###########"
    access_token="###########"
    access_token_secret="#################"

    auth = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_secret_key)
    auth.set_access_token(access_token,access_token_secret)
    return auth
def main():
    api=tweepy.API(func_auth())
    hashtag=input("Enter the hashtag:")
    number=input("Enter the number of tweets(max 3200):")
    number=int(number)
    fileName=input("Enter the filename where tweets will be saved:")+".txt"
    my_file=open(fileName,'w',encoding="utf-8")
    i=1
    try:
        tweets=tweepy.Cursor(api.search,q=hashtag).items(number)
        for tweet in tweets:
            my_file.write(str(i)+". "+tweet.text)
            my_file.write("\n")
            i+=1
        print("Tweets written to file successfully")
    except Exception as E:
        print("Some error occured"+str(E))

    my_file.close()
main()
