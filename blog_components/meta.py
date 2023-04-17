import os

import openai
from dotenv import load_dotenv

load_dotenv()

# API Keys
openai.api_key = os.environ.get("OPENAI_API_KEY")


def get_excerpt(blog_title, blog_body):
    """
    Generates an excerpt for a given blog post using OpenAI API.

    :param blog_title: str, the title of the blog post.
    :param blog_body: str, the body of the blog post.
    :return: str, generated excerpt for the blog post.
    """
    prompt = f"""
        You are a content writer tasked with creating an excerpt for the following blog post.

        Title: {blog_title}

        Body:
        {blog_body}

        The excerpt should:
        - Be concise and limited to a few sentences.
        - Capture the main theme of the blog post.
        - Entice the reader to click and read the full post.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def get_tags(blog_title, blog_body):
    """
    Generates tags for a given blog post using OpenAI API.

    :param blog_title: str, the title of the blog post.
    :param blog_body: str, the body of the blog post.
    :return: str, generated tags for the blog post.
    """
    prompt = f"""
        You are a content writer tasked with creating tags for the following blog post.

        Title: {blog_title}

        Body:
        {blog_body}

        The tags should:
        - Be concise and limited to a few words.
        - Capture the main theme of the blog post.
        - Be relevant to the topic of the blog post.

        Returning only the tags as a comma separated list.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
