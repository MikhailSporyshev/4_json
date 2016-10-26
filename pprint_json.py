import json

def load_data(filepath):
    return json.load(open(filepath))


def pretty_print_json(data):
    print(json.dumps(data,ensure_ascii = False, indent = 4))


if __name__ == '__main__':
    data = load_data(input())
    pretty_print_json(data)
