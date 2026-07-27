from fastapi import FastAPI

app = FastAPI(
    title="AI Resume Analyzer API"
)


@app.get("/")
def home():
    return {
        "message": "AI Resume Analyzer API Running"
    }
