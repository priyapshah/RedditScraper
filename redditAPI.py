import praw

# create instance of reddit
reddit = praw.Reddit(client_id = '59cxBcvPTe0WpA',
                     client_secret = 'pirfl-hoyTkwgLLQ8epmN_EbD1NJvQ',
                     username = 'netsReddit',
                     password = 'swap>>>',
                     user_agent = "csScraper v1.0 (by /u/netsReddit)")

# subreddit of interest
subreddits = ['CMU', 'UIUC', 'MIT', 'stanford', 'UCSD', 'berkeley', 'cornell', 'umich', 'udub', 'umd', 'gatech', 
              'neu', 'columbia', 'uwmadison', 'upenn', 'utaustin' , 'purdue', 'umass', 'nyu', 'ucla']

keywords = ['CS', 'CSE', 'CIS', 'EECS', 'Comp Sci', 'CompSci', 'CSCI', 'Computer Science', 'Computer Sciences', 
            'Computerscience', 'C Science', 'Cscience']

# outer for-loop goes to each subreddit. inner for-loop scans for keywords
for subreddit in subreddits:
  new = subreddit.new(limit = 500)
  relevant_posts = []
  for submission in new:
    if (submission.body.contains )
    print(submission.title)
    

# subreddit = reddit.subreddit('UPenn')

# get the top 5 hot posts
hot_posts = subreddit.hot(limit = 1)

# print the titles 
for submission in hot_posts:
    print(submission.title)
    print(50*'-')
    submission.comments.replace_more(limit=0)
    comments = submission.comments.list()
    for comment in comments:
        print(50*'*')
        print(comment.body)
        # if (len(comment.replies) > 0):
        #     for reply in comment.replies:
        #         print(reply.body)

