import re

def validate_passwords(passwords):
    valid_passwords = []
    for password in passwords.split(","):
        if not (6 <= len(password) <= 12):
            continue
        if not re.search("[a-z]", password):
            continue
        if not re.search("[A-Z]", password):
            continue
        if not re.search("[0-9]", password):
            continue
        if not re.search("[$#@]", password):
            continue
        passwords
        valid_passwords.append(password)

    return ",".join(valid_passwords)

input_password = "asqwr1234@1,aF145#,2w3E*,2We3345"
output = validate_passwords(input_password)
print("Valid Passwords:", output)
