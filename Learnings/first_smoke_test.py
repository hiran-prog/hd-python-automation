import sys
import platform

print("=========================================")
print("   PYTHON ENVIRONMENT SMOKE TEST: PASSED ")
print("=========================================")
print(f"OS Platform: {platform.system()} {platform.release()}")
print(f"Python Ver:  {sys.version.split()[0]}")
print("Ready to build some aerospace automation frameworks!")
print("=========================================")