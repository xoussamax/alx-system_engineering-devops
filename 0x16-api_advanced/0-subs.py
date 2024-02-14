#!/usr/bin/python3
"""number of subscribers for a given subreddit"""
from typing import Optional
import json
from urllib.parse import quote # For URL encoding

import requests

API_URL = "http://www.reddit.com/"
USER_AGENT = {"User-agent": "Mozilla/5.0"}
CONTENT_TYPE = "application/json; charset=utf-8"

def number_of_subscribers(subreddit: str) -> int:
    """Returns the number of subscribers for a given subreddit."""
    try:
        about_page = _fetch_about_page(subreddit)
        
        # Checking for correct content type
        assert CONTENT_TYPE in about_page.headers['Content-Type']
    
        page_content = about_page.text
            
            # Parsing JSON data
            parsed_dict = json.loads(page_content)
                
                # Extracting subscriber count
                num_subscribers = parsed_dict['data']['subscribers']
                
                return num_subscribers
    except Exception:
        raise ValueError(f"Invalid subreddit '{subreddit}'!")

def _fetch_about_page(subreddit: str) -> Optional[requests.Response]:
    """Fetches the /about.json endpoint for a given subreddit."""
    encoded_sr = quote(subreddit)  
    target_endpoint = f"/r/{encoded_sr}/about.json"
    full_target_path = API_URL + target_endpoint
    
    resp = requests.get(full_target_path, headers=USER_AGENT)
    
    # Checking for possible redirections
    if resp.history:
        last_resp = resp.history[-1]
        location = last_resp.headers['Location']
        if '/search?q=' in location:
            # We were redirected to search results => non-existent subreddit
            return None
    
    return resp
