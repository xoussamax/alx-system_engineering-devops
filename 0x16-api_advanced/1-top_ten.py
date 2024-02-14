#!/usr/bin/python3
"""Titles of the first 10 hot posts listed in a subreddit"""
from requests import get


def top_ten(subreddit):
    """Queries Reddit API and prints the titles
    of the first 10 hot spots in a subreddit"""

    if subreddit is None or not isinstance(subreddit, str):
        print('None')

    api_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}

    response = get(api_url, headers=user_agent,
                   params=params, allow_redirects=False)
    if response.status_code != 200:
        print('None')

    results = response.json()

    try:
        data = results['data']['children']

        for post in data:
            print(post['data']['title'])

    except Exception:
        print('None')
