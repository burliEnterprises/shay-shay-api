![](/static/shay.png)

ShayShay API
============

A free REST API for random Shannon Sharpe quotes. 
You can take a look at the finished product on the website: [ShayShay API](http://burli.pythonanywhere.com/shayshay)

Introduction
------------

Welcome to the Shay Shay API! You can use my API to get random quotes & sayings from the legendary NFL hall of famer Shannon Sharpe. 

There is no authentication or authorization for the API, it’s 100% open
and free. Please don't abuse your use.

If you want to contribute or check out the source, visit the project on
[GitHub](https://github.com/burliEnterprises/shay-shay-api).


API Usage
---------
### Get a random quote
This endpoint gets you a random Shannon Sharpe quote. The quote is just
a generic quote; it’s not specified by category or anything.

#### HTTP Request:

    GET http://burli.pythonanywhere.com/shayshay/random 

#### Query Parameters:
|Parameter|Type  |Description |
|--|--|--
|limit  |integer  |The amount of quotes you want to grab from the API (max. 20)

#### Result:

    GET http://burli.pythonanywhere.com/shayshay/random?limit=3 
    {
        "source": "ShayShay API",
        "quotes": [
            "I won't talk about ... ",
            "I'm just ... Hall of Fame",
            "Without TD, we ... That's fact"
        ]
    }


## Note to self

**Tools & Frameworks:**
- CSS Framework: [Mu](https://github.com/BafS/mu)
- Python Web Server: [Flask](https://github.com/pallets/flask)
- Server Hosting: [Python Anywhere](https://www.pythonanywhere.com/user/burli/files/home/burli)
 
**Tutorials & Sources:**
- Souces for quotes:
-- [Reddit](https://www.reddit.com/r/Skiuuup/comments/aa2h96/shannon_sharpe_quotes_from_undisputed/)
-- [Quotetab](https://www.quotetab.com/quote/by-shannon-sharpe/)
-- [Fox Sports](https://www.foxsports.com/nfl/story/shannon-sharpe-undisputed-skip-bayless-033020)
-- [Brainyquote](https://www.brainyquote.com/authors/shannon-sharpe-quotes)
-- [Brian Dodd](https://briandoddonleadership.com/2011/08/08/15-hall-of-fame-leadership-quotes-from-shannon-sharpe/)
- Flask Tutorials 
-- [HTML Templates in Flask](https://pythonhow.com/html-templates-in-flask/)
-- [Images in Flask](https://stackoverflow.com/questions/28207761/where-does-flask-look-for-image-files)
-- [CSS in Flask](https://stackoverflow.com/questions/13772884/css-problems-with-flask-web-app)


## Moving forward:

- Demo on website, kanye.rest for comparison
- Implement more filters (quotation categories?)
- Medium

* * * * *

Made with ❤️ by [Burli](burli.biz)

