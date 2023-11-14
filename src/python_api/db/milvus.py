from pymilvus import Collection, connections, MilvusException
from typing import Any, Iterable, List, AnyStr

def connect():
    connections.connect("default", host="localhost", port="19530")

def disconnect():
    connections.disconnect("default")

def delete_by_document_name(document_name)->bool:
  connect()
  collection = Collection("LangChainCollection")
  chunks = find_chunks_by_document(document_name)
  chunkIds = list(map(lambda item: str(item["pk"]), chunks))
  idsString = ",".join(chunkIds)
  collection.delete("pk in [" + idsString + "]")
  disconnect()

def find_chunks_by_document(document_name)->list[AnyStr]:
  collection = Collection("LangChainCollection")
  collection.load()
  res = collection.query(
    expr = "source in ['" + document_name + "']",
    offset = 0,
    limit = 16380, 
    output_fields = ["pk"],
  )
  return res

# taken from the Langchain milvus module
def insert(
    texts: Iterable[dict],
    batch_size: int = 50,
    **kwargs: Any,
) -> List[str]:
    texts = list(texts)
    total_count = len(texts)
    pks: list[str] = []
    for i in range(0, total_count, batch_size):
        end = min(i + batch_size, total_count)
        insert_list = texts[i:end]
        try:
            connect()
            collection = Collection("LangChainCollection")
            res: Collection
            res = collection.insert(insert_list, **kwargs)
            pks.extend(res.primary_keys)
            print(collection.schema)
            disconnect()
        except MilvusException as e:
            raise e
    return pks
