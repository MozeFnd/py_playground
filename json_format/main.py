import json

filename = "comm_card_core_dir/data_render"
# JSON string as input
with open(filename) as f:
    json_str = f.read()
    # '{"name": "John", "age": 30, "city": "New York"}'

# Parse the JSON string
data = json.loads(json_str)

# Output formatted JSON with an indent
formatted_json = json.dumps(data, indent=4, ensure_ascii=False)
# formatted_json = formatted_json.encode("utf-8").decode("unicode_escape")
with open(filename + '_formatted', 'w') as f:
    f.write(formatted_json)
# print(formatted_json)