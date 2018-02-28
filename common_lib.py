import re
import os
from typing import List, Dict, Set

import praw
from wordcloud import WordCloud
from PIL import Image

class WordcloudSettings:

    def __init__(self, height=800, width=800, margin=5, max_words=200, filtered_words=[], output_filename="wordcloud.png"):
        self.height = height
        self.width = width
        self.margin = margin
        self.max_words = max_words
        self.filtered_words = set(filtered_words)
        self.output_filename = output_filename

    def add_url(self, reddit_url: str) -> 'WordcloudSettings':
        self.url = reddit_url
        return self

def generate_wordcloud(settings: WordcloudSettings):
    try:
        verify_settings(settings)
    except Exception as e:
        print(e)
        return 
    comments = extract_comments(settings.url)
    frequency_map = generate_frequency_map(comments, settings.filtered_words)
    generate_image(frequency_map, settings)

def verify_settings(settings: WordcloudSettings):

    # Verify the url
    if not settings.url or type(settings.url) != str:
        raise ValueError("Error: Invalid reddit url: {0}".format(settings.url))
    regex = re.compile('.*reddit.com/.*/comments/.*')
    if regex.match(settings.url) == None:
        raise ValueError("Error: Invalid reddit url: {0}".format(settings.url))
    
    # Verify the height, width, and margin.
    if type(settings.height) != int:
        raise ValueError("Error: Invalid height value of: {0}. Expected int got {1}".format(settings.height, type(settings.height)))
    if type(settings.width) != int:
        raise ValueError("Error: Invalid width value of: {0}. Expected int got {1}".format(settings.width, type(settings.width)))
    if type(settings.margin) != int:
        raise ValueError("Error: Invalid margin value of: {0}. Expected int got {1}".format(settings.margin, type(settings.margin)))
    if type(settings.max_words) != int:
        raise ValueError("Error: Invalid max_words value of: {0}. Expected int got {1}".format(settings.max_words, type(settings.max_words)))

def extract_comments(reddit_url: str) -> List[str]:
    reddit = praw.Reddit(user_agent="Reddit to Word Cloud", client_id=os.environ["REDDIT_CLIENT_ID"], client_secret=os.environ["REDDIT_CLIENT_SECRET"])
    submission = reddit.submission(url=reddit_url)
    comments = []
    submission.comments.replace_more(limit=32, threshold=5)
    comment_queue = submission.comments[:]
    while comment_queue:
        comment = comment_queue.pop(0)
        comments.append(comment.body)
        comment_queue.extend(comment.replies)
    return comments

def generate_frequency_map(comments: List[str], filtered_words: Set[str]) -> Dict[str, float]:
    frequency_map = dict()
    regex = re.compile('[^a-zA-Z]')
    for comment in comments:
        adjusted_words = [word.lower() for word in comment.split(" ")]
        for word in adjusted_words:
            word = regex.sub('', word)
            if word == "" or word in filtered_words:
                continue
            if word not in frequency_map:
                frequency_map[word] = 0
            frequency_map[word] += 1
    
    return frequency_map

def generate_image(frequency_map: Dict[str, float], settings: WordcloudSettings):
    wordcloud = WordCloud(margin=settings.margin, height=settings.height, width=settings.width).generate_from_frequencies(frequency_map)
    image = wordcloud.to_image()
    image.save(settings.output_filename)