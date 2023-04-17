from blog_components.headline import blog_post_title
from blog_components.body import generate_content
from blog_components.meta import get_excerpt, get_tags
from blog_components.media import generate_img_prompts, produce_image
from wordpress_post import create_post, upload_image_to_wordpress, get_or_create_tags
from modifiers.modify_body import add_disclaimer

blog_title, title_prompt = blog_post_title()
blog_body, body_prompt = generate_content(blog_title, title_prompt)
blog_post_excerpt = get_excerpt(blog_title, blog_body)
blog_post_tags = get_tags(blog_title, blog_body)

print(f"Blog Title: {blog_title}")
print(f"Blog Body: {blog_body}")
print(f"Blog Excerpt: {blog_post_excerpt}")
print(f"Blog Tags: {blog_post_tags}")

image_prompt = generate_img_prompts(blog_title, blog_body, title_prompt, body_prompt)
print(f"Image Prompt: {image_prompt}")

image_url = produce_image(image_prompt)
print(f"Image URL: {image_url}")

image_id = upload_image_to_wordpress(image_url)
print(f"Image ID: {image_id}")

blog_body = add_disclaimer(blog_body)
tag_ids = get_or_create_tags(blog_post_tags)

# Post to WordPress
create_post(blog_title, blog_body, blog_post_excerpt, image_id, tag_ids)
