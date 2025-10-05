# Jenkins Python Game

Simple number-guessing Python CLI game with tests, Dockerfile, and Jenkins pipeline for building, testing, and pushing Docker images to Docker Hub.

Overview
- Python 3.10+
- pytest for tests
- Dockerfile to build an image
- Jenkinsfile for a declarative pipeline that runs tests, builds the image, tags it with commit SHA and pushes to Docker Hub

Setup
1. Create a Docker Hub repository (ex: `dockerhub-username/jenkins-python-game`).
2. Add Jenkins credentials:
   - docker-hub-credentials (username/password or token) in Jenkins Credentials store.
3. Set up a GitHub webhook to trigger Jenkins on push.

Local commands

Build and run tests:

```powershell
python -m venv venv; .\venv\Scripts\Activate.ps1; pip install -r requirements.txt; pytest -q
```

Build Docker image locally:

```powershell
docker build -t yourhubuser/jenkins-python-game:latest .
```

Jenkins
- The `Jenkinsfile` uses a credential ID placeholder `docker-hub-credentials`. Replace with your Jenkins credentials ID.

License: MIT
