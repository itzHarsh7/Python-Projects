import pywhatkit as p
text = '''Hello Guys...
Welcome To the pseducode of Converting Text into Handwriting.

This is how it actully look's like.

we have used a Function named "text_to_handwriting which is imported from pywhatkit library.
it accepts parameters like text, format in which you want tour text converted , color code [R,G,B].

Important Point:-->>
This library will use internet to do its task done. Without Internet Connection, It will not work and will throw a Big Error!!!

'''
p.text_to_handwriting(text, 'TextToHandwriting.png', [0,0,198])
print("END")