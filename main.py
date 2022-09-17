import warnings
from datetime import datetime

import csv
from facebook_scraper import get_posts

warnings.filterwarnings("ignore")

group_id = "1295673443855365" #TODO: add list, extract IDs
num_pages = 2 #convert to date - manual if possible

format_data = "%y%m%d_%H%M%S"
filename = f"facebook_export_{group_id}_{datetime.strftime(datetime.now(), format_data)}.csv"

extracted_fields = ["text", "likes", "reactors"]  # TODO: add fields that you want in the export csv
# TODO: limit by date - manual entry (weekends ect.), add groupIDs
data = {field: [] for field in extracted_fields}

for post in get_posts(group_id, pages=num_pages):
    print(post.keys())
    for field in extracted_fields:
        data[field].append(post[field])

df = pd.DataFrame(data)
df.to_csv("exports/" + filename, index=False)
print(df.head())
