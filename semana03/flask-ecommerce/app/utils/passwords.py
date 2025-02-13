import bcrypt

def hash_password(password: str):
    pwd_bytes = password.encode('utf-8')
    pwd_hasshed = bcrypt.hashpw(pwd_bytes, bcrypt.gensalt())
    return pwd_hasshed.decode('utf-8')