#! /usr/bin/env python3

import praw
import os

def authenticate():
    print('Authenticating...')
    reddit = praw.Reddit('test01', user_agent='TYTBot')
    print('Authenticated as {}'.format(reddit.user.me()))

    return reddit

def saved_comments():
    if not os.path.isfile('comments_replied.txt'):
        comments_replied = []
    else:
        with open('comments_replied.txt', 'r') as f:
            comments_replied = f.read()
            comments_replied = comments_replied.split('\n')
            comments_replied = filter(None, comments_replied)
            comments_replied = list(comments_replied)

    return comments_replied
