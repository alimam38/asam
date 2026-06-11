
f = open(r'C:\Users\alima\Dropbox\Meridia\integra-core\Index8-live.html', encoding='utf-8')
content = f.read()
f.close()

# Point at production backend
content = content.replace(
    "window.INTEGRA_API_BASE = 'http://localhost:8000';",
    "window.INTEGRA_API_BASE = 'http://localhost:8002'; // production backend — switch to https://integra.meridiahq.com when NAS deployed"
)

# Inline the wiring script so it works as a single file (no external dependency)
wiring = open(r'C:\Users\alima\Dropbox\Meridia\integra-core\integra-wiring.js', encoding='utf-8').read()
content = content.replace(
    '<script src="integra-wiring.js"></script>',
    f'<script>\n{wiring}\n</script>'
)

g = open(r'C:\Users\alima\Dropbox\Meridia\integra-core\Index8-live.html', 'w', encoding='utf-8')
g.write(content)
g.close()
print(f"Index8 wired. File size: {len(content):,} chars")
