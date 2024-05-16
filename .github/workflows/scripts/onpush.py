import sys
import json
import requests
import teams_card

repo = sys.argv[2]
pusher = sys.argv[3]
commits = sys.argv[4].split('~~')

message = teams_card.build_simple_teams_card(f"New commits pushed to [{repo}](github.com/{repo}) by {pusher}", commits)

response = requests.post(sys.argv[1], json = message)
print(response)