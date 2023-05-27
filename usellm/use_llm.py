from typing import List, Optional
import json
import requests


class Message:
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content

    def __repr__(self):
        return json.dumps(self.to_dict())

    def __str__(self):
        return json.dumps(self.to_dict())

    def to_dict(self):
        return {
            "role": self.role,
            "content": self.content,
        }

    def to_json(self):
        return json.dumps(self.to_dict())


class Options:
    def __init__(
        self,
        messages: Optional[List[Message]] = [],
        stream: Optional[bool] = None,
        template: Optional[str] = None,
        inputs: Optional[dict] = None,
    ):
        self.messages = messages
        self.stream = stream
        self.template = template
        self.inputs = inputs


class UseLLM:
    def __init__(self, service_url: str):
        self.service_url = service_url

    def chat(self, options: Options) -> None:
        if options.stream:
            raise Exception("Streaming is not supported")

        data = json.dumps(
            {
                "messages": [msg.to_dict() for msg in options.messages],
                "stream": options.stream,
                "$action": "chat",
                "template": options.template,
                "inputs": options.inputs,
            }
        )

        response = requests.post(
            self.service_url,
            headers={"Content-Type": "application/json"},
            data=data,
        )

        if response.status_code != 200:
            raise Exception(response.text)
        else:
            json_response = response.json()
            if "error" in json_response:
                raise Exception(json_response["error"]["message"])
            elif "choices" not in json_response:
                raise Exception(
                    "Unexpected response: {}".format(json_response))
            else:
                message = json_response["choices"][0]["message"]
                return Message(role=message["role"], content=message["content"])
