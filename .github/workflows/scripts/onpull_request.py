import sys
import json
import requests
import teams_card

repo = sys.argv[2]
action = sys.argv[3]
req_title = sys.argv[4]
requester = sys.argv[5]
commit_url = sys.argv[6]

if action == 'opened':
    message = teams_card.build_simple_teams_card(f"New pull request in [{repo}](github.com/{repo})", [f"{requester} wants to merge {req_title}"])

    response = requests.post(sys.argv[1], json = {'content': out_text})
    print(response)