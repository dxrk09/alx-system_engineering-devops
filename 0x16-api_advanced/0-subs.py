#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyBot/1.0'}  # Set a custom User-Agent to avoid rate limiting
    
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        
        # Check if the subreddit exists
        if 'error' in data:
            if data['error'] == 404:  # Subreddit not found
                return 0
            else:
                raise Exception(f"Reddit API returned an error: {data['message']}")
        
        # Extract subscriber count
        subscribers = data['data']['subscribers']
        return subscribers
