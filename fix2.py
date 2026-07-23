import re
c = open('.github/workflows/flutter-build.yml', 'r', encoding='utf-8', errors='ignore').read()
# Add quotes around each secrets reference
for var in ['RENDEZVOUS_SERVER', 'RELAY_SERVER', 'API_SERVER', 'RS_PUB_KEY', 'FIXED_PASSWORD']:
    old = '${{ secrets.' + var + ' }}'
    new = '"${{ secrets.' + var + ' }}"'
    c = c.replace(old, new)
open('.github/workflows/flutter-build.yml', 'w', encoding='utf-8').write(c)
print('Done')
