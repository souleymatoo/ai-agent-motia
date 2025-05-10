from pydantic import BaseModel
import anthropic
from dotenv import load_dotenv
import os

load_dotenv()

# Define a Pydantic model for input validation
class InputModel(BaseModel):
    message: str
 
config = {
    "type": "event",
    "name": "Sentiment Analysis",
    "subscribes": ["product-review"], 
    "emits": ["positive-review", "negative-review"],
    "input": InputModel.model_json_schema(), # We use jsonschema to validate
    "flows": ["default"]
}

def get_sentiment_analysis(client, review):
    response = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=100,
        temperature=1,
        system="You are a helpful assistant that analyzes customer reviews and determines if they are positive or negative. Respond with only the word 'positive' or 'negative'.",
        messages=[
            {
                "role": "user", 
                "content": [
                    {
                        "type": "text",
                        "text": review
                    }
                ]
            }
        ]
    )
    return response.content[0].text.strip().lower()

def get_reframed_review(client, review):
    response = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=200,
        temperature=0.7,
        system="You are a helpful assistant that reframes negative customer reviews into constructive feedback. Focus on identifying the core issue and suggesting improvements while maintaining a positive tone. Keep the response concise and actionable.",
        messages=[
            {
                "role": "user", 
                "content": [
                    {
                        "type": "text",
                        "text": f"Please reframe this negative review into constructive feedback: {review}"
                    }
                ]
            }
        ]
    )
    return response.content[0].text.strip()
 
async def handler(input, context):
    review = input.review
    context.logger.info(f'Processing input: {review}')

    client = anthropic.Anthropic()
    sentiment = get_sentiment_analysis(client, review)
    context.logger.info(f"Sentiment: {sentiment}")

    topic = "positive-review" if sentiment == "positive" else "negative-review"
    context.logger.info(f"topic: {topic}")
    review_message = review if sentiment == "positive" else get_reframed_review(client, review)

    # Emit the sentiment analysis result
    await context.emit({
        "topic": topic,
        "data": {
            "review": review_message,
            "sentiment": sentiment
        }
    })