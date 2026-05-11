from prefect import flow, task

@task
def say_hello(name: str):
    print(f"Hello, {name}!")

@flow(name="my-first-flow")
def my_simple_flow(name: str = "World"):
    say_hello(name)

if __name__ == "__main__":
    # This is for local execution and deployment registration
    # The work_pool_name must match the name defined in docker-compose.yml
    # The path in the storage block should match the volume mount in docker-compose.yml
    my_simple_flow.deploy(
        name="my-first-deployment",
        work_pool_name="local-push-pool",
        image="prefecthq/prefect:2-latest", # This is a placeholder, actual image is not used for local-file-system
        # Using a local-file-system storage block for simplicity in local testing
        # The path /opt/prefect/flows is where the flow code is mounted inside the worker container
        # The flow_entrypoint should be relative to this path
        storage=({
            "block_type_slug": "local-file-system",
            "_block_document_name": "local-storage",
            "path": "/opt/prefect/flows",
            "_encode_json": False
        }),
        flow_entrypoint="flow.py:my_simple_flow",
        # You can add a schedule here if needed, e.g., schedule=IntervalSchedule(interval=timedelta(minutes=5))
    )
