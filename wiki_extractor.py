import os
from collections import OrderedDict
import wikipedia
import json
def search_wiki(keywords, number_of_search, wiki_pages):
    suggestion = False
    result_set = wikipedia.search(keywords, number_of_search, suggestion)
    # print(result_set)
    for term in result_set:
        try:
            page = wikipedia.page(term, preload=False)
            # print(page)
            page_title = page.url
            # page_summary = page.summary
            page_content = page.content
            wiki_pages[str('url:')+page_title] = str('paragraph:')+ str(page_content)
        except wikipedia.exceptions.DisambiguationError as error:
            pass
        except wikipedia.exceptions.PageError as error:
            pass
    return wiki_pages
def fetch_wiki(keywords, number_of_search,out_json):
    wiki_pages = OrderedDict()
    search_wiki(keywords, number_of_search, wiki_pages)
    myList = []
    for a in wiki_pages:
      c = OrderedDict()
      c[a] = wiki_pages[a]
      myList.append(c)
    json_object = json.dumps(myList,separators=(",",","), indent = 2) 
    # Writing to json
    with open(out_json, "w") as outfile:
        outfile.write(json_object)
    return wiki_pages

keyword = str(input())
n_related = int(input())
out_json = str(input())
fetch_wiki(keyword,n_related,out_json)