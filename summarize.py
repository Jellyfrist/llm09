from litellm import completion
from config import PROVIDER_MODEL as MODEL

def summarize(text, length="brief"):
    lengths = {"brief":"in 1–2 sentences","medium":"in 3–4 sentences","detailed":"in 5–6 sentences with key points"}
    r = completion(
        model=MODEL,
        messages=[
            {"role":"system","content":f"You are an expert summarizer. Summarize {lengths.get(length,'in 2–3 sentences')}"},
            {"role":"user","content":text}
        ],
        temperature=0.1, max_tokens=70,
    )
    return r.choices[0].message["content"].strip()

if __name__ == "__main__":
    sample = """
    What is a Chicken?
Domesticated Bird:
Chickens are medium-sized, domesticated birds primarily raised for their meat and eggs. 
Ancestry:
They are descended from wild jungle fowl, with the red junglefowl (Gallus gallus) being the primary ancestor, possibly with contributions from gray junglefowl. 
Anatomy:
Chickens have short wings, making them poor fliers, and a round body with a short beak. Male chickens are roosters, and females are hens, both of which can have combs and wattles. 
Global Importance:
Chickens are the most common domestic animal and a crucial component of global agriculture, with billions raised annually for consumption. 
Interesting Facts
Social Animals:
Chickens are intelligent and social animals, possessing complex vocalizations and behaviors. 
Egg Production:
Hens can lay many eggs a year, some of which are fertile if a rooster is involved. 
Cultural Significance:
Beyond their economic importance, chickens feature prominently in folklore, religion, and literature across many cultures. 
    """
    print(summarize(sample, "brief"))