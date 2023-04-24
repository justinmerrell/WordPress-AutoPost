import os
import random
import requests
import openai
from dotenv import load_dotenv

load_dotenv()

# API Keys
NEWSAPI_KEY = os.environ.get("NEWSAPI_KEY")
openai.api_key = os.environ.get("OPENAI_API_KEY")


def get_real_headlines(api_key=NEWSAPI_KEY):
    """Fetches the latest headlines related to AI, tech, entrepreneurship, and self-help."""
    url = "https://newsapi.org/v2/everything"

    topics_of_interest = [
        "artificial intelligence OR machine learning OR deep learning",
        "technology trends OR tech innovations OR emerging technologies",
        "entrepreneurship OR startups OR business growth OR venture capital",
        "self-help OR personal development OR productivity OR time management"
    ]

    params = {
        "q": topics_of_interest[random.randint(0, len(topics_of_interest) - 1)],
        "apiKey": api_key,
        "pageSize": 5,
        "page": 1,
        "sortBy": "publishedAt",
        "language": "en",
    }

    response = requests.get(url, params=params, timeout=10)

    if response.status_code == 200:
        data = response.json()
        if data["totalResults"] > 0:
            headlines = [article["title"] for article in data["articles"]]
            return headlines
        else:
            return ["No articles found related to AI or the latest tech trend."]
    else:
        raise Exception(f"Error: Unable to fetch articles. Status code: {response.status_code}")


def paraphrase_headline(headlines):
    """
    Generates a new blog post title based on the provided headlines.
    """
    with open("prompts/headline.txt", "r", encoding="UTF-8") as headline_prompt_file:
        prompt = headline_prompt_file.read()

    prompt = prompt.replace("{{HEADLINES}}", str(headlines))

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content.strip(), prompt


def blog_post_title():
    """Generates a new blog post title based on the latest news headlines."""
    return paraphrase_headline(get_real_headlines())


if __name__ == "__main__":
    original_headlines = get_real_headlines()
    new_headline, _ = paraphrase_headline(original_headlines)

    print(f"Original Headlines: {original_headlines}")
    print(f"New Headline: {new_headline}")
