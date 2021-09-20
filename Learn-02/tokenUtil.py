tokenCache = {}

def genToken(username):
    token = username[::-1]
    tokenCache[token] = username
    return token

def validateToken(token):
    tokenInfo = token[::-1]
    if(tokenInfo == tokenCache[token]):
        return True
    else:
        return False