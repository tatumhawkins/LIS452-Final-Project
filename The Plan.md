# LIS452-Final-Project
Vocab quiz creator

I'm using the book 'How to think like a computer scientist: Learning with Python 3 (RLE)' by Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers.
This can be found at http://openbookproject.net/thinkcs/python/english3e/ and the info at http://openbookproject.net/thinkcs/python/english3e/fdl-1.3.html allows me to borrow it for this project. I also emailed the corresponding author asking about permission, but since the site hasn't been updated since 2012 I'm not expecting a response. I very much hope I'm not breaking any copyright laws...
I copied each chapter into a .txt file and will be using those files as my textbook for this project. 
I considered using the Python for Everyone book, but frankly this book will be easier to work with. PfE differentiates between the vocab word and its defintion by bolding the vocab word. This text has the vocab word on one line and the definition on the next line without splitting hte definition across multiple lines. Since the bold goes away in a .txt file (and I wouldn't know how to detected for it anyway), the Wentworth book is more friendy for a first attempt at this type of program. 


Steps I anticipate/have completed:
X	Isolate the glossary. 
X	Split the glossary into words and definitions and use this to create a Python list (not dictionary). I'm fairly comfortable with lists, I don't really know what I'm doing with dictionaries.  
o	Process the rest of the text looking for long words and words that a used infrequently. 
o	Ask the user with each of these words whether they should be included on the dictionary. 
o	Get definitions for these additional words. (User input??)
o	Create a game/quiz that randomly selects a word from the dictionary, displays it, and asks the user to supply the correct word.
o	Keep track of which/how many words are correct.
o	At the end, display the user’s “score” and a list of missed words. 
