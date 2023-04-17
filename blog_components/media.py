import os

import runpod
import openai

from dotenv import load_dotenv

load_dotenv()

# API Keys
runpod.api_key = os.environ.get("RUNPOD_API_KEY")
openai.api_key = os.environ.get("OPENAI_API_KEY")


def generate_img_prompts(blog_title, blog_post):
    """
    Generates an image prompt based on the provided blog title and post using OpenAI API.

    :param blog_title: str, the title of the blog post.
    :param blog_post: str, the body of the blog post.
    :return: str, generated image prompt.
    """
    prompt = f"""
        Create an image prompt that captures the essence of a blog post titled '{blog_title}' with the following content:

        {blog_post}

        The prompt should result in a beautiful and relevant image when used with an AI image generation model.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def produce_image(image_prompt):
    """
    Generates an image using RunPod API based on the provided image prompt.

    :param image_prompt: str, the image prompt.
    :return: str, generated image URL.
    """
    negative_prompt = """
        Avoid:
        - un-detailed skin
        - semi-realistic, cgi, 3d, render, sketch, cartoon, drawing
        - ugly eyes, worst quality, low quality, jpeg artifacts
        - white robe, easynegative, bad-hands-5, grainy, low-res
        - extra limb, poorly drawn hands, missing limb, blurry, malformed hands, blur
        - nude, naked, porn, gross, ugly, bad, bad quality
    """

    endpoint = runpod.Endpoint("stable-diffusion-v1")

    run_request = endpoint.run({"prompt": image_prompt, "negative_prompt": negative_prompt})

    run_results = run_request.output()

    return run_results[0]["image"]
