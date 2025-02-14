# README

## Overview

The `PerplexityAPI` class is a Python wrapper for interacting with the Perplexity AI API. It allows users to send chat completion requests to the API and retrieve responses. This class handles the creation of payloads, sending requests, and parsing responses.

## Installation

To use the `PerplexityAPI` class, you need to have the `requests` library installed. You can install it using pip:

```
pip install requests
```

## Usage

### Initialization

To initialize the `PerplexityAPI` class, you need to provide your API key:

```python
from perplexity_api import PerplexityAPI

api_key = "your_api_key_here"
api = PerplexityAPI(api_key)
```

### Sending a Request

To send a request to the Perplexity AI API, use the `send_request` method. You need to specify the model and messages, and you can also provide additional keyword arguments:

```python
model = "your_model_name"
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Tell me a joke."}
]

response = api.send_request(model, messages)
```

### Retrieving the Response

To retrieve the response content from the API, use the `get_response` method. You can pass the JSON data returned by the `send_request` method, or it will use the last response stored in the instance:

```python
content = api.get_response(response)
print(content)
```

## Methods

### `__init__(self, api_key)`

Initializes the `PerplexityAPI` instance with the provided API key.

- `api_key`: Your API key for the Perplexity AI API.

### `create_payload(self, model, messages, **kwargs)`

Creates the payload for the API request.

- `model`: The model name to use for the request.
- `messages`: A list of message dictionaries.
- `**kwargs`: Additional keyword arguments to include in the payload.

### `send_request(self, model, messages, **kwargs)`

Sends a request to the Perplexity AI API and returns the JSON response.

- `model`: The model name to use for the request.
- `messages`: A list of message dictionaries.
- `**kwargs`: Additional keyword arguments to include in the payload.

### `get_response(self, json_data=None)`

Retrieves the response content from the JSON data. If no JSON data is provided, it uses the last response stored in the instance.

- `json_data`: The JSON data returned by the `send_request` method (optional).

## Example

```python
from perplexity_api import PerplexityAPI

api_key = "your_api_key_here"
api = PerplexityAPI(api_key)

model = "your_model_name"
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Tell me a joke."}
]

response = api.send_request(model, messages)
content = api.get_response(response)
print(content)
```

This example demonstrates how to initialize the `PerplexityAPI` class, send a request to the Perplexity AI API, and retrieve the response content.