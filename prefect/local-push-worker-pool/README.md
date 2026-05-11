# Prefect Local Push Worker Pool Setup

This guide provides instructions to set up a local Prefect environment with a push worker pool using Docker Compose. It includes a sample Prefect flow and all the necessary CLI commands.

## Prerequisites

Before you begin, ensure you have the following installed:

*   **Docker Desktop:** Includes Docker Engine and Docker Compose.
    *   [Download Docker Desktop](https://www.docker.com/products/docker-desktop)
*   **Prefect CLI:** Installed via pip.
    ```bash
    pip install prefect
    ```

## Setup Instructions

Follow these steps to get your local Prefect environment up and running.

### 1. Navigate to the Project Directory

First, change your current directory to where this `README.md` file and the `docker-compose.yml` are located:

```bash
cd /Users/vignesh/code/python/prefect/local-push-worker-pool
```

### 2. Start the Prefect Server and Worker

Use Docker Compose to start the Prefect server, PostgreSQL database, and the Prefect worker. The worker is configured to listen for work on a pool named `local-push-pool`.

```bash
docker compose up -d
```

This command will:
*   Download the necessary Docker images (`prefecthq/prefect` and `postgres`).
*   Start a PostgreSQL container for the Prefect server's database.
*   Start the Prefect server, accessible on `http://localhost:4200`.
*   Start a Prefect worker that automatically connects to the server and listens on the `local-push-pool`.

### 3. Configure Prefect CLI to Connect to Your Local Server

You need to tell your local Prefect CLI where to find the Prefect API.

```bash
prefect config set PREFECT_API_URL="http://localhost:4200/api"
```

### 4. Create the Push Work Pool

Before deploying your flow, you need to create the `local-push-pool` on the Prefect server. This is the pool that your worker is listening to.

```bash
prefect work-pool create "local-push-pool" --type push
```

### 5. Create a Local Filesystem Storage Block

For the worker to find your flow code, you need to register a `local-file-system` storage block with the Prefect server. This block tells Prefect where the flow code is located *inside the worker container*.

```bash
prefect storage create --type local-file-system --name local-storage --path /opt/prefect/flows
```

### 6. Deploy the Sample Flow

Now, deploy the `my_simple_flow` from `flows/flow.py`. This command registers the flow with the Prefect server and creates a deployment that the worker can pick up.

```bash
python flows/flow.py
```

Upon successful deployment, you should see output indicating that the deployment `my-first-flow/my-first-deployment` has been created.

### 7. Run the Deployed Flow

You can trigger a run of your deployed flow using the Prefect CLI. The worker will automatically pick up this run.

```bash
prefect deployment run "my-first-flow/my-first-deployment"
```

Alternatively, you can trigger runs directly from the Prefect UI.

### 8. View the Prefect UI

Open your web browser and navigate to `http://localhost:4200` to access the Prefect UI. Here you can monitor your flow runs, deployments, and worker status.

## Cleanup

To stop and remove the Docker containers and networks created by Docker Compose:

```bash
docker compose down
```

To remove the Docker volumes (which store the PostgreSQL data and Prefect server metadata):

```bash
docker compose down --volumes
```

This completes the setup and demonstration of a local Prefect push worker pool. If you have any questions, feel free to ask!