import re
def mask_aadhar(email):
    pattern = r"([a-zA-Z])([a-zA-Z0-9]+)(\@)([a-zA-Z0-9]+)(\.)([a-z]+)"
    match = re.search(pattern,email)
    return match.group(1) + len(match.group(2))*"#" + match.group(3)+match.group(4)+match.group(5)+match.group(6)


# print(mask_aadhar(int(input("Enter aadhar number:"))))
print(mask_aadhar(input("Enter email:")))