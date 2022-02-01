from PIL import Image, ImageFont, ImageDraw
from RedditScraper import RedditScraper


class TextBox:
    """
    Essentially a wrapper for various PIL modules. Allows a text box object to be defined to control
    size, position, text, etc.
    """

    def __init__(self, text, img, width=100, font=None, fill=(255, 255, 255, 255)):
        self.text = text
        self.imgSize = img.size
        self.width = width
        self.font = font
        self.fill = fill
        self.pos = None

        self.d = ImageDraw.Draw(img)
        self.wrappedText = self.wrapText()

    def drawText(self, pos=(0, 0)):
        """
        draws the current wrappedText content to the canvas
        """
        self.pos = pos
        self.d.multiline_text(pos, self.wrappedText, fill=self.fill, font=self.font)

    def wrapText(self):
        """
        takes in a string of text and adds newline tokens in order to repsect textbox width
        @ param: text to wrap
        @ return: wrappedText, a string containting the same as text but with newline tokens
        """
        wrappedText = ""
        for word in self.text.split(' '):
            if self.d.multiline_textsize(wrappedText + " " + word, self.font)[0] > self.width:
                wrappedText = wrappedText + "\n " + word
            else:
                wrappedText = wrappedText + " " + word
        return wrappedText

    def boxSize(self):
        """
        @return: tuple (width, height) containing size of textbox, in pixels
        """
        return self.d.multiline_textsize(self.wrappedText, self.font)

    def position(self):
        """
        @ return: tuple (width, height) containing position of textbox, in pixels
        """
        return self.pos


# Get new posts
redditScraper = RedditScraper()
posts = redditScraper.getPostsFromSub('AmITheAsshole', 30)

# folder to place completed images
imagesFolder = 'img/'

buffer = 150 # margin size in image, [pix]
boldFont = ImageFont.truetype('fonts/SourceSerif4-Bold.ttf', 48)
italicFont = ImageFont.truetype('fonts/SourceSerif4-MediumItalic.ttf', 48)

for i in range(len(posts)):
    img = Image.open("bg_blur.png") # open image
    post = posts.iloc[i]
    postTitle = post['title']
    postBody = post['body']

    bodyBox = TextBox(text=postBody, img=img, width=img.size[0] - 3 * buffer, font=italicFont)
    bodyBox.drawText((buffer, img.size[1] - bodyBox.boxSize()[1] - buffer))

    titleBox = TextBox(text=postTitle, img=img, width=img.size[0] - 3 * buffer, font=boldFont)
    titleBox.drawText((buffer, bodyBox.position()[1] - 150))

    if titleBox.position()[1] > 3 * buffer:
        img.save(imagesFolder + str(i) + ".png")
    #img.show()



