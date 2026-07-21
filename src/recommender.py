import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Read songs.csv and return a list of song dicts with numeric fields cast to numbers."""
    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against user prefs (0-100) and return the score with per-feature reasons."""
    reasons: List[str] = []
    total = 0.0

    # Genre match: +30 (categorical — full points if equal, else 0)
    if song["genre"] == user_prefs.get("genre"):
        total += 30
        reasons.append("genre match (+30)")
    else:
        reasons.append("genre mismatch (+0)")

    # Mood match: +20 (categorical)
    if song["mood"] == user_prefs.get("mood"):
        total += 20
        reasons.append("mood match (+20)")
    else:
        reasons.append("mood mismatch (+0)")

    # Energy similarity: up to 20 points, 1 - |diff| / 1.0, clamped at 0
    energy_sim = max(0.0, 1 - abs(song["energy"] - user_prefs.get("energy", 0.5)) / 1.0)
    energy_pts = round(energy_sim * 20, 1)
    total += energy_pts
    reasons.append(f"energy similarity: {energy_sim:.2f} (+{energy_pts})")

    # Valence similarity: up to 15 points, 1 - |diff| / 1.0, clamped at 0
    valence_sim = max(0.0, 1 - abs(song["valence"] - user_prefs.get("valence", 0.5)) / 1.0)
    valence_pts = round(valence_sim * 15, 1)
    total += valence_pts
    reasons.append(f"valence similarity: {valence_sim:.2f} (+{valence_pts})")

    # Tempo similarity: up to 15 points, 1 - |diff| / 140, clamped at 0
    tempo_sim = max(0.0, 1 - abs(song["tempo_bpm"] - user_prefs.get("tempo_bpm", 100)) / 140)
    tempo_pts = round(tempo_sim * 15, 1)
    total += tempo_pts
    reasons.append(f"tempo similarity: {tempo_sim:.2f} (+{tempo_pts})")

    return (round(total, 1), reasons)

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score every song and return the top k as (song, score, explanation), highest first."""
    # Score every song in the catalog, building (song, score, explanation) tuples.
    scored = [
        (song, *_to_score_and_explanation(user_prefs, song))
        for song in songs
    ]
    # Rank highest score first, then keep the top k.
    scored.sort(key=lambda item: item[1], reverse=True)
    return scored[:k]


def _to_score_and_explanation(user_prefs: Dict, song: Dict) -> Tuple[float, str]:
    """Run score_song and flatten its reasons list into one explanation string."""
    score, reasons = score_song(user_prefs, song)
    return score, "; ".join(reasons)
