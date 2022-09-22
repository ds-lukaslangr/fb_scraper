import sys
import warnings

from fb_scraper.scraper import download_posts, base_datetime, write

warnings.filterwarnings("ignore")


def main():
    group_ids = sys.argv[1:]
    data = {}
    max_date = base_datetime

    for group_id in group_ids:
        downloaded_data, group_name, new_max_date = download_posts(group_id)
        data[group_name] = downloaded_data

        if new_max_date > max_date:
            max_date = new_max_date
        print("Download finished.")

    if max_date == base_datetime:
        print("No new posts.")
    else:
        write(data, max_date)


if __name__ == "__main__":
    main()
