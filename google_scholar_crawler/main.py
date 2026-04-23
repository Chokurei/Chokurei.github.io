import json
import os
from datetime import datetime

import requests

SERPAPI_KEY = os.environ["SERPAPI_KEY"]
SCHOLAR_ID = os.environ["GOOGLE_SCHOLAR_ID"]
ENDPOINT = "https://serpapi.com/search.json"


def fetch_author():
    params = {
        "engine": "google_scholar_author",
        "author_id": SCHOLAR_ID,
        "api_key": SERPAPI_KEY,
        "num": 100,
    }
    articles = []
    start = 0
    base = None
    while True:
        params["start"] = start
        resp = requests.get(ENDPOINT, params=params, timeout=60)
        resp.raise_for_status()
        data = resp.json()
        if data.get("error"):
            raise RuntimeError(f"SerpAPI error: {data['error']}")
        if base is None:
            base = data
        batch = data.get("articles", [])
        articles.extend(batch)
        if len(batch) < params["num"] or "next" not in data.get("serpapi_pagination", {}):
            break
        start += params["num"]
    base["articles"] = articles
    return base


def extract_citedby(table):
    for row in table or []:
        if "citations" in row:
            return int(row["citations"].get("all", 0))
    return 0


def extract_index(table, key):
    for row in table or []:
        if key in row:
            return int(row[key].get("all", 0))
    return 0


def main():
    data = fetch_author()
    author_block = data.get("author", {})
    cited_by = data.get("cited_by", {})
    table = cited_by.get("table", [])

    total_citations = extract_citedby(table)
    h_index = extract_index(table, "h_index")
    i10_index = extract_index(table, "i10_index")

    publications = {}
    for art in data.get("articles", []):
        pub_id = art.get("citation_id")
        if not pub_id:
            continue
        publications[pub_id] = {
            "author_pub_id": pub_id,
            "title": art.get("title"),
            "authors": art.get("authors"),
            "publication": art.get("publication"),
            "year": art.get("year"),
            "num_citations": int((art.get("cited_by") or {}).get("value") or 0),
            "citedby_url": (art.get("cited_by") or {}).get("link"),
        }

    result = {
        "name": author_block.get("name"),
        "affiliations": author_block.get("affiliations"),
        "scholar_id": SCHOLAR_ID,
        "citedby": total_citations,
        "hindex": h_index,
        "i10index": i10_index,
        "publications": publications,
        "updated": str(datetime.now()),
    }

    os.makedirs("results", exist_ok=True)
    with open("results/gs_data.json", "w") as f:
        json.dump(result, f, ensure_ascii=False)

    shield = {
        "schemaVersion": 1,
        "label": "citations",
        "message": f"{total_citations}",
    }
    with open("results/gs_data_shieldsio.json", "w") as f:
        json.dump(shield, f, ensure_ascii=False)

    print(f"citedby={total_citations} hindex={h_index} i10={i10_index} pubs={len(publications)}")


if __name__ == "__main__":
    main()
