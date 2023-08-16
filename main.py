import argparse

from src.blog_components.headline import blog_post_title
from src.blog_components.body import generate_content
from src.blog_components.meta import get_excerpt, get_tags
from src.blog_components.media import generate_img_prompts, produce_image
from src.wordpress import create_post, upload_image_to_wordpress, get_or_create_tags
from src.modifiers.modify_body import add_disclaimer
from src.utils.health import send_healthcheck


def main(live=False):
    """
    Generate Blog Title
    """
    blog_title, title_prompt = blog_post_title()
    print(f"Blog Title: {blog_title}")

    # ------------------------ Generate Blog Body Content ------------------------ #
    blog_body, body_prompt = generate_content(blog_title, title_prompt)
    print(f"Blog Body: {blog_body}")

    # ------------------------ Generate Blog Post Excerpt ------------------------ #
    blog_post_excerpt = get_excerpt(blog_title, blog_body)
    print(f"Blog Excerpt: {blog_post_excerpt}")

    # ---------------------------- Generate Blog Tags ---------------------------- #
    blog_post_tags = get_tags(blog_title, blog_body)
    print(f"Blog Tags: {blog_post_tags}")

    # ------------------ Generate Image Prompt and Upload Image ------------------ #
    image_prompt = generate_img_prompts(blog_title, blog_body, title_prompt, body_prompt)
    print(f"Image Prompt: {image_prompt}")

    image_url = produce_image(image_prompt)
    print(f"Image URL: {image_url}")

    image_id = upload_image_to_wordpress(image_url)
    print(f"Image ID: {image_id}")

    # ------------------------- Additional Modifications ------------------------- #
    blog_body = add_disclaimer(blog_body)
    tag_ids = get_or_create_tags(blog_post_tags)

    # ------------------------- Post Content to WordPress ------------------------ #
    if live:
        create_post(blog_title, blog_body, blog_post_excerpt, image_id, tag_ids)
    else:
        print("Not posting to WordPress because --live flag was not set.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Post blog to WordPress.')
    parser.add_argument('--live', action='store_true',
                        help='If set, the tweet will be posted to WordPress. Otherwise, the tweet will be printed to the console.')

    args = parser.parse_args()

    try:
        main(args.live)
        send_healthcheck()
    except Exception as err:
        send_healthcheck(fail=True)
        raise err
