import os
import openai
from dotenv import load_dotenv

load_dotenv()

# API Keys
openai.api_key = os.environ.get("OPENAI_API_KEY")


def generate_content(blog_title):
    """
    Generates content for a blog post using OpenAI API.

    :param blog_title: str, the title of the blog post.
    :return: str, generated content for the blog post.
    """
    prompt = f"""
        You are a ghostwriter commissioned to write a blog post titled: `{blog_title}`.
        The blog posts should explore the shared desires, fears, and aspirations of humanity, always ending on an optimistic note.
        The blog needs to be relevant to the title, but do not include the title in the body of the blog post.
        Try to write it in a way that mimics the style from the following examples; do not paraphrase the examples; the content should be original.

        Keep the following guidelines in mind while writing the post:
        - Use a clear and concise writing style, avoiding overly complex language or jargon.
        - Maintain a conversational and relatable tone.
        - Organize the content logically, separating different ideas or points into paragraphs.
        - Include real-life examples and anecdotes to illustrate your points.
        - Provide actionable advice, tips, or insights to help readers improve their time management skills.
        - Draw inspiration from `How to Drop Out` by Ran Prieur, #1: a general theory of collaboration by Gray Mirror, On Hacking by Richard Stallman
        - Channel the personality of George Hotz
        """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    blog_title = "Dedication | Being an Entrepreneur"
    blog_body = generate_content(blog_title)
    print(f"Blog Title: {blog_title}")
    print(f"Blog Body: {blog_body}")
