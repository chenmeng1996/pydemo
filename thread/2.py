import re

log = "'app_id': 1234 hhh 'app_id': 1234"
a = re.findall(r"'app_id': (\d+)", log)
print(a)
