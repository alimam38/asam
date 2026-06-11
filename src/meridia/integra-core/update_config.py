
f = open(r'C:\Users\alima\Dropbox\Meridia\integra-core\meridia-wiring\config.py', encoding='utf-8')
content = f.read()
f.close()

replacements = [
    ('DB_HOST: str = os.getenv("DB_HOST", "192.168.1.100")', 'DB_HOST: str = os.getenv("DB_HOST", "192.168.0.160")'),
    ('DB_PORT: int = int(os.getenv("DB_PORT", "5432"))', 'DB_PORT: int = int(os.getenv("DB_PORT", "5433"))'),
    ('DB_NAME: str = os.getenv("DB_NAME", "meridia")', 'DB_NAME: str = os.getenv("DB_NAME", "meridia_core")'),
    ('DB_USER: str = os.getenv("DB_USER", "meridia_app")', 'DB_USER: str = os.getenv("DB_USER", "meridia")'),
    ('DB_PASS: str = os.getenv("DB_PASS", "CHANGE_ME")', 'DB_PASS: str = os.getenv("DB_PASS", "Ethanj2020##")'),
    ('FRED_API_KEY: str = os.getenv("FRED_API_KEY", "YOUR_FRED_KEY_HERE")', 'FRED_API_KEY: str = os.getenv("FRED_API_KEY", "f0b8d36d1bf405c35820e2ec3e93379f")'),
    ('CENSUS_API_KEY: str = os.getenv("CENSUS_API_KEY", "YOUR_CENSUS_KEY_HERE")', 'CENSUS_API_KEY: str = os.getenv("CENSUS_API_KEY", "27ccdb0ed92ac87ede38443a31af535ebca4e3b4")'),
    ('TARGET_MSA: str = "12060"', 'TARGET_MSA: str = "12054"'),
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        print('Updated: ' + old[:50])
    else:
        print('NOT FOUND: ' + old[:50])

g = open(r'C:\Users\alima\Dropbox\Meridia\integra-core\meridia-wiring\config.py', 'w', encoding='utf-8')
g.write(content)
g.close()
print('config.py saved')
