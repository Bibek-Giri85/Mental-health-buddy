import streamlit as st
from core.crew_setup import run_crew

st.set_page_config(page_title="Mental Health Support Bot", layout="centered")
st.title("🧠 Mental Health Support Bot")
st.write("Get quick emotional support, empathy, and self-care tips.")

user_input = st.text_input("How are you feeling today?")

# Mood-specific jokes/notes
mood_responses = {
    "sad": {
        "emoji": "😢",
        "note": "You're allowed to feel blue, but also remember… even clouds take breaks and become cotton candy at sunset."
    },
    "anxious": {
        "emoji": "😰",
        "note": "Anxiety’s like a browser with 50 tabs open — take a breath, close a few mentally, and refresh 🍃"
    },
    "angry": {
        "emoji": "😡",
        "note": "Totally okay to feel this way. But maybe try yelling into a pillow like a karaoke mic 🎤 (it won’t judge)."
    },
    "lonely": {
        "emoji": "🥺",
        "note": "Feeling alone? You're not. Even Wi-Fi signals reach out — and so am I 💖"
    },
    "default": {
        "emoji": "💖",
        "note": "Whatever you're feeling is valid. Here's a digital marshmallow for your soul ☁️"
    }
}

def detect_mood(text):
    
    text = text.lower()
    if "sad" in text or "low" in text:
        return "sad"
    elif "anxious" in text or "nervous" in text or "worried" in text:
        return "anxious"
    elif "angry" in text or "frustrated" in text:
        return "angry"
    elif "lonely" in text or "alone" in text:
        return "lonely"
    return "default"

if st.button("Get Support"):
    if user_input:
        with st.spinner("Analyzing..."):
            result = run_crew(user_input)

            outputs = []
            if hasattr(result, "tasks_output"):
                for task_output in result.tasks_output:
                    raw_text = getattr(task_output, "raw", "").strip()
                    if raw_text:
                        outputs.append(raw_text)

            if outputs:
                mood = detect_mood(user_input)
                mood_data = mood_responses.get(mood, mood_responses["default"])

                st.success("Here's your support:")
                st.write(f"- {mood_data['emoji']} Mood Insight: {outputs[0]}")  # Mood Analyzer
                st.write(f"- ❤️ Support: {outputs[1]}")  # Companion
                st.write(f"- 🌱 Self-Care Tip: {outputs[2]}")  # Self-care
                st.write(f"- 🌈 Bonus Thought: {mood_data['note']}")
            else:
                st.warning("Couldn't generate support. Please try again.")
    else:
        st.warning("Please enter something about how you're feeling.")
