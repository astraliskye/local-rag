# Local RAG

A local agent connected to your knowledge base that gives you personalized

## Local Setup

### Kubernetes

Prerequisites: a Kubernetes environment and kubectl

```shell
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### Docker

Prerequisites: Docker!

#### Docker Registry

Pull Docker image from the registry and run it

Note: if you are not using tinyllama you should change the MODEL_NAME environment variable to reflect the name of your chosen model. OLLAMA_HOST defaults to http://127.0.0.1:11434.

```shell
docker pull astraliskye/local-rag
docker run --rm --name local-rag --net <same network as ollama> -e MODEL_NAME=tinyllama -e OLLAMA_HOST=http://<ollama container hostname or localhost>:11434 -p 8000:8000 astraliskye/local-rag
```

#### Build image and run it

Build Docker image and run it

Note: if you are not using tinyllama you should change the MODEL_NAME environment variable to reflect the name of your chosen model

```shell
docker build -t local-rag .
docker run --rm --name local-rag --net <same network as ollama> -e MODEL_NAME=tinyllama -e OLLAMA_HOST=http://<ollama container hostname or localhost>:11434 -p 8000:8000 local-rag
```

### Containerless

Prerequisites:

- Ollama installed, running, and a model pulled
- Python 3.13

Clone the repo:

```shell
git clone https://github.com/astraliskye/local-rag
```

Install Python dependencies:

```shell
pip install -r requirements.txt   # pip
uv add -r requirements.txt        # uv
```

Run the API:

Note: if you are not using tinyllama you should change the MODEL_NAME environment variable to reflect the name of your chosen model

```shell
MODEL_NAME=tinyllama OLLAMA_HOST=http://127.0.0.1:11434 uvicorn app:app --port 8000    # Run uvicorn directly
MODEL_NAME=tinyllama OLLAMA_HOST=http://127.0.0.1:11434 fastapi run app.py --port 8000 # Run via fastapi
```

## Adding context to LLM generation

### Included script

Prerequisites:

- Python 3.13
- chromadb installed

```shell
python embed.py <dir/file> <dir/file> ...
```

The script will run through each provided argument, treating it as a filepath. If it is a file, the script will embed the file in the ChromaDB database. If it is a directory, the script will recursively add embed files contained within that directory and its subdirectories. Note the

### Through the API

The application has a built-in endpoint for adding embeddings to the database. You can use an HTTP client to send a POST request to the `/add` endpoint. The server expects the request body to be a valid JSON object of the form:

```JSON
{
  "content": "Some content to be embedded"
}
```

If successful, you will receive a HTTP 200 response.

## API endpoints

### `/query`

Query the model. Use URL parameter `q` to define the desired query:

```URL
curl http://<server IP>:8000/query?q=Some query
```

### `/add`

Embed more data into the model. Provide the content to be embedded in the content attribute of the JSON body:

```JSON
{
  "content": "Some content to be embedded"
}
```

### `/docs`

Docs generated automatically by OpenAPI. Use to interactively explore the API.

### `/health`

Returns a consistent response for ensuring the API is running in at least a minimum capacity.

```JSON
{
  "status": "ok"
}
```

## Case Study - Add Your Obsidian Knowledge Base

Provided in the `docs` folder are some documents to test the API with, but here I'll describe how to add your own Obsidian vault to the ChromaDB to be used as context for prompting the LLM.

### Reveal vault in your system folder

1. If not already on the main view where you can see a list of your vaults, click on your vault name and select Manage Vaults
2. Click on the three dot menu
3. Click on "Reveal vault in system explorer"

### Embed vault contents

The default location of vaults are in `/home/<user>/Documents` on Linux and `C:\Users\<username>\Documents` on Windows.

Run this command:

```shell
python embed.py /path/to/vault
```

This will embed every page of your vault (including stylesheets and other miscellaneous Obsidian files) into ChromaDB.

## Roadmap

- [x] Documentation: README written (embed.py, Obsidian usage, API endpoints)
- [ ] Testing: Add unit testing with pytest
- [ ] Testing: Improve API test strategy and cover more endpoints
- [ ] Tooling: Add argparse usage instructions to embed.py
- [ ] CI/CD: Add lint/test/build pipeline with artifact publishing
- [ ] Observability: Structured logging, tracing, and basic dashboards
- [ ] Security: Dependency scanning, authn, rate limiting, and secrets handling
- [ ] API: Publish OpenAPI spec with versioning and compatibility notes
- [ ] Performance: Load testing and latency/throughput benchmarks
- [ ] Deployment: Health checks, readiness probes, and Helm/K8s docs
