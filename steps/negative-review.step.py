from pydantic import BaseModel

class InputModel(BaseModel):
    review: str
    sentiment: str

config = {
    "type": "event",
    "name": "Negative Review Handler",
    "description": "Handles negative product reviews",
    "subscribes": ["negative-review"],
    "emits": [],
    "input": InputModel.model_json_schema(),
    "flows": ["default"]
}

async def handler(input, context):
    review = input.review
    sentiment = input.sentiment
    context.logger.info(f'Processing negative review: {review} with sentiment: {sentiment}')
    
    # Here you can add any specific logic for handling negative reviews
    # For example: storing in a database, sending notifications to support team, etc. 