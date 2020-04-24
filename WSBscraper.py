import praw

reddit = praw.Reddit(client_id='biRuOMuCJCyNiw',
    client_secret = 'E6uL2FScBRdyGCtFpprT-2We1qg',
    user_agent='windows:com.nodomain.wsbscraperCE:v0.1 (by u/StudentOfAwesomeness)')

#for submission in reddit.subreddit('wallstreetbets').hot(limit=None):
    #print(submission.title)

# we want comments, not submissions

submission = reddit.submission(id='g6k3gr')
#submission = reddit.submission(id='g77iwd')
submission.comments.replace_more(limit=None)
for comment in submission.comments.list():
    print(comment.body)

# code below can be replaced with list() method of comments
#comment_queue = submission.comments[:] # creates top level trees with queue of comments?
#while comment_queue:
#    comment = comment_queue.pop(0)
#    print(comment.body)
#    comment_queue.extend(comment.replies)

#for top_level_comment in submission.comments: ** only displays top level comments **
#   print(top_level_comment.body)


#top_level_comments = list(submission.comments)
#all_comments = submission.comments.list()