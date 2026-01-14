from notion_client import Client

NOTION_TOKEN = "YOUR_NOTION_TOKEN_HERE"
notion = Client(auth=NOTION_TOKEN)

print("=" * 50)
print("접근 가능한 모든 페이지 검색")
print("=" * 50)

response = notion.search(query="", filter={"property": "object", "value": "page"})
results = response.get("results", [])
print(f"\n접근 가능한 페이지: {len(results)}개\n")

for r in results[:15]:
    title = "N/A"
    if r.get("properties"):
        for v in r["properties"].values():
            if v.get("title") and v["title"]:
                title = v["title"][0]["plain_text"]
                break
    if r.get("child_page"):
        title = r["child_page"].get("title", title)
    
    page_id = r["id"]
    print(f"  - {title}")
    print(f"    ID: {page_id}")
    print()
