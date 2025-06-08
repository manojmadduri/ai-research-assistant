# Placeholder for API dependenciesfrom fastapi import Depends, Header, HTTPException

def verify_token(x_token: str = Header(...)):
    if x_token != "secret-token":
        raise HTTPException(status_code=401, detail="Invalid or missing token")
    return x_token
