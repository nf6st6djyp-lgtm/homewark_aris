from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for name, value in attrs:
            print(f"-> {name} > {value}")

    def handle_startendtag(self, tag, attrs): 
        print(tag)
        for name, value in attrs:
            print(f"-> {name} > {value}")


n = int(input())
html = ""
for _ in range(n):
    html += input().strip() + '\n'


parser = MyHTMLParser()
parser.feed(html)
