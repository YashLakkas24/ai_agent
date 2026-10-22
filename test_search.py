from tools import search_tool

try:
    result = search_tool.invoke("AI industry trends 2026")
    print(result)
except Exception as e:
    print(f"Search failed: {type(e).__name__:{e}}")
