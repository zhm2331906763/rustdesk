content = open('.github/workflows/flutter-build.yml','r', encoding='utf-8').read()
insert = """  # Custom env vars for custom client build (read from secrets via build-custom.yml)
  RENDEZVOUS_SERVER: ${{ secrets.RENDEZVOUS_SERVER }}
  RELAY_SERVER: ${{ secrets.RELAY_SERVER }}
  API_SERVER: ${{ secrets.API_SERVER }}
  RS_PUB_KEY: ${{ secrets.RS_PUB_KEY }}
  FIXED_PASSWORD: ${{ secrets.FIXED_PASSWORD }}
"""
content = content.replace('  VCPKG_BINARY_SOURCES:', insert + '  VCPKG_BINARY_SOURCES:')
open('.github/workflows/flutter-build.yml','w').write(content)
print("OK")
