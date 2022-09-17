import warnings
import sys

from fb_scraper.scraper import download_posts

warnings.filterwarnings("ignore")


def main():
    group_ids = sys.argv[1:]
    print(group_ids)

    for group_id in group_ids:
        print(f"Downloading group={group_id}...")
        download_posts(group_id)
        print(f"Finished")


if __name__ == "__main__":
    main()
