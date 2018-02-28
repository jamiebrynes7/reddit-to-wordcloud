# Reddit To Wordcloud

This tool will turn a Reddit thread into a wordcloud.

This project relies heavily on the [word cloud generator](https://github.com/amueller/word_cloud) Python module written by Andreas Mueller.

## Getting Started

**Prerequisites** 
You must have Python 3.5 or greater installed on your system. 

1. Clone this repository with `git clone git@github.com:jamiebrynes7/reddit-to-wordcloud.git`
2. (optional) Create a virtual environment
3. Install the Python requirements with `pip install -r requirements.txt`

### Getting a Reddit API Key

1. Go to [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps) to register for an API key.
2. Select script as the type and enter a name and description and a redirect uri (localhost works fine for this).
3. Copy the client id and export it as an environment variable `export REDDIT_CLIENT_ID="..."`
4. Copy the secret and export it as an environment variable `export REDDIT_CLIENT_SECRET="..."`

### Running the CLI Tool

The CLI tool can be ran with `python reddit2wordcloud.py --url=reddit_url --output=wordcloud.png`. You can optionally include a `--config` argument with a path to a JSON configuration file for the word cloud. An example of this config file can be found [here](config.json).
