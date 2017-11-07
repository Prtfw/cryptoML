#!/usr/bin/env python3

import praw
import re
import datetime

# def parse_comment(comment, output_file):
    # output_file.write(comment.id + ',' 
            # + str(comment.author) + ',' 
            # + re.sub('\n',' \ newline \ ',re.sub(',','\,',comment.body)) + ',' 
            # + str(comment.created_utc) + ',' 
            # + str(comment.ups) + ',' 
            # + str(comment.downs) + ',' 
            # + str(comment.gilded) + '\n')

    # print(len(comment.replies))
    # for c in comment.replies.list().replace_more(limit=0):
        # parse_comment(c, output_file)


reddit = praw.Reddit(client_id='ZcnK5LAldOQV7Q',
                     client_secret='aQKtfImtKmqWzjRbrQrvvpGkIKs',
                     password='Mr6AkDryQj2lzJ8PDW8Q',
                     username='TaoistPellagra',
                     user_agent='awesomescraper')

output_file = open('comments_timeframe.csv', 'a')
output_file.write('id,author,body,timestamp_utc,upvotes,downvotes,gilded\n') #write column headers
comment_count = 0

for submission in reddit.subreddit('ethtrader').submissions(start=1454284800, end=1510023264):
    submission = reddit.submission(id=submission)
    submission.comments.replace_more(limit=0)
    for comment in submission.comments.list():
        output_file.write(comment.id + ',' 
                + str(comment.author) + ',' 
                + re.sub('\n',' \ newline \ ',re.sub(',','\,',comment.body)) + ',' #Reversibly replace chars that may be problematic for parsing
                + str(comment.created_utc) + ',' 
                + str(comment.ups) + ',' 
                + str(comment.downs) + ',' 
                + str(comment.gilded) + '\n')
        comment_count += 1
        if comment_count % 1000 == 0: 
            print(str(comment_count) + ' comments at ' + str(datetime.datetime.now()))
#
#4cgibt
#submission = reddit.submission(id='4cgibt')
#submission = reddit.submission(id='4cr30n')

#print(len(submission.comments))
#for top_level_comment in submission.comments:
    
    #print(dir(top_level_comment))
    #print(type(str(top_level_comment.gilded)))
    #print(top_level_comment.replies.list())
 #   parse_comment(top_level_comment, output_file)


