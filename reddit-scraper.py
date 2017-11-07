#!/usr/bin/env python3

import praw

reddit = praw.Reddit(client_id='ZcnK5LAldOQV7Q',
                     client_secret='aQKtfImtKmqWzjRbrQrvvpGkIKs',
                     password='Mr6AkDryQj2lzJ8PDW8Q',
                     username='TaoistPellagra',
                     user_agent='awesomescraper')

#for submission in reddit.subreddit('ethtrader').submissions(start=1456790400, end=1459468800):
#    print(submission)

submission = reddit.submission(id='4cg27c')

for top_level_comment in submission.comments:
    print(type(top_level_comment))

