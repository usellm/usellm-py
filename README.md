# useLLM - Use Large Language Models in Python App

## Usage

### Chat API

```python

from usellm import UseLLM, Options, Message


llm = UseLLM("https://usellm.org/api/llm")

def chat():
    res = llm.chat(
        Options(messages=[Message(role="user", content="Who are you?")])
    )
    print(res)

```

### Template API

```python

from usellm import UseLLM, Options, Message


llm = UseLLM("https://usellm.org/api/llm")

def template():
    res = llm.chat(
        Options(template="tutorial-generator",
                inputs={"topic": "Machine Learning"})
    )
    print(res)

```
