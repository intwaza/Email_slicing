Email=input("Enter your Email:").strip()
username=Email[:Email.index("@")]
domain_name=Email[Email.index("@")+1:]
print(domain_name)
print(username)
