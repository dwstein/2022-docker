### rag3 - Containerized LLM for Python

## Project Description

Create an application that uses LLMs to read my documents and researches them.  I want the system to be private so I’m comfortable sharing my personal information like legal documents, bank statements…etc.  I also want to choose different models, including the latest LLMs and embedding models to have the best possible experience.


### Project Info

## requiremetns.txt
```bash
fastapi
pydantic
uvicorn
watchfiles
httpx
```


### Project Usage

```
pip install -r requirements.txt
```

This is how you run the code locally (without Docker):

```
uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```

Build and run the Docker image locally, as follows:

```
docker build -t channel-api .
docker run -d -p 8080:80 channel-api
```

In order to run the example server with docker compose, use this:

```
docker-compose up --build
docker-compose up -d 
```




### Project Directory - Goal
```bash
/project_root
│
├── app/
│   ├── __init__.py
│   ├── main.py               # Your FastAPI application entry point
│   ├── models/
│   │   ├── __init__.py
│   │   └── models.py         # Data models, if any
│   ├── services/
│   │   ├── __init__.py
│   │   └── api_services.py   # Services for external API interactions
│   └── routes/
│       ├── __init__.py
│       └── endpoints.py      # FastAPI routes
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```