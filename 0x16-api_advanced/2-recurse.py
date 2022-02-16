#!/usr/bin/python3
"""Reddit API"""

from requests import get


def recurse(subreddit, hot_list=[], after=''):
    """return all hot post"""
    apiUrl = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit, after)
    headers = {'user-agent': 'my-app/0.0.1'}
    req = get(apiUrl, headers=headers)
    if req.json().get("kind") == "Listing":
        data = req.json().get("data")
        children = data.get("children")
        for c in children:
            hot_list.append(c.get("data").get("title"))
        page = data.get("after")
        if page:
            return recurse(subreddit, hot_list, page)

    if hot_list == []:
        return None
    return hot_list
