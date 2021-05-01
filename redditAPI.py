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

for school in subreddits:
    subreddit = reddit.subreddit(school)

    # create a file for the school
    schoolFile = open(school+".txt","w+")

    # get the top n hot posts
    hot_posts = subreddit.hot(limit = 5)

    # print the post titles and body 
    for submission in hot_posts:
        print(submission.title)
        schoolFile.write(submission.title)
        schoolFile.write("\n")
        print(submission.selftext)
        schoolFile.write(submission.selftext)
        schoolFile.write("\n")
        print(50*'-')
        


# outer for-loop goes to each subreddit. inner for-loop scans for keywords
# for subreddit in subreddits:
#   new = subreddit.new(limit = 500)
#   relevant_posts = []
#   for submission in new:
#     if (submission.body.contains )
#     print(submission.title)
