#Test code for browsing the web
import webbrowser
'import sys, pyperclip'

google=input('Google search: ')
webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % google)

"""
if len(sys.argv) > 1:
    address=''.join(sys.argv[1:])
else:
    address =pyperclip.paste()

webbrowser.open('https://www.goglles' + address)
"""
