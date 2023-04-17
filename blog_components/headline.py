import os
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

    params = {
        "q": "artificial intelligence OR technology OR entrepreneurship OR self-help",
        "apiKey": api_key,
        "pageSize": 5,
        "page": 1,
        "sortBy": "publishedAt",
        "language": "en",
    }

    response = requests.get(url, params=params)

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
    """Generates a new blog post title based on the provided headlines."""
    prompt = f"""
        You are a ghostwriter for a blog that focuses on the latest tech trends, specifically AI, as well as self-help and entrepreneurship topics.

        Using the following headlines as inspiration for a blog post, combine them into a new single blog post title.
        Headlines: `{headlines}`

        The new title must be coherent and make sense.
        Do not include an individual's name or a specific location in the headline.
        Do not write about about family, politics, parenting, or religion.Controversial topics are fine, but do not write about anything that could be considered offensive.
        The title should leave the reader wanting to read the blog post.

        The tile should follow the format: `single word | short catchy phrase`
        Examples: `Dedication | Being an Entrepreneur`, `Consistency | Easier Said Than Done`, `Books | Lifes Shortcut`, `Meditation | The Key to Happiness`, 'Stress | The Silent Killer'
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content.strip()


def blog_post_title():
    """Generates a new blog post title based on the latest news headlines."""
    return paraphrase_headline(get_real_headlines())


if __name__ == "__main__":
    original_headlines = get_real_headlines()
    new_headline = paraphrase_headline(original_headlines)

    print(f"Original Headlines: {original_headlines}")
    print(f"New Headline: {new_headline}")
