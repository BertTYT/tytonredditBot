#! /usr/bin/env python3

import praw
import time
import os
from Authenticate import authenticate

#Subreddit applied to

sub = 'testing_css_and_stuff'

#Reply Messages

shop_message = '''###Did someone mention Shop TYT! Come get TYT merch at [ShopTYT](https://shoptyt.com/)\n\n
#####Follow Shop TYT on [Instagram](https://www.instagram.com/shoptytofficial/) and show us what TYT swag you're rocking.\n\n
------\n\n
^TYTBot ^is ^a ^bot ^not ^a ^human. ^Find ^out ^more ^about ^TYTBot ^in ^the ^Wiki.'''

membership_message = '''###Are you interested in becoming a TYT Member? [Membership has its perks!](https://tytnetwork.com/join/)\n\n
#####Members get access to the Full Show plus Post Game plus Agressive Progressives plus Old School plus so much more!\n\n
------\n\n
^TYTBot ^is ^a ^bot ^not ^a ^human. ^Find ^out ^more ^about ^TYTBot ^in ^the ^Wiki.'''

live_message = '''###See the live show here from 6-8pm ET every week night!\n\n
###Chat with viewers and hosts using '#TYTLive.'\n\n
#####Get your message across to TYT using Youtube's Super Chat!\n\n
------\n\n
^TYTBot ^is ^a ^bot ^not ^a ^human. ^Find ^out ^more ^about ^TYTBot ^in ^the ^Wiki.'''

of_course = '''#[OF COOOUURSE!](https://media.giphy.com/media/E1GXeDOw2p0zK/giphy.gif)\n\n
------\n\n
^You ^have ^invoked ^TYTBot. ^Find ^out ^more ^about ^TYTBot ^in ^the ^Wiki.'''

serabees = '''#[SERABEES!](https://youtu.be/YlTp-Rg-hug?t=4m56s)\n\n
------\n\n
^You ^have ^invoked ^TYTBot. ^Find ^out ^more ^about ^TYTBot ^in ^the ^Wiki.'''

we_got_em = '''#[Ladies and gentlemen...](https://www.youtube.com/watch?v=S02BHmWPZNs)\n\n
------\n\n
^You ^have ^invoked ^TYTBot. ^Find ^out ^more ^about ^TYTBot ^in ^the ^Wiki.'''

supreme_court = '''#[The TYT Supreme Court has ruled!](https://media.giphy.com/media/vbtOtFhEmeDvO/giphy.gif)\n\n
------\n\n
^You ^have ^invoked ^TYTBot. ^Find ^out ^more ^about ^TYTBot ^in ^the ^Wiki.'''

god_bless = '''#[God bless. Go Foward.](https://cdn.meme.am/instances/250x250/18279427/god-bless-go-forward.jpg)\n\n
------\n\n
^You ^have ^invoked ^TYTBot. ^Find ^out ^more ^about ^TYTBot ^in ^the ^Wiki.'''

hoss = '''#[Have at it!..](https://memegenerator.net/img/instances/500x/63501002/have-at-it-hoss.jpg)\n\n
------\n\n
^You ^have ^invoked ^TYTBot. ^Find ^out ^more ^about ^TYTBot ^in ^the ^Wiki.'''

#Dictionary of phrases bot itirates through

phrases = { 'Shop TYT' : shop_message , 'TYT Shop' : shop_message , 'Membership' : membership_message , 'Live Show' : live_message , 'Of Course!' : of_course ,
 'Of Cooooouurse!' : of_course , 'Serabeees' : serabees , 'Serabeees!' : serabees , 'we got him' : we_got_em , 'tyt supreme court' : supreme_court ,
 'God Bless' : god_bless }

def tyt_bot(r, comments_replied):
    print('Starting bot...')

    for key in phrases.keys(): #iterates thru keys in phrases dictionary

        for comment in r.subreddit(sub).comments(limit=10):
            if key.lower() in comment.body.lower() and comment.id not in comments_replied and comment.author != r.user.me():
                comment.reply(phrases[key]) #replies with value from phrases dictionary
                print('Replied to comment ' + comment.id)

                comments_replied.append(comment.id)

                with open('comments_replied.txt', 'a') as f:
                    f.write(comment.id + '\n')


    print('Will start up again in 5 seconds...')
    time.sleep(5)  # sleep for 5 seconds

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

def main():
    reddit = authenticate()
    comments_replied = saved_comments()

    while True:
        tyt_bot(reddit, comments_replied)


if __name__ == '__main__':
    main()
