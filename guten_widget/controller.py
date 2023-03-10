"""controller.py will manage making API calls to the Gutendex and 
format the results for display."""

# import statements
import requests

#set some variables to help our API call
domain = "https://gutendex.com/"
endpoint = "books/?search="

# Make an API call
def make_call(query: str) -> str:
    """take the terms (of the search) and use it to make an API call
    then return formatted results or error if does not return a 200 code"""

    # create our url
    url = domain + endpoint + query

    # make the call
    response  = requests.get(url)
    results = ""
    if response.ok:
        results = get_top_results(response)
        results = format_results(results)
    else:
        results = "There was an error. Please try later."
    return results

def get_top_results(response, max=4) -> list:
    """takes an API response and returns a list of the fist max # of results"""
    results = response.json()["results"]
    return results[:max]

def format_results(results) -> str:
    """take results (a list), extract the info we need and return a 
    formatted string"""
    formatted_results = ""
    for item in results:
        title = item.get("title")
        formatted_results += "<p><b>Title: <i>" + title + "</i></b></p>"
        authors = item.get("authors")
        if len(authors) >1:
            formatted_results += "<p>Authors</p><ul>"
            for author_data in authors:
                author = author_data.get("name")
                formatted_results += "<li>" + author + "</li>"
            formatted_results =+ "</ul>"
        else:
            author = authors[0].get("name")
            formatted_results += "<p>by " + author + "</p>"
    return formatted_results

if __name__ == "__main__":
    call_results = make_call("douglas")
    print(call_results)