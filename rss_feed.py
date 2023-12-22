import feedparser


user_url = feedparser.parse(input("Enter your Link:"))

for i in user_url:
    title = user_url.feed.title
    despt = user_url.feed.description
    link = user_url.feed.link

    print("title:", title)
    print("description:", despt)
    print("For More:", link)

"""
Links you can use to run it:::
link 1 :
Top Stories = https://www.cbc.ca/webfeed/rss/rss-topstories

link 2 : 
World = https://www.cbc.ca/webfeed/rss/rss-world

link 3 :
Canada = https://www.cbc.ca/webfeed/rss/rss-canada

link 4 :
business = https://www.cbc.ca/webfeed/rss/rss-business

Link 5 :

Health = https://www.cbc.ca/webfeed/rss/rss-health

Link 6 :

Arts & Entertainment = https://www.cbc.ca/webfeed/rss/rss-arts

Link 7 :

Technology & Science = https://www.cbc.ca/webfeed/rss/rss-technology

Link 8 :
Offbeat = https://www.cbc.ca/webfeed/rss/rss-offbeat

Link 9 :

Indigenous = https://www.cbc.ca/webfeed/rss/rss-Indigenous"""
