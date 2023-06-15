from typing import List, Optional
import json
import requests
import numpy as np


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


class GenerateImageResponse:
    def __init__(self, images):
        self.images = images

    def __repr__(self):
        return json.dumps(self.to_dict())

    def __str__(self):
        return json.dumps(self.to_dict())

    def to_dict(self):
        return {
            "images": self.images,
        }

    def to_json(self):
        return json.dumps(self.to_dict())

class EmbedResponse:
    def __init__(self, embeddings):
        self.embeddings = embeddings

    def __repr__(self):
        return json.dumps(self.to_dict())

    def __str__(self):
        return json.dumps(self.to_dict())

    def to_dict(self):
        return {
            "embeddings": self.embeddings,
        }

    def to_json(self):
        return json.dumps(self.to_dict())


class SpeakResponse:
    def __init__(self, audio_url):
        self.audio_url = audio_url

    def __repr__(self):
        return json.dumps(self.to_dict())

    def __str__(self):
        return json.dumps(self.to_dict())

    def to_dict(self):
        return {
            "audio_url": self.audio_url,
        }

    def to_json(self):
        return json.dumps(self.to_dict())

class TranscribeResponse:
    def __init__(self, text):
        self.text = text
        
    def __repr__(self):
        return json.dumps(self.to_dict())

    def __str__(self):
        return json.dumps(self.to_dict())

    def to_dict(self):
        return {
            "text": self.text,
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
        embed_input: Optional[str] = "",
        embed_user: Optional[str] = "",
        prompt: Optional[str] = None,
        n: Optional[int] = None,
        size: Optional[str] = None,
        text: Optional[str] = None,#added
        model_id: Optional[str]=None,
        voice_id: Optional[str]=None,
        audio_url: Optional[str]=None, #added
    ):
        self.messages = messages
        self.stream = stream
        self.template = template
        self.inputs = inputs
        self.prompt = prompt
        self.n = n
        self.size = size
        self.embed_input = embed_input
        self.embed_user = embed_user
        self.text = text
        self.audio_url = audio_url

class EmbeddingOptions:
    def __init__(
        self,
        embeddings:list[list[any]],
        query:list[float],
        top
    ):
        self.embeddings = embeddings
        self.query = query 
        self.top = top

class UseLLM:
    def __init__(self, service_url: str):
        self.service_url = service_url

    def chat(self, options: Options) -> Message:
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

    def generate_image(self, options: Options) -> GenerateImageResponse:

        if options.prompt is None:
            raise Exception('Prompt is required')

        no_of_images = options.n
        if no_of_images is None:
            no_of_images = 1

        image_size = options.size
        if image_size is None:
            image_size = '256x256'

        data = json.dumps(
            {
                "prompt": options.prompt,
                "$action": "generateImage",
                "n": no_of_images,
                "size": image_size
            }
        )

        response = requests.post(
            self.service_url,
            headers={"Content-Type": "application/json"},
            data=data,
            timeout=5000
        )

        if response.status_code != 200:
            raise Exception(response.text)
        else:
            json_response = response.json()
            res = GenerateImageResponse(images=json_response["images"])
            return res        

    def embed(self, options: Options) -> EmbedResponse:
        
        if options.embed_input is None:
            raise Exception("Input paragraph is required")

        data = json.dumps(
            {
                "input": options.embed_input,
                "user": options.embed_user,
                "$action": "embed"
            }
        )
        response = requests.post(
            self.service_url,
            headers={"Content-Type": "application/json"},
            data=data
        )
        if response.status_code != 200:
            raise Exception(response.text)
        else:
            json_response = response.json()
            res = EmbedResponse(embeddings=json_response["embeddings"])
            return res



    def speak(self, options: Options) -> SpeakResponse:
        if options.text is None:
            raise Exception('Input Text is required')
            
        #This function will return an audioURL which will be the audio version of the input text.
        
        data = json.dumps(
            {
                "text": options.text,
                "$action": 'speak'  
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
            res = SpeakResponse(audio_url = json_response['audioUrl'])
            return res
            


    def transcribe(self,options: Options) -> TranscribeResponse:

        if options.audio_url is None:
            raise Exception('Input Audio Url is Missing')
        
        data = json.dumps(
        {
            "audioUrl" : options.audio_url,
            "$action" : 'transcribe'
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
            res = TranscribeResponse(text = json_response['text'])
            return res

    def cosineSimilarity(self, vecA, vecB):
        dot_product = np.dot(vecA, vecB)
        magnitude = np.linalg.norm(vecA) * np.linalg.norm(vecB)
        return dot_product / magnitude
    
    
    def scoreEmbeddings(self, options:EmbeddingOptions) -> List[float]:
        scores = [self.cosineSimilarity(options.query, vector) for vector in options.embeddings]
        sorted_scores = sorted([(score, index) for index, score in enumerate(scores)], key=lambda x: x[0], reverse=True)
        
        
        if options.top is not None:
            sorted_scores = sorted_scores[:options.top]
    
        return sorted_scores
