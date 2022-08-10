import csv

from scraper import get_videos
from extractor import price_extractor, model_extractor


def dict_list_maker(list):
    dict_list = []
    for video in list:
        model = model_extractor(video["title"])
        price = price_extractor(video["title"])
        dict_list.append({**video, **model, **price})
    return dict_list

def CSV_writer(target_csv, dict_list):
    with open(target_csv, "w", newline="") as file:
        field_names = [
            "brand",
            "model",
            "year",
            "price",
            "currency",
            "pub_date",
            "title",
            "url",
        ]
        writer = csv.DictWriter(file, fieldnames=field_names)

        writer.writeheader()
        writer.writerows(dict_list)


def scrape_playlist(source_html, target_csv, max):
    raw_list = get_videos(source_html, max)
    dict_list = dict_list_maker(raw_list)
    CSV_writer(target_csv, dict_list)
