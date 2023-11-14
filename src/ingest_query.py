from python_api.query.simple_query import query
from python_api.ingest.ingest_single import ingest

def main():
    task = input("\nTask?\n 1) Ingest\n 2) Query\n ")
    if task == "1":
      ingest()
    elif task == "2":
      query()

if __name__ == "__main__":
    main()
