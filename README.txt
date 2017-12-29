[Not Actively Maintained] API has been encountering issues since December 2017

Sunray Instagram Bot Functionality Introduction

TLDR: This instagram bot harvests targeted instagram profiles and allow you to follow

1. profile harvesting
- The bot harvests the latest 200 followers from the specified user ID in the nested dictionary.

2. follow_protocol
- Identifies and skips fake accounts and celebrity instagram accounts by follower/following ratio
- Identifies and skips accounts that you are already following/have sent follow request
- Follow healthy profiles and private profiles

3. unfollow_protocol
- Generate a list of following from your account
- Follow 

4. throttle
- To slow down the bot in order to avoid detection
- Customised timing in randint


This bot is a product of the python Instagram API developped by LevPasha at https://github.com/LevPasha/Instagram-API-python
It is necessary to download and install his API and requirements before this bot will function normally.
