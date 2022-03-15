# Markdown Syntax

[Markdown Cheat Sheet notes](https://www.markdownguide.org/cheat-sheet/)  

[More syntax notes](https://www.markdownguide.org/basic-syntax/)

To open markdown split-screen with preview:
![screenshot](ScreenShot.jpg)

To view the file in markdown preview mode:==Cmd+Shift+v==
---

![Picture of a tree](tree.jpg)
**Bold text requires use of astrics**

Adding an emoij :joy:

These words are ==super important==.
Here is a quote:
> blockquote.

Here is some code:

    def color_converter(red, green, blue):
        hex_r = number_to_hex_string(red)
        hex_g = number_to_hex_string(green)
        hex_b = number_to_hex_string(blue)
        print("#" + hex_r + hex_g + hex_b)
        return #+hex_r+hex_g+hex_b
 
<br>


    def number_to_hex_string(num): 
    prefix = '0x'
        hex_string = hex(num)
        if hex_string.startswith(prefix):
            hex_string = hex_string[len(prefix):]
        if len(hex_string) < 2:
            hex_string = '0' + hex_string
        return hex_string.upper()

    color_converter(100,50,5)'

---

Notes from Adie Meeting today, 2/14/22:

1. Use markdown for notes and push to git
2. Pay attention when learning about git and github
3. Don't get behind!
4. Make friends & help eachother.

[Article talking about how to push notes from VSCode to git:](https://praveenjuge.com/blog/how-i-take-notes-using-vs-code-and-github/)

[other recommended programs for markdown notes](https://www.dendron.so/)

Here's a sentence with a footnote. [^1]

My-Do List:
~ Learn markdown~
~Take notes~
Learn to push to github

[^1]: This is the footnote.
