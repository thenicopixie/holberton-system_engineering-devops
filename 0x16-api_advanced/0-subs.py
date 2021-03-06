#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Return number of subscribers of a subreddit"""
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    try:
        return requests.get(url, allow_redirects=False,
                            headers={'User-Agent': 'SomethingSomething'}
                            ).json().get("data").get("subscribers")
    except:
        return 0
