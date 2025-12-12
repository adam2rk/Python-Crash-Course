from pathlib import Path

filePath = Path('pi_digits.txt')
Contents = filePath.read_text()
print(Contents)