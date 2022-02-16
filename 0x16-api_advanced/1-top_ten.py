#!/usr/bin/python3
"""Reddit API"""

from requests import get


def top_ten(subreddit):
    """Print top 10 hot post"""
    apiUrl = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {'user-agent': 'my-app/0.0.1'}
    req = get(apiUrl, headers=headers, params={'limit': '10'})
    if req.json().get("kind") == "Listing":
        data = req.json().get("data")
        children = data.get("children")
        for c in children:
            print(c.get("data").get("title"))
    else:
        print("None")
