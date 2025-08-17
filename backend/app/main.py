from fastapi import FastAPI

app = FastAPI(
    title="Dashboard de Telefonia",
    description="API para consumir dados de telefonia"
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="localhost",
        port=8000,
        log_level="info",
        reload=True
    )
