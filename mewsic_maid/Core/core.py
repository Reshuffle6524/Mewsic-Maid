
import requests
def searchsuggestions(query:str, engine:str) -> List[dict]:

    if engine == 'google':
        suggestion_url = 'https://suggestqueries.google.com/complete/search?output=firefox&q=s'

    else :
        """startpage is better"""
        suggestion_url = 'https://www.startpage.com/osuggestions'

    suggestion_url = 'https://www.startpage.com/osuggestions'

    params = {
        'q': query
    }

    response = requests.get(suggestion_url, params=params)
    suggestions = response.json()

    # Print the suggestions
    for suggestion in suggestions[1]:
        print(suggestion)
    pass
    return suggestions


