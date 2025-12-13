import json

text = """```json
{
  "is_correct": false,
  "result": 4
}
```"""
if text.startswith("```json"):
    text = text.split("\n", 1)[1]
    text = text.split("```")[0]


# print(text['is_correct'])

result = json.loads(text)
print(f"Czy poprawne: {result['is_correct']}, poprawna odpowiedź: {result['result']}")
