from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = Groq(api_key=os.getenv("GROK_API_KEY"))

SYSTEM_PROMPT = '''
You are a children's picture book writer.
Return ONLY valid JSON:
{
  "title": "",
  "pages": [
    {
      "page_number": 1,
      "text": "",
      "image_prompt": ""
    }
  ]
}
'''

def generate_story(user_prompt):
    response = client.chat.completions.create(
        model="grok-1",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7
    )

    content = response.choices[0].message.content
    return json.loads(content)
