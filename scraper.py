from parsel import Selector
import requests
import time

BASE_URL = 'https://www.youtube.com'
FETCH_AWAIT_TIME = 1

VIDEO_URLS = '//a[@id="thumbnail"]/@href'


def fetch(url):
    try:
        time.sleep(FETCH_AWAIT_TIME)
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            # with open("dump.html", "w") as file:
            #     file.write(response.text)
            return response.text
        else:
            return None
    except requests.Timeout:
        return None


# Example /watch?v=Dgc0_jMwQLE&amp;list=PLOrUltkUqy_OkXAc8IJJ-xHI_RYyeczw8&amp;index=1
def url_formatter(url):
    return BASE_URL + url.split("&")[0]


def get_url_list():
    with open("Yacht_playlist_list.html", "r") as file:
        content = file.read()
    selector = Selector(text=content)
    urls_list = selector.xpath(VIDEO_URLS).getall()

    return list(map(url_formatter, urls_list))


def get_title(content):
    return content.split("><title>")[1].split(" - YouTube</title>")[0]


def get_date(content):
    return content.split('"publishDate":"')[1].split('",')[0]


def scrape_video(content, url):
    try:
        video = {}
        video['url'] = url
        video['title'] = get_title(content)
        video['pub_date'] = get_date(content)
        return video
    except TypeError:
        return video


def get_videos(amount):
    results = []
    while len(results) < amount:
        url_list = get_url_list()
        for url in url_list:
            if len(results) >= amount:
                break
            results.append(scrape_video(fetch(url), url))
    return results




