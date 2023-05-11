def serverip():
    ip = "192.168.2.60" #"192.168.1.151"
    return ip

def give_data():
    contenttype = "text/json"
    return_data = b'["messagetext": []]'
    return (contenttype, return_data)