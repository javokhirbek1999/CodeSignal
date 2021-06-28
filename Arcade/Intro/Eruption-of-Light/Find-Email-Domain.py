def findEmailDomain(address):
    domain = address.split("@")
    return domain[-1]
