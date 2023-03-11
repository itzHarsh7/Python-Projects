from instabot import Bot
bot = Bot()

bot.login(username = "", password="")   # enter your username and password of your istagram id
bot.follow("")  # enter useename to be followed 
bot.unfollow("")  # enter useename to be unfollowed 
bot.upload_photo("", caption = "")   #Enter path of your picture to upload and write caption in your picture
bot.send_message("Message", ["Username", "Username"])  # u can write as many useername whom you want to send the same message
followers = bot.get_user_followers("")
for follower in followers:
    print(bot.get_user_info(follower))
following = bot.get_user_following("")
for Following in following:
    print(bot.get_user_info(Following))
