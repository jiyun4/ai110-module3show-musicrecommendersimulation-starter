# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**tastefinder v.01**

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

- **What kind of recommendations does it generate:** It ranks a fixed catalog of 20 songs against a user's taste profile and returns the top matches, each with a 0–100 score and a per-feature reason breakdown.

- **What assumptions does it make about the user:** It assumes the profile is complete, cleanly formatted (numbers in `[0,1]`, labels spelled/cased exactly like the catalog), and internally consistent — testing showed it silently fills in defaults, clamps out-of-range values, and resolves contradictory tastes (e.g. sad + high energy) toward whatever scores highest.

- **Is this for real users or classroom exploration:** Strictly classroom exploration — the tiny catalog and lack of input validation make it a teaching tool, not a system for real listeners.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

- **What features of each song are used:** Each song is described by its genre, its mood, how energetic it is, how happy or positive it sounds (valence), and how fast it is (tempo).

- **What user preferences are considered:** The user tells the app their favorite genre and mood, plus how much energy, positivity, and speed they like in music.

- **How does the model turn those into a score:** The app compares the user's taste to each song and gives out points — a full match on genre or mood earns big points, while energy, positivity, and tempo earn points based on how close the song is to what the user wanted. It adds these up to a score out of 100 and recommends the highest-scoring songs.

- **What changes did you make from the starter logic:** I built out the scoring so it uses all five features instead of just genre, and I added a plain-language reason for every song so the user can see why it was picked.

---

## 4. Data  

Describe the dataset the model uses.  

- **How many songs are in the catalog:** There are 20 songs, each stored with its genre, mood, energy, tempo, positivity, danceability, and acousticness.

- **What genres or moods are represented:** It covers a wide spread of genres (pop, lofi, rock, jazz, hip hop, classical, edm, country, r&b, metal, folk, reggae, funk, blues, and more) and just as many moods (happy, chill, intense, sad, romantic, aggressive, peaceful, and others).

- **Did you add or remove data:** No — I used the starter catalog as it came.

- **Are there parts of musical taste missing:** Yes. Because there are only 20 songs, most genres have just one example, so there is very little variety within any single style, and things like language, lyrics, era, and culture are not captured at all.

---

## 5. Strengths  

Where does your system seem to work well  

- **User types for which it gives reasonable results:** It works best for listeners with a clear, consistent taste — a lofi/chill fan, a metal/aggressive fan, or a happy pop fan all get songs that obviously fit, usually scoring 90 or higher.

- **Patterns the scoring captures correctly:** It reliably matches energy and mood — calm profiles get soft, quiet songs and upbeat profiles get loud, fast ones, which is exactly what those preferences should do.

- **Cases where the recommendations matched my intuition:** When I asked for a sad, low-positivity profile it returned slow, gloomy blues and classical tracks, and when I asked for a happy one it returned bright pop — both matched what I would have picked myself.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

- **Features it does not consider:** It ignores lyrics, language, artist, era, and popularity, so it only "hears" a song as a set of numbers, not as actual music.

- **Genres or moods that are underrepresented:** Almost every genre has only one song, so if a user's favorite style barely appears in the catalog, they can never get a good match.

- **Cases where the system overfits to one preference:** Genre and mood are worth half the total score and are all-or-nothing, so the app leans heavily on them — a song in the "right" genre can win even if its energy and tempo are a poor fit.

- **Ways the scoring might unintentionally favor some users:** Users whose taste matches the common, well-represented genres do great, while users with rare tastes or who spell a label differently (like "Pop" instead of "pop") get worse results through no fault of their own.

---

## 7. Evaluation  

To check whether the recommender worked, I set up pairs of very different listeners and
looked at the songs each one got. For every pair I asked a simple question: do the songs
match the kind of person I described?

**Pair 1 — A high-energy dance fan vs. a calm study listener**
The dance fan got a loud, upbeat electronic song, while the calm listener got soft, quiet
tracks that are good for studying. This makes sense: when I asked for lower energy, the app
moved away from loud songs and picked gentle ones instead.

**Pair 2 — A happy listener vs. a sad listener**
The happy listener got a bright, cheerful song, and the sad listener got slow, gloomy ones.
The app clearly picked up on the mood I asked for and matched the feeling of the music to it.

**Pair 3 — The same listener, but I only changed the mood**
I kept everything the same and only switched the mood from "happy" to "intense." The top song
changed from a cheerful pop track to a high-energy workout song, but both stayed in the pop
genre. This shows the mood really does change the results, while the genre keeps the list
focused on the music the person likes.

**What surprised me:** even a small change, like switching one mood word, was enough to
reorder the top songs. That told me the app leans heavily on genre and mood, maybe more than
it should.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

- **Additional features or preferences:** I would add things like era, language, and artist so the app understands more about a song than just its sound numbers.

- **Better ways to explain recommendations:** Instead of showing points, I could write friendlier reasons like "chosen because it's calm and acoustic, just like you asked."

- **Improving diversity among the top results:** I would stop the list from being all one genre by mixing in a few close but different styles, so the user discovers new music.

- **Handling more complex user tastes:** I would let genre and mood be partial matches (so "pop" and "indie pop" count as similar) and catch contradictory or messy input instead of silently guessing.

---

## 9. Personal Reflection  

A few sentences about your experience.  

- **What I learned about recommender systems:** I learned that a recommender is really just a scoring rule, and that the choices behind that rule — like how many points each feature is worth — quietly decide what people end up seeing.

- **Something unexpected I discovered:** I was surprised how easily the system could be thrown off, whether by a small mood change reshuffling the whole list or by a capital letter causing it to miss an obvious match.

- **How this changed the way I think about music apps:** It made me realize the apps I use every day are making the same kinds of trade-offs, and that they can trap people in a "bubble" of familiar music just because of how their scoring is set up.
