import openai
import os

# openai.api_key = os.environ.get('OPENAI_TOKEN')

def send_to_openai(image_path):
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "rate the task from 0 to 2, where 2 is the solution is completely correct. "
                                             "Write comments to the solution"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_path,
                        },
                    },
                ],
            }
        ],
        max_tokens=300,
    )

    return response.choices[0].message.content
