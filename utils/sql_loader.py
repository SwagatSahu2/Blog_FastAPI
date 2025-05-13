import yaml

def load_queries(file_path: str = "sql/queries.yaml"):  
    with open(file_path, "r") as file:
        return yaml.safe_load(file)["queries"]