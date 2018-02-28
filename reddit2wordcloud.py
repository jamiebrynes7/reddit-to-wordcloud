import argparse
import json
import sys

from common_lib import generate_wordcloud, WordcloudSettings

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="The reddit thread URL.", type=str)
    parser.add_argument("-o", "--output", help="The output filename. The default is wordcloud.png", type=str, default="wordcloud.png")
    parser.add_argument("-c", "--config", help="The JSON configuration file.", type=str)
    args = parser.parse_args()

    settings = construct_wordcloud_settings(args.config).add_url(args.url)
    generate_wordcloud(settings)

def construct_wordcloud_settings(json_file_url: str) -> WordcloudSettings:
    if not json_file_url:
        return WordcloudSettings()

    try:
        with open(json_file_url) as f:
            json_settings = json.load(f)
            return WordcloudSettings(**json_settings)
    except IOError:
        print("Error: Could not find config file: %s" % json_file_url)
        sys.exit(1)

if __name__ == "__main__":
    main()