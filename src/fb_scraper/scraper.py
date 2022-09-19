from datetime import datetime
from pathlib import Path

import pandas as pd
from facebook_scraper import get_posts

fields_to_extract = [
    "time",
    "user_id",
    "username",
    "post_url",
    "likes",
    "shares",
    "reactors",
    "text",
]

date_format = "%Y%m%d_%H%M%S"
base_datetime = datetime(1, 1, 1)


def download_posts(group_id: str):
    data = {field: [] for field in fields_to_extract}
    max_date = get_max_date()
    new_max_date = base_datetime

    for post in get_posts(group_id, pages=10):
        if post["time"] < max_date:
            continue

        for field in fields_to_extract:
            data[field].append(post[field])

            if post["time"] > new_max_date:
                new_max_date = post["time"]

    return data, new_max_date


def get_date(datetime_: datetime) -> str:
    return datetime.strftime(datetime_, date_format)


def get_max_date() -> datetime:
    xlsx_files = list(Path("./fb_exports").glob("*.xlsx"))

    if not xlsx_files:
        return base_datetime

    max_date_file = max(xlsx_file for xlsx_file in xlsx_files)

    return datetime.strptime(max_date_file.stem, date_format)


def write(data, max_date):
    date_str = get_date(max_date)
    path = Path("./fb_exports")
    path.mkdir(parents=True, exist_ok=True)

    # pylint: disable=abstract-class-instantiated
    with pd.ExcelWriter(f"{path.as_posix()}/{date_str}.xlsx") as writer:
        for group_id, sheet in data.items():
            print(f"Writing group={group_id}...")
            df = pd.DataFrame(sheet)
            df.to_excel(writer, sheet_name=group_id, index=False)
            print(df.head())
            print("Write finished.")
