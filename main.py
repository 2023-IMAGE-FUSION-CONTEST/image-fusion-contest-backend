from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import requests
import json

origins = [
	"http://127.0.0.1:3000",
	"http://127.0.0.1:3001",
	"https://contest.presso.codes"
]

app = FastAPI()

app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"]
)


class Item(BaseModel):
	fn_index: int
	data: list


@app.post("/api/image-fusion")
def post_image_fusion(item: Item):
	url = "https://demo.70e9f1a0f18a49a29a0cd16c9e0750df.lambdaspaces.com/run/predict"
	headers = {
		"Content-Type": "application/json"
	}
	data = {
		"fn_index": item.fn_index,
		"data": item.data
	}

	response = requests.post(url, headers=headers, json=data)
	return json.loads(response.text)
