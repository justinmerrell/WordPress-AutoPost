import os

import runpod
import openai

from dotenv import load_dotenv

load_dotenv()

# API Keys
runpod.api_key = os.environ.get("RUNPOD_API_KEY")
openai.api_key = os.environ.get("OPENAI_API_KEY")


def generate_img_prompts(blog_title, blog_post, title_prompt, body_prompt):
    """
    Generates an image prompt based on the provided blog title and post using OpenAI API.

    :param blog_title: str, the title of the blog post.
    :param blog_post: str, the body of the blog post.
    :return: str, generated image prompt.
    """
    prompt = """
        Create an image prompt that captures the essence of the blog post title and body.

        The prompt should result in a beautiful and relevant image when used with an AI image generation model.
        The style should be hyper-realistic and the image should be of high quality.
        Only return the prompt, no need to provide an introduction or explanation.

        Examples of good image prompts include language like:
        - trending on pixiv, detailed, clean lines, sharp lines, crisp lines, award winning illustration, masterpiece, 4k, eugene de blaas and ross tran, vibrant color scheme, intricately detailed
        - cinematic, colorful background, concept art, dramatic lighting, high detail, highly detailed, hyper realistic, intricate, intricate sharp details, octane render, smooth, studio lighting, trending on artstation
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "assistant", "content": title_prompt},
            {"role": "system", "content": blog_title},
            {"role": "assistant", "content": body_prompt},
            {"role": "system", "content": blog_post},
            {"role": "user", "content": prompt}
        ]
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
