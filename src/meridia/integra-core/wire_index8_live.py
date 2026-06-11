
f = open(r'C:\Users\alima\Downloads\Index8-live.html', encoding='utf-8')
content = f.read()
f.close()
old = "window.INTEGRA_API_BASE = 'http://localhost:8000';"
new = "window.INTEGRA_API_BASE = 'https://integra.meridiahq.com';"
if old in content:
    content = content.replace(old, new)
    g = open(r'C:\Users\alima\Downloads\Index8-live.html', 'w', encoding='utf-8')
    g.write(content)
    g.close()
    print('Done')
else:
    print('Not found')
