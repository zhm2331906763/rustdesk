with open('.github/workflows/flutter-build.yml','r',encoding='utf-8',errors='ignore') as f:
    content = f.read()
# Check for YAML syntax near our changes
idx = content.find('RENDEZVOUS_SERVER')
if idx > 0:
    snippet = content[idx-80:idx+200]
    print("=== Context around RENDEZVOUS_SERVER ===")
    print(snippet)
    print("=== End ===")
# Check indentation - should be 2 spaces per level
for i, line in enumerate(content.split('\n')):
    if 'RENDEZVOUS_SERVER' in line or 'RELAY_SERVER' in line or 'API_SERVER' in line:
        spaces = len(line) - len(line.lstrip())
        print(f"Line {i}: {spaces} spaces: {line.strip()}")
