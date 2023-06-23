import requests
import sys
import re


def count_keywords(subreddit, word_list, after=None, count_dict={}):
    """Queries the Reddit API, parses the title of all hot articles,
       and counts the occurrences of given keywords.
    """
    if after is None:
        headers = {'User-Agent': 'Mozilla/5.0'}
        params = {'limit': 100, 'g': 'GLOBAL'}
        response = requests.get(f'https://www.reddit.com/r/{subreddit}/hot.json', headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json()
        after = data.get('data', {}).get('after', None)
        if after is None:
            return

    for post in data.get('data', {}).get('children', []):
        title = post.get('data', {}).get('title', '').lower()
        for word in word_list:
            count = title.count(word.lower())
            if count > 0:
                count_dict[word] = count_dict.get(word, 0) + count

    if after is not None:
        count_keywords(subreddit, word_list, after, count_dict)
    else:
        sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = sys.argv[2].split()
        count_keywords(subreddit, word_list)
