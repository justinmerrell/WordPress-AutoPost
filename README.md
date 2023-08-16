# Automated Blog Post Generator

This project is an automated blog post generator that creates a blog post title, body, and excerpt, generates an image based on the content, and uploads the post to a WordPress site using the WordPress REST API.

## Project Structure

    - blog_components/headline.py: Generates the blog post title.
    - blog_components/body.py: Generates the blog post content.
    - blog_components/meta.py: Generates the blog post excerpt.
    - blog_components/media.py: Generates image prompts and produces an image using an external image generation API.
    - wordpress_post.py: Contains functions for creating a post and uploading an image to WordPress using the REST API.
    - main.py: Brings everything together and creates a blog post on a WordPress site.

## Requirements

    - Python 3.6 or higher
    - requests library
    - dotenv library

## Setup

1. Clone the repository and install the required libraries:

    ```bash
    git clone https://github.com/yourusername/automated-blog-post-generator.git
    cd automated-blog-post-generator
    pip install -r requirements.txt
    ```

2. Create a .env file in the root directory of the project with the following variables:

    ```bash
    WORDPRESS_SITE_URL=your_wordpress_site_url
    WORDPRESS_USERNAME=your_wordpress_username
    WORDPRESS_PASSWORD=your_wordpress_password

    NEWSAPI_KEY=your_newsapi_key
    OPENAI_API_KEY=your_openai_api_key

    RUNPOD_API_KEY=your_runpod_api_key
    ```

    Replace your_wordpress_site_url, your_wordpress_username, and your_wordpress_password with the appropriate values for your WordPress site.

3. Run the main.py script:

    ```bash
    python main.py
    ```

    This script will generate a blog post title, body, and excerpt, create an image based on the content, and upload the post to your WordPress site.
