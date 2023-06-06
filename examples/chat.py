from usellm import Message, Options, UseLLM

# Initialize the service
service = UseLLM(service_url="https://usellm.org/api/llm")

# Prepare the conversation
messages = [
  Message(role="system", content="You are a helpful assistant."),
  Message(role="user", content="What can you do for me?"),
]
options = Options(messages=messages)

# Interact with the service
response = service.chat(options)

# Print the assistant's response
print(response.content)
