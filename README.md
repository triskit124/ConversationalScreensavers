# Conversational Screensavers

A quick project to generate nice looking screensavers (well, wallpapers mostly) with posts pulled from r/CasualConversation. 
These conversational wallpapers are a nice way to peer into someone's day.

I have my Mac set to cycle through wallpapers from a folder every 1 minute.

Typeface: [Source Serif 4](https://fonts.google.com/specimen/Source+Serif+4) by [Frank Grießhammer](https://fonts.google.com/?query=Frank+Grie%C3%9Fhammer)

## Generating Wallpapers
In `CreateImage.py`:
1. Specify a base image to place text over: `img = Image.open("bg.png")`
2. Specify folder to store wallpapers: `imagesFolder = 'img/'`
3. Specify a Sub and number of posts to pull: `posts = redditScraper.getPostsFromSub('CasualConversation', 50)`
4. `python3 CreateImage.py`

## Samples

![Example 1](examples/ex1.png "Example")

![Example 2](examples/ex2.png "Example")

![Example 3](examples/ex3.png "Example")

![Example 4](examples/ex4.png "Example")