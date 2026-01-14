"""
Notion API 테스트 스크립트
"""
from notion_client import Client

NOTION_TOKEN = "YOUR_NOTION_TOKEN_HERE"
notion = Client(auth=NOTION_TOKEN)

print("=" * 50)
print("Notion API 연결 테스트")
print("=" * 50)

try:
    response = notion.search(query="새 페이지")
    print(f"\n검색 결과: {len(response.get('results', []))}개")
    
    for i, r in enumerate(response.get('results', [])):
        print(f"\n[{i+1}] ID: {r['id']}")
        print(f"    Object: {r.get('object')}")
        print(f"    Type: {r.get('type', 'N/A')}")
        
        # 제목 추출 시도
        if r.get('properties'):
            for k, v in r['properties'].items():
                if v.get('type') == 'title' and v.get('title'):
                    title_text = v['title'][0]['plain_text'] if v['title'] else 'N/A'
                    print(f"    Title: {title_text}")
        
        # child_page인 경우
        if r.get('child_page'):
            print(f"    Child Page Title: {r['child_page'].get('title', 'N/A')}")
            
except Exception as e:
    print(f"\n오류 발생: {type(e).__name__}")
    print(f"메시지: {e}")
    
    if "Could not find" in str(e) or "unauthorized" in str(e).lower():
        print("\n해결 방법:")
        print("1. 노션에서 '새 페이지' 열기")
        print("2. 우측 상단 '...' 클릭")
        print("3. 'Connections' 또는 '연결' 클릭")
        print("4. Integration 검색하여 추가")
