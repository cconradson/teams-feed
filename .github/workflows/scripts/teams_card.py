def build_simple_teams_card(title, lines):
    """
    Builds dictionary for a teams card with bolded title and lines underneath that can then be placed in the json variable for a post request
    """

    blist = [{
        'type': 'TextBlock',
        'text': title,
        'weight': 'bolder',
        'size': 'Large'
    }]

    for line in lines:
        blist.append({'type': 'TextBlock', 'text': line})

    return {
        'type': 'message',
        'attachments': [
            {
                'contentType': 'application/vnd.microsoft.card.adaptive',
                'content': {
                    '$schema': 'http://adaptivecards.io/schemas/adaptive-card.json',
                    'type': 'AdaptiveCard',
                    'version': '1.0',
                    'body': blist
                }
            }
        ]
    }