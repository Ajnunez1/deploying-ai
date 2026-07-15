import kagglehub
import pandas as pd
from pathlib import Path

# Download dataset
path = kagglehub.dataset_download("tmdb/tmdb-movie-metadata")

# Load movie dataset
movies_path = Path(path) / "tmdb_5000_movies.csv"
movies = pd.read_csv(movies_path)

# Create a sample
movies_small = (
    movies[["title", "overview", "genres", "release_date"]]
    .dropna(subset=["title", "overview"])
    .sample(n=500, random_state=42) #42 for reproducibility
)

# Save inside the folder
output_path = Path(__file__).parent / "data" / "movies.csv"
output_path.parent.mkdir(parents=True, exist_ok=True)

movies_small.to_csv(output_path, index=False)

print(f"Saved {len(movies_small)} movies to: {output_path}")
print(f"File size: {output_path.stat().st_size / 1_000_000:.2f} MB")