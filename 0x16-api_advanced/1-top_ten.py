#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """Print posts for a subreddit"""
    u = "https://api.reddit.com/r/{}/hot?sort=hot&limit=10".format(subreddit)
    try:
        top = requests.get(u, allow_redirects=False,
                           headers={'User-Agent': 'Someone'}
                           ).json().get("data").get("children")
        titles = [t.get("data").get("title") for t in top]
        for t in titles:
            print(t)
    except:
        print(None)
