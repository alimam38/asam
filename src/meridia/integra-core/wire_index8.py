f = open(r'C:\Users\alima\Dropbox\Meridia\prototypes\Index8.html', encoding='utf-8')
content = f.read()
f.close()
old = "const API_BASE = window.INTEGRA_API || 'http://localhost:8000/api/v1';"
new = "const API_BASE = window.INTEGRA_API || 'https://integra.meridiahq.com/api/v1';"
if old in content:
    content = content.replace(old, new)
    g = open(r'C:\Users\alima\Dropbox\Meridia\prototypes\Index8.html', 'w', encoding='utf-8')
    g.write(content)
    g.close()
    print('Done - Index8 now points to integra.meridiahq.com')
else:
    print('String not found - check manually')
