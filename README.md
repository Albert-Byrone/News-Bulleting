# News

## Author

This application with help to those who dont get time to watch TV.The website shows different articles from different authors .It consumes data from the [NEWS API](https://newsapi.org/)

## Live Demo

Click  https://news-bullets.herokuapp.com/  to visit the site

## User Story

1. A user would see various news sources on the homepage of the application.
2. A user would also be able to select a news source and see all news articles from the selected news source in the application.
3. A user will be able to see the image, description and the time a news article was created from the News-Articles tab.
4. A click on an article and read the full article on the source website.

## Development Installation
1. Cloning the repository:
```bash
 git clone
 ```

2. MOve to folder and install the rquirements
```bash 
cd News_Bulletins
pip install requirements.txt
```

3. Export the configurations
``` bash
export NEWS_API_KEY = '<Enter your API key>'
```
4.Testing the application
```bash
python3.6 manage.py test
```
5.Running the Application
```bash
python3,6 manage.py server
```
6. Open your application on your browser `127.0.0.1:5000`

## Technology used

* [Python3.6](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)

# Contact Information 

If you have any question or contributions, please email me at albertbyrone1677@gmail.com

## License
* *MIT License:*
* Copyright (c) 2019 **Albert Byrone**