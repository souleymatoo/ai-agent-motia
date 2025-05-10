from pydantic import BaseModel

class InputModel(BaseModel):
    review: str
    sentiment: str

config = {
    "type": "event",
    "name": "Positive Review Handler",
    "description": "Handles positive product reviews",
    "subscribes": ["positive-review"],
    "emits": [],
    "input": InputModel.model_json_schema(),
    "flows": ["default"]
}

async def handler(input, context):
    review = input.review
    sentiment = input.sentiment
    context.logger.info(f'Processing positive review: {review} with sentiment: {sentiment}')
    
    # Here you can add any specific logic for handling positive reviews
    # For example: storing in a database, sending notifications, etc. 