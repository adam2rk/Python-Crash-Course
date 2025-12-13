from pathlib import Path
import os
print(os.getcwd())


filePath = Path(r'Chapter 10 - Files and Exceptions\pi_digits.txt')
Contents = filePath.read_text()

#printing each line that's what splintlines provides
# lines each indivudal line and then it prints it
lines = Contents.splitlines()
for line in lines:
    print(line)

print(Contents)