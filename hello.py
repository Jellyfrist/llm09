from litellm import completion
from config import PROVIDER_MODEL as MODEL

resp = completion(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are chicken."},
        {"role": "user", "content": "Say hello in 7 words."}
    ],
    max_tokens=32,
)
print("REPLY:", resp.choices[0].message["content"]) 
print("USAGE:", getattr(resp, "usage", {}))