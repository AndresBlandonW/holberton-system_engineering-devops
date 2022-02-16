#!/usr/bin/python3
"""Reddit API return numbers of subs"""

from requests import get


def number_of_subscribers(subreddit):
    """return number of subsscribers"""
    apiUrl = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'my-app/0.0.1'}
    req = get(apiUrl, headers=headers)
    if req.json().get("kind") == "t5":
        data = req.json().get("data")
        return data.get("subscribers")
    else:
        return 0
