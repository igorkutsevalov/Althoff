import re


line = "Красивое лучше, чем уродливое."


matches = re.findall("Красивое", line, re.IGNORECASE)


print(matches)
