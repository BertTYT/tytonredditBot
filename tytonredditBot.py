#! /usr/bin/env python3

import praw
import time
import os
from Authenticate import authenticate
from Authenticate import saved_comments
from botModules import tyt_bot

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

def main():
    reddit = authenticate()
    comments_replied = saved_comments()

    while True:
        tyt_bot(reddit, comments_replied)


if __name__ == '__main__':
    main()
