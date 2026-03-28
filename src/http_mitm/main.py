import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()


@app.post("/login")
async def login(request: Request):
    body = await request.json()
    print(f"\n>>> {body}")
    return {"status": "ok"}


def run():
    uvicorn.run(app, host="0.0.0.0", port=8080)


def run_ssl():
    import uvicorn

    uvicorn.run(
        app, host="0.0.0.0",
        port=8443,
        ssl_keyfile="key.pem",
        ssl_certfile="cert.pem"
    )
