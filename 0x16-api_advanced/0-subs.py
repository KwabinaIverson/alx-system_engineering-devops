#!/usr/bin/python3
"""
    A function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers)
    for a given subreddit. If an invalid subreddit is given, the function should return 0
"""

import requests

def number_of_subscribers(subreddit):
    """
    A function that queries the Reddit API.

    Arg:
        subreddit (str): A valid subreddit.

    Returns:
        Number of subcribers (int)  (not active users, total subscribers) for a given subreddit.
        If an invalid subreddit is given, the function should return 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": 'MyBot/1.0'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            print(f"Error: {data['message']}")
            return 0
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return 0
    except ValueError as ve:
        print(f"Error decoding JSON: {ve}")
        return 0
