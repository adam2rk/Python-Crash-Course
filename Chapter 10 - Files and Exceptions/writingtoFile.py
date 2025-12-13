#writing to a file
from pathlib import Path

filePath = Path(r"Chapter 10 - Files and Exceptions\Programming.txt")
filePath.write_text("Hello World I love programming")