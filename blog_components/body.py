import os
import openai
from dotenv import load_dotenv

load_dotenv()

# API Keys
openai.api_key = os.environ.get("OPENAI_API_KEY")


def generate_content(blog_title, blog_title_prompt):
    """
    Generates content for a blog post using OpenAI API.

    :param blog_title: str, the title of the blog post.
    :return: str, generated content for the blog post.
    """
    prompt = f"""
        You are a ghostwriter commissioned to write a blog post titled: {blog_title}.
        The blog posts should explore the shared desires, fears, and aspirations of humanity, always ending on an optimistic note.
        The blog needs to be relevant to the title, but do not include the title in the body of the blog post.

        Keep the following guidelines in mind while writing the post:
        - Use a clear and concise writing style, avoiding overly complex language or jargon.
        - Maintain a conversational and relatable and engaging tone.
        - Use a mix of both informative and conversational styles to effectively communicate your story and experiences.
        - Organize the content logically, separating different ideas or points into paragraphs.
        - Keep the content more general, focusing on providing insights and advice without relying too heavily on personal anecdotes.
        - Provide actionable advice, tips, or insights to help readers in their personal and professional lives.
        - Draw inspiration from a variety of sources, such as the writings of Ran Prieur, Gray Mirror, and Richard Stallman, as well as the personality of George Hotz.
        - Ensure the content aligns with one or more of the following themes: artificial intelligence, technology trends, entrepreneurship, or personal development.

        Experiences to draw inspiration from:
        Justin Merrell is a software developer and entrepreneur with diverse experiences, including dropping out of college, founding a successful makerspace, and embracing a minimalistic lifestyle.
        He has a strong background in various projects and has learned the importance of considering alternative perspectives and giving others the benefit of the doubt.
        His core values center around not following the masses, seeking happiness outside of the traditional path, and continuously learning and growing.
        Justin is working on building a consistent online presence and generating content to share his insights and experiences with a broader audience.
        """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "assistant", "content": blog_title_prompt},
            {"role": "system", "content": blog_title},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content, prompt


if __name__ == "__main__":
    blog_title = "Dedication | Being an Entrepreneur"
    blog_body, _ = generate_content(blog_title)
    print(f"Blog Title: {blog_title}")
    print(f"Blog Body: {blog_body}")
