import chromadb
import pandas as pd
from pathlib import Path

base_path = Path(__file__).parent
movies_path = base_path / "data" / "movies.csv"
chroma_path = base_path / "chroma_db"

movies = pd.read_csv(movies_path)

client = chromadb.PersistentClient(path=str(chroma_path))

collection = client.get_or_create_collection(
    name="movies"
)

documents = movies["overview"].tolist()
ids = [str(i) for i in range(len(movies))]
metadata = [
    {
        "title": row["title"],
        "release_date": str(row["release_date"])
    }
    for _, row in movies.iterrows()
]

collection.add(
    ids=ids,
    documents=documents,
    metadatas=metadata
)

print(f"Saved {collection.count()} movies in ChromaDB.")