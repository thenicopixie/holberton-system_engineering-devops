#!/usr/bin/python3
"""
Recursive funciton that queries the Reddit API and returns
a list containing the titles of all hot articles for a given
subreddit. If no results are found for the given subreddit,
the function returns None
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Retuns a list of titles of all hot articles
    for a given subreddit.
    """
    url = "https://api.reddit.com/r/{}/hot".format(subreddit)
    if after is not None:
        url += "?after={}".format(after)
    try:
        top = requests.get(url, allow_redirects=False,
                           headers={'User-Agent': 'Someone'}
                           ).json().get("data")
        children = top.get("children")
        for child in children:
            hot_list.append(child.get("data").get("title"))
        next_page = top.get("after")
        if next_page:
            return recurse(subreddit, hot_list, after=next_page)
        else:
            return hot_list
    except:
        return None
