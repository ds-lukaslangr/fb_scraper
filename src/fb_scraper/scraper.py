from datetime import datetime
from pathlib import Path

from facebook_scraper import get_posts
import pandas as pd

fields_to_extract = [
    "text",
    "likes",
    "reactors",
]


def download_posts(group_id: str):
    data = {field: [] for field in fields_to_extract}

    for post in get_posts(group_id, pages=2):
        for field in fields_to_extract:
            data[field].append(post[field])

    date = get_date()
    path = Path(f"./fb_exports/{date}")
    path.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame(data)
    df.to_excel(f"{path.as_posix()}/{group_id}.xlsx", index=False)
    print(df.head())


def get_date() -> str:
    date_format = "%Y%m%d_%H%M%S"
    return datetime.strftime(datetime.now(), date_format)
