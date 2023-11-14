
### Install requirements

Check the `requirements.txt` file and note that the requirements specify 2 specific packages:

```bash
pip3 install -r requirements.txt
```

### Set environment variables

The application uses several environment variables that you'll need to set. Put them in a `.env` file in the root directory of the project. Here's what your `.env` file should look like:

```sh
#Important-this needs to come from this file or won't work
OPENAI_KEY=

```
Launch a local version of the Milvus DB:
```sh
sudo docker-compose up -d
```
# Use Cases

## Query using Retrieval-Augmented-Generation(RAG) pattern
Ask questions to your documents
Find the relevant part
Summarize with LLM

This is a barebones app to show the following:
- The RAG pattern
- Usage of a vector database, particularly a production level one(in this case Milvus)
- Simple integration of Langchain

### Test dataset
This repo uses a [state of the union transcript](./source_documents/state_of_the_union.txt) as an example.

### Ask questions of the document
In order to run the app:

```shell
python src/main.py
```

```shell
choose 1 or 2(query or ingest)
```

Ingest will just load a document into the LLM and should be done first.

Query will allow asking questions of that document and should be done after.

And wait for the script to require your input.

```plaintext
> Enter a query:
```

Type `exit` to finish the script.

