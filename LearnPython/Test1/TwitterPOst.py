"""
Step 1
You must add your mobile phone to your Twitter profile before creating an application.
Go to: Settings -> Add Phone -> Add number -> Confirm -> Save.
Do not forget to turn off all text notifications.
Step 2
Set up a new app
Go to: Twitter Apps -> Create New App -> Leave Callback URL empty -> Create your Twitter application.
You should see "Your application has been created. Please take a moment to review and adjust your application's settings".
Step 3
By default, app's access level is read-only. To send out tweets, it requires write permission.
Go to: Permissions tab -> What type of access does your application need? -> Choose Read and Write -> Update settings.
You should see "The permission settings have been successfully updated. It may take a moment for the changes to reflect."
Step 4
Time to get the keys and access tokens for OAuth.
Go to: Keys and Access Tokens tab . You'll see this under "Your Access Token" : You haven't authorized this application for your own account yet. By creating your access token here, you will have everything you need to make API calls right away. The access token generated will be assigned your application's current permission level.
Click Create my access token
You should see "Your application access token has been successfully generated. It may take a moment for changes you've made to reflect. Refresh if your changes are not yet indicated. This access token can be used to make API requests on your own account's behalf. Do not share your access token secret with anyone."
Verify that you see access token/secret - and the permission is set to "read and write".
From this page, note down the Access Token, Access Token Secret, Consumer Key (API Key), Consumer Secret (API Secret). Consumer Key/Secret help twitter identify the app and Access Token/Secret help twitter identify the user (that is you).
Step 5
We will use tweepy to access Twitter's API. You can install it using pip: pip install tweepy (try to setup a virtualenv for this - they are very useful).
Finally, this simple python script sends out a tweet:

pip install tweepy
"""
import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "wtE3Ei7OLpI4VohOxoG9nfs1K",
    "consumer_secret"     : "IBhdRUFUqH5vbtzVYRGPnRZPgREr8mcWSHRxbaRcRc3Cw9MKQO",
    "access_token"        : "1002151531-QdIeV2A2ttPxBEfqmc44F7X46fKXQwvneHROZcs",
    "access_token_secret" : "jXqqUm51BFNhU1HurfKM9kQZZhpAdCE7SAbwKX9UFzkzQ" 
    }

  api = get_api(cfg)
  tweet = "Internet is working"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()