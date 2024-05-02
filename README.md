### rag3 - Containerized LLM for Python

### Current Issues
- conversation id issues
- issue seems to be with this fuction get_or_create_conversation in endpoints
- the idea is to have a consistent conversation id.  



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
langchain
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

### Prompt Info

## run_full_text.sh
- `chmod +x run_full_text.sh`
- `./run_full_text.sh`




### Project Directory - Goal
```bash
.
├── Dockerfile
├── README.md
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── routes
│   │   ├── __init__.py
│   │   └── endpoints.py
│   └── services
│       ├── __init__.py
│       └── api_services.py
├── channels.json
├── directory_tree.txt
├── docker-compose.yaml
├── full_text.txt
├── models
│   ├── __init__.py
│   ├── channel.py
│   └── models.py
├── requirements.txt
└── run_full_text.sh

5 directories, 17 files
```