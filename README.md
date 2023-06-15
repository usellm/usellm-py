# useLLM - Use Large Language Models in Python App

The `usellm` Python library enables interaction with a chat-based Large Language Model (LLM) service. This interaction can be used to perform various language-related tasks, like generating chat conversation using the OpenAI API. It's designed as a Python port of the [`usellm`](https://usellm.org) JavaScript library.

## Installation

The library can be installed with `pip`:

```
pip install usellm
```

## Example Usage

Here is a basic usage example:

```python
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
```

## Image Example Usage

```
from usellm import Options, UseLLM

# Initialize the service
service = UseLLM(service_url="https://usellm.org/api/llm")


# Interact with the service
options = Options(prompt="Generate a beautiful landscape", n=3, size="512x512")

response = service.generate_image(options)

# Print the image URLs
for image in response.images:
    print(image)
```

The above code will generate a response using the OpenAI ChatGPT API. The service URL "https://usellm.org/api/llm" should be used only for testing.

## Classes and Methods

### 1. `UseLLM` class

The `UseLLM` class provides the interface for interacting with the LLM service.

Methods:

- `__init__(self, service_url: str)`: Initializes a new instance of the `UseLLM` class.
- `chat(self, options: Options) -> Message`: Interacts with the LLM using the provided `Options`, and returns a `Message` instance that represents the LLM's response.

### 2. `Options` class

The `Options` class represents a set of configuration options for a chat interaction with the LLM.

- `messages`: A list of `Message` instances representing the conversation up to the current point.
- `stream`: A boolean indicating if the interaction is a streaming interaction. Note: streaming is currently not supported.
- `template`: A string representing a message template to guide the conversation.
- `inputs`: A dictionary of additional inputs for the conversation.
- `prompt`: A string representing the prompt for generating images.
- `n`: An integer representing the number of images to generate (default: 1).
- `size`: A string representing the size of the generated images (default: '256x256').

Methods:

- `__init__(self, messages: Optional[List[Message]] = [], stream: Optional[bool] = None, template: Optional[str] = None, inputs: Optional[dict] = None)`: Initializes a new instance of the `Options` class.

### 3. `Message` class

The `Message` class represents a message in a conversation. It consists of two main attributes:

- `role`: The role of the message sender. Common values could be `system`, `user`, `assistant`.
- `content`: The content of the message.

Methods:

- `__init__(self, role: str, content: str)`: Initializes a new instance of the `Message` class.
- `__repr__(self) -> str`: Returns a string representation of the `Message` instance.
- `__str__(self) -> str`: Returns a string representation of the `Message` instance.
- `to_dict(self) -> dict`: Returns a dictionary representation of the `Message` instance.
- `to_json(self) -> str`: Returns a JSON string representation of the `Message` instance.

## Exceptions

The library raises an `Exception` in the following situations:

- If the `stream` option is set to `True`, because streaming is not currently supported.
- If the HTTP response status code from the LLM service is not 200.
- If the HTTP response from the LLM service contains an "error" field.
- If the HTTP response from the LLM service does not contain a "choices" field.

Please create an issue to report bugs or suggest improvements. Learn more about the original JavaScript library here: https://usellm.org
