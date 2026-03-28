# 🌍 English → Nigerian Language Translator

A bilingual dictionary web app that translates English words into five Nigerian/African languages: **Yoruba, Igbo, Hausa, Idoma, and Mwaghavul**.

---

## 📋 Description

This project was built as a collaborative group assignment where each member contributed a dictionary of 20 English words translated into their assigned language. The app allows users to look up English words and instantly see their translation in the selected language.

---

## 🚀 How to Run (Streamlit Version)

Make sure you have Python and Streamlit installed, then run:

```bash
pip install streamlit
streamlit run translator.py
```

The app will open in your browser at `localhost created from your code editor`.

---

## 🎮 How to Use

1. **Select a language** from the dropdown menu (Yoruba, Igbo, Hausa, Idoma, or Mwaghavul).
2. **Type an English word** in the text input field.
3. Click the **Translate** button to see the result.
4. If the word exists in the dictionary, the translation is displayed.
5. If not found, an error message is shown.

> **Note:** Translations are **not case-sensitive** — `Water`, `water`, and `WATER` all work.

---

## 🗣️ Languages Included

| Language | Region | Words |
|----------|--------|-------|
| Yoruba | Southwest Nigeria | 20 |
| Igbo | Southeast Nigeria | 20 |
| Hausa | Northern Nigeria | 19 |
| Idoma | Benue State, Nigeria | 20 |
| Mwaghavul | Plateau State, Nigeria | 20 |

---

## 📖 Sample Word List

| English | Yoruba | Igbo | Hausa | Idoma | Mwaghavul |
|---------|--------|------|-------|-------|-----------|
| water | omi | mmiri | ruwa | ami | — |
| food | ounje | nri | abinci | inyam | biise |
| friend | ore | enyi | — | ogele | shaarr |
| love | ife | ifuru | — | iyolo | — |
| money | — | — | kudi | owo | shagal |
| God | — | — | — | Owoicho | naan |

---

## 👥 Group Contributions

Each group member was responsible for one language dictionary of 20 words:

| Member | Language |
|--------|----------|
| Member 1 | Yoruba |
| Member 2 | Igbo |
| Member 3 | Hausa |
| Member 4 | Idoma |
| Member 5 | Mwaghavul |


---

## 🛠️ Requirements

- Python 3.x
- Streamlit

```bash
pip install streamlit
```

---

## 📁 File Structure

```
translator.py      # Main Streamlit app
README.md          # Project documentation
```




- Include audio playback for each word
- Add more Nigerian languages (Efik, Tiv, Ijaw, etc.)
- Allow users to suggest or add new words
