with open('.github/workflows/flutter-build.yml','r',encoding='utf-8',errors='ignore') as f:
    content = f.read()
# Add quotes around ${{ secrets.XXX }} items
import re
content = re.sub(r'(?m)^(  [A-Z_]+): \${{', r'\1: "${{', content)
content = content.replace('secrets.RENDEZVOUS_SERVER }}', 'secrets.RENDEZVOUS_SERVER }}"')
content = content.replace('secrets.RELAY_SERVER }}', 'secrets.RELAY_SERVER }}"')
content = content.replace('secrets.API_SERVER }}', 'secrets.API_SERVER }}"')
content = content.replace('secrets.RS_PUB_KEY }}', 'secrets.RS_PUB_KEY }}"')
content = content.replace('secrets.FIXED_PASSWORD }}', 'secrets.FIXED_PASSWORD }}"')
open('.github/workflows/flutter-build.yml','w',encoding='utf-8') as f:
    f.write(content)
print('OK')
