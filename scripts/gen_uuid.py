import secrets

def uuid():
    def p(s):
        p = secrets.token_hex(4)
        return '-' + p[:4] + '-' + p[4:] if s else p

    return p(False) + p(True) + p(True) + p(False)

print(uuid())