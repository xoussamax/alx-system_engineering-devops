#!/usr/bin/python3
""" ahaa"""
from requests import get
import json

def number_of_subscribers(subreddit):
    # Check if input is a string
    if not isinstance(subreddit, str):
        raise TypeError("Subreddit must be a string")
    
    url = f"https://www.reddit.com/r/{subreddit}/about/.json"
    headers = {"User-Agent": "my_app"}  # Set a custom user agent to avoid rate limiting issues

    try:
        response = get(url, headers=headers)
        
        if response.status_code != 200:
            return 0
            
        data = json.loads(response.text)
        subscriber_count = int(data["data"]["subscribers"])
        return subscriber_count

    except Exception as e:
        print(f"An error occurred while fetching {subreddit}: {str(e)}")
        return 0
