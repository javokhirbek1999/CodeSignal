from ipaddress import ip_address as ip
def isIPv4Address(inputString):
    try:ip(inputString)
    except:return False
    return True
