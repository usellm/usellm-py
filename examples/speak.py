
from usellm import Options, UseLLM

# Initialize the service
service = UseLLM(service_url="https://usellm.org/api/llm")


options = Options(text = "Hi, I am Himani!")

# Interact with the service
response = service.speak(options)

# Print the assistant's response
print(response)
