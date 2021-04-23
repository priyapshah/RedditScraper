import praw

# create instance of reddit
reddit = praw.Reddit(client_id = '59cxBcvPTe0WpA',
                     client_secret = 'pirfl-hoyTkwgLLQ8epmN_EbD1NJvQ',
                     username = 'netsReddit',
                     password = 'swap>>>',
                     user_agent = "csScraper v1.0 (by /u/netsReddit)")

# subreddit of interest
subreddit = reddit.subreddit('UPenn')

# get the top 5 hot posts
hot_posts = subreddit.hot(limit = 1)

# print the titles 
for submission in hot_posts:
    print(submission.title)
    print(50*'-')
    comments = submission.comments
    for comment in comments:
        print(50*'*')
        print(comment.body)
        # if (len(comment.replies) > 0):
        #     for reply in comment.replies:
        #         print(reply.body)

