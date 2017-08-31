#! /usr/bin/env python3

import praw
import time
import os

#Reply Messages

shop_message = '''Did someone mention Shop TYT! Come get TYT merch at [ShopTYT](https://shoptyt.com/)\n
                Follow Shop TYT on [Instagram](https://www.instagram.com/shoptytofficial/) and show us what TYT swag you're rocking.\n
                ------
                ######TYTBot is a bot not a human. Find out more about TYTBot in the Wiki'''

membership_message = '''Are you interested in becoming a TYT Member? [Membership has its perks!](https://tytnetwork.com/join/)\n
                     Members get access to the Full Show plus Post Game plus Agressive Progressives plus Old School plus so much more!\n
                     ------
                     ######TYTBot is a bot not a human. Find out more about TYTBot in the Wiki'''

live_message = '''See the live show here from 6-8pm ET every week night!\n
               Chat with viewers and hosts using '#TYTLive.'\n
               Get your message across to TYT using Youtube's Super Chat!
               ------
               ######TYTBot is a bot not a human. Find out more about TYTBot in the Wiki'''

#Dictionary of phrases bot itirates through

phrases = { '(?i)Shop TYT' : shop_message , '(?i)TYT Shop' : shop_message , '(?i)Membership' : membership_message , '(?i)Live Show' : live_message }

#Start bot module

def tyt_bot(r, comments_replied):
    print('Starting bot...')

    for comment in r.subreddit('testing_css_and_stuff').comments(limit=10):
        for key in phrases.keys(): #iterates thru keys in phrases dictionary
            if key in comment.body and comment.id not in comments_replied and comment.author != r.user.me():
                comment.reply(phrase[key]) #replies with value from phrases dictionary
                print('Replied to comment ' + comment.id)

                comments_replied.append(comment.id)

                with open('Macintosh HD/Users/bhidalgo/Documents/github_local/PythonScripts/tytonredditBot/Logs/comments_replied.txt', 'a') as f:
                    f.write(comment.id + '\n')


    print('Will start up again in 5 seconds...')
    time.sleep(5)  # sleep for 5 seconds
