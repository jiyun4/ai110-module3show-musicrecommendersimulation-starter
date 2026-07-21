# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
  The song use genre, mood, energy, valence, and tempo_bpm
- What information does your `UserProfile` store
 it stores the user's preferred genre, mood, energy, valence, and tempo
- How does your `Recommender` compute a score for each song
it uses score = 1 − |song_value − user_pref| / range to reward closeness to the user's preference; categorical features like genre and mood score 1 for a match and 0 for a miss
- How do you choose which songs to recommend
The recommender scores each song by comparing it against the user's taste profile across five features. Each feature produces a similarity score between 0 and 1, multiplied by its weight. A potential weight is that the system might over-prioritize genre, since it holds the largest weight

You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

================================================
  TOP RECOMMENDATIONS
================================================

1. Sunrise City  —  Neon Echo
   Score: 92.6 / 100
   Reasons:
     • genre match (+30)
     • mood match (+20)
     • energy similarity: 0.98 (+19.6)
     • valence similarity: 0.66 (+9.9)
     • tempo similarity: 0.87 (+13.1)

2. Gym Hero  —  Max Pulse
   Score: 69.9 / 100
   Reasons:
     • genre match (+30)
     • mood mismatch (+0)
     • energy similarity: 0.87 (+17.4)
     • valence similarity: 0.73 (+10.9)
     • tempo similarity: 0.77 (+11.6)

3. Rooftop Lights  —  Indigo Parade
   Score: 61.9 / 100
   Reasons:
     • genre mismatch (+0)
     • mood match (+20)
     • energy similarity: 0.96 (+19.2)
     • valence similarity: 0.69 (+10.3)
     • tempo similarity: 0.83 (+12.4)

4. Night Drive Loop  —  Neon Echo
   Score: 47.7 / 100
   Reasons:
     • genre mismatch (+0)
     • mood mismatch (+0)
     • energy similarity: 0.95 (+19.0)
     • valence similarity: 0.99 (+14.8)
     • tempo similarity: 0.93 (+13.9)

5. Concrete Kings  —  MC Vertex
   Score: 46.5 / 100
   Reasons:
     • genre mismatch (+0)
     • mood mismatch (+0)
     • energy similarity: 1.00 (+20.0)
     • valence similarity: 0.80 (+12.0)
     • tempo similarity: 0.96 (+14.5)

================================================

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran.

- **What happened when you changed the weight on genre from 2.0 to 0.5:** When I lowered genre from 30 points to about 7, the top pick (Sunrise City) dropped from 92.6 to 69.6 and songs from other genres like Night Drive Loop rose into the top 3. This showed that a high genre weight is what locks users into one genre.

- **What happened when you added tempo or valence to the score:** Adding tempo and valence lifted well-rounded matches — Sunrise City went from 69.6 to 92.6 and gaps between songs widened. But it also handed out easy points to songs the user never described, since missing preferences default to the middle.

- **How did your system behave for different types of users:** For clear, consistent users (lofi/chill, metal/aggressive, classical/melancholic) it worked well, giving the "right" genre a 90+ score every time. The weakness is that the winner is almost always a same-genre song, so every user type ends up in its own narrow bubble.

---

## Limitations and Risks

Genre and mood are worth half the score and must match exactly, so the system keeps showing songs from the user's chosen genre and rarely suggests anything new, a filter bubble that limits discovery. Missing preferences quietly fill in with default values, so users get "free" points they never asked for. The catalog only has 20 songs, so any genre or mood that is missing or rare can never be recommended well. And because labels must match exactly, a user who types "Pop" instead of "pop" is unfairly penalized without any warning.

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



