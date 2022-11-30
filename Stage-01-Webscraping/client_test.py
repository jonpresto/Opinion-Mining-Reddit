import praw

reddit = praw.Reddit(
    client_id = 'wHg_1bNEVbRHEN7ajiC5Tw',
    client_secret = 'Z5bY7PWrsxUS3CykE9BYQYtu05HPEA',
    user_agent = 'PrincipleEmergency62'
)

print(reddit.read_only) #Output: True

# Print submission titles for the top 10 hottest posts right now

for submission in reddit.subreddit('spotify').hot(limit=10):
    print(submission.title)


reddit = praw.Reddit(
    client_id = 'wHg_1bNEVbRHEN7ajiC5Tw',
    client_secret = 'Z5bY7PWrsxUS3CykE9BYQYtu05HPEA',
    username="PrincipleEmergency62",
    password="wall34KeysPhon3#",
    user_agent="PrincipleEmergency62"

)

print(reddit.read_only)
# Output: False