import sys
import json
import requests
import teams_card

repo = sys.argv[2]
branch = sys.argv[3]
pusher = sys.argv[4]
commits = sys.argv[5].split('~~')

message = teams_card.build_simple_teams_card(f"New commits pushed to the {branch} branch of [{repo}](github.com/{repo}) by {pusher}", commits)

response = requests.post(sys.argv[1], json = message)
print(response)