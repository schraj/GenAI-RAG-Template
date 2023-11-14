import openai
from python_api.shared.app_base import initialize_openai


initialize_openai()

response = openai.ChatCompletion.create(
    engine="gpt-35-turbo",
    messages=[
      {"role": "system", "content": "You are an AI assistant that helps people find information."},
      {"role": "user", "content": "what is the point of ai?"},
    ]
)
print(response)