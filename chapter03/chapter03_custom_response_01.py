from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse
import uvicorn

app = FastAPI()


@app.get("/html", response_class=HTMLResponse)
async def get_html():
    return """
        <html>
            <head>
                <title>Hello world!</title>
            </head>
            <body>
                <h1>Hello world!</h1>
            </body>
        </html>
    """


@app.get("/text", response_class=PlainTextResponse)
async def text():
    return "Hello world2!"


@app.get("/")
async def index():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("chapter03_custom_response_01:app", host="127.0.0.1", port=8000, reload=True)
