from litellm import completion
from config import PROVIDER_MODEL as MODEL

def rewrite(text, style):
    styles = {
        "formal":"formal, business‑appropriate",
        "casual":"friendly, conversational",
        "technical":"precise technical writing",
        "marketing":"persuasive, benefits‑led"
    }
    r = completion(
        model=MODEL,
        messages=[
            {"role":"system","content":f"Rewrite in {styles.get(style,'clear and concise')} style while preserving meaning."},
            {"role":"user","content":text}
        ],
        temperature=0.4, max_tokens=200,
    )
    return r.choices[0].message["content"].strip()

if __name__ == "__main__":
    print(rewrite("Most scientists agree that the Southeast Asian Red Junglefowl (gallus gallus) is the primary wild ancestor of chickens. However, because DNA studies show that the Red Junglefowl lacks the gene for yellow skin (and shanks) it is believed that some point, hybridization with the Grey Junglefowl (Gallus sonnaratii) of India has occurred. The body structure of the Indian Gamebird (Cornish) and the Brahmas of China gives physical evidence of Grey Jungle- fowl influence. The tail carriage of the breed Sumatra indicates genetic contributions of the SriLanka Junglefowl (Gallus lafayetti). No doubt the Green Junglefowl (Gallus varius) has also contributed to modern chickens.", "marketing"))