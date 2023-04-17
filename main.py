from blog_components.headline import blog_post_title
from blog_components.body import generate_content
from blog_components.meta import get_excerpt
from blog_components.media import generate_img_prompts, produce_image
from wordpress_post import create_post, upload_image_to_wordpress

blog_title = blog_post_title()
blog_body = generate_content(blog_title)
blog_post_excerpt = get_excerpt(blog_title, blog_body)

print(f"Blog Title: {blog_title}")
print(f"Blog Body: {blog_body}")
print(f"Blog Excerpt: {blog_post_excerpt}")

image_prompt = generate_img_prompts(blog_title, blog_body)
print(f"Image Prompt: {image_prompt}")

image_url = produce_image(image_prompt)
print(f"Image URL: {image_url}")

image_id = upload_image_to_wordpress(image_url)
print(f"Image ID: {image_id}")

# Post to WordPress
create_post(blog_title, blog_body, blog_post_excerpt, image_id)
