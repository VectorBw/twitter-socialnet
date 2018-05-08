import json
import config
import sys
import re
import csv

adjacency_list = {}
graph_file = open(config.filegraph, "a")
writer = csv.writer(graph_file)
with open("test.json", "r") as f:
    p = json.dumps(json.loads(f.readline()),indent=4)
    print(p)
    for line in f:
        try:
            line_object = json.loads(line)
            screen_name = line_object["user"]["screen_name"]
            tweet = line_object["text"]
            targets = re.findall("@[a-z/A-Z/0-9]{1,15}", tweet)
            for ta in targets:
                adjacency_list[screen_name] = ta.strip('@')
                ad  = [screen_name,ta.strip('@')]
                writer.writerow(ad)
        except ValueError:
            pass














##        print(line_object['user']['screen_name'])
