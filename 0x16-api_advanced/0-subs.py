#!/usr/bin/python3
"""number of subscribers for a given subreddit"""
def number_of_subscribers(subreddit):
    """Queries Reddit API and returns the
    number of subscribers for subreddit"""
    from requests import get
    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    user_agent = {'User-agent': 'User-agent'}

    response = get(api_url, headers=user_agent, allow_redirects=False)
    if response.status_code >= 300:
        return 0

    return response.json().get("data").get("subscribers")
