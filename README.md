# Instagram-Auto-Replier-Bot
This project is an Instagram automation bot that logs into Instagram, scrapes user profiles from a specific post's comments, and sends automated replies to their stories or highlights. The bot is built using Selenium with undetected-chromedriver to avoid detection.


# Features
Login to Instagram: The bot logs into Instagram using provided credentials.
Scrape Profiles: It scrapes unique user profiles from the comments of a specific Instagram post.
Send Automated Replies: The bot sends a predefined reply to users' active stories or highlights.
Profile Tracking: Tracks and saves processed profiles to avoid duplicate messaging.

# Setup
Prerequisites
Python 3.x
undetected-chromedriver
Selenium
tqdm

# Installations and requirenments
pip install undetected-chromedriver selenium tqdm

Must have latest chrome vertion!

# Update your Instagram credentials, post URL, and message details in the script:
username = "your_username"
password = "your_password"
post_url = "https://www.instagram.com/p/your_post_url/"
reply_message = "Hello there!"
emojis = "🙂"
reply_message2 = "How are you?"
