from logging import exception
import tweepy

consumer_key= "lExvivcHfGFaeX1xFtpv0m32J"
consumer_secret_key= "hTkwaG4UeZGo1uusVUBIwStHBb4OcSahPAeGx8K9sSqTpu2DHw"
access_token= "1394145443907440640-TwtVavBoZUCIhzG78qUQIvy5U1cT8q"
access_token_secret= "FQt1i7kDlYVMihktJ4DAyPgxuD1gVONpXKQqxDIHC78jb"

def OAuth():
    try:
        auth = tweepy.OAuthHandler(consumer_key,consumer_secret_key)
        auth.set_access_token(access_token,access_token_secret)
        return auth
    except Exception as e:
        return None


oauth=OAuth()
api=tweepy.API(oauth)
api.update_status("how is the weather")
print("mojo introduced")