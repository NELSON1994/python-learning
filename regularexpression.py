# re.match(pattern, string, flags=0)

print("---search and replace")
# re.sub(pattern, repl, string, max=0)
import re as reg

phone = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
num = reg.sub(r'#.*$', "", phone)
print("phone number is : ", num)

# Remove anything other than digits
num = reg.sub(r'\D', "", phone)
print("phone number is : ", num)
