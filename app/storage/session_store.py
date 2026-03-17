sessions = {}

def add_request(ip):
    sessions[ip] = sessions.get(ip, 0) + 1

def get_requests(ip):
    return sessions.get(ip, 0)