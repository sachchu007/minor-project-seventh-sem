import tweepy
def func_auth():
    api_key="ifdDnfQEtcGNAnD6fxJRnpJgx"
    api_secret_key="R2ji153G0EWvjEqxRqpOFwGAo2Cuip3IoudyEz8jFllJr09sQF"
    access_token="1110242648307232774-TDjEX5GFHrnwbUg3sS18Vuk9nDkvHk"
    access_token_secret="vkkGXP5wsxXYsMBQjGlwXtvhe6p0O5qBS9HGleHIKuxy6"

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