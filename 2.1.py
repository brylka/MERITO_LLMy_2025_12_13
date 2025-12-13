text = """```json
{
  "is_correct": false,
  "result": 4
}
```"""
if text.startswith("```json"):
    text = text.split("\n", 1)[1]
    text = text.split("```")[0]


print(text)