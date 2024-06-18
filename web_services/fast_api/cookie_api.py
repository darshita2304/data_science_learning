from fastapi import FastAPI, Response, Cookie
from typing import Annotated
app = FastAPI()


@app.get("/")
def func(response: Response):
    response.set_cookie(key="gfg_cookie_key", value="gfg_cookie_value")
    return {"message": "Cookie is set on the browser"}


@app.get("/cookie")
def func(gfg_cookie_key: Annotated[str , Cookie()] = None):
	return {"gfg_cookie": gfg_cookie_key}
