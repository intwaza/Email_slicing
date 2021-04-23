Email=input("Enter your Email:").strip()
username=Email[:Email.index("@")]
domain_name=Email[Email.index("@")+1:]
print("Your username is {} and domain_name is {}".format(username, domain_name))
