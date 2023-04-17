import os
import json
import requests
from urllib.request import urlretrieve
from urllib.parse import urlparse

from dotenv import load_dotenv

load_dotenv()

# Replace the following with your own WordPress site URL, username, and password
WORDPRESS_SITE_URL = os.environ.get("WORDPRESS_SITE_URL")
WORDPRESS_USERNAME = os.environ.get("WORDPRESS_USERNAME")
WORDPRESS_PASSWORD = os.environ.get("WORDPRESS_PASSWORD")


def get_jwt_token():
    """Obtain JWT token from the WordPress website."""
    url = f"{WORDPRESS_SITE_URL}/wp-json/jwt-auth/v1/token"
    auth_data = {'username': WORDPRESS_USERNAME, 'password': WORDPRESS_PASSWORD}
    response = requests.post(url, data=auth_data)

    if response.status_code == 200:
        return response.json()['token']
    else:
        raise Exception(f"Error: Unable to obtain JWT token. Status code: {response.status_code}")


def get_content_type(file_extension):
    """Get the appropriate content type for the file extension."""
    if file_extension == ".jpg" or file_extension == ".jpeg":
        return "image/jpeg"
    elif file_extension == ".png":
        return "image/png"
    else:
        raise ValueError(f"Unsupported file extension: {file_extension}")


def create_post(title, content, excerpt, featured_media_id, tags, token=None):
    """Create a new WordPress post with the given content and featured media."""

    url = f"{WORDPRESS_SITE_URL}/wp-json/wp/v2/posts"

    if token is None:
        token = get_jwt_token()

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {token}"
    }

    post_data = {
        'title': title,
        'content': content,
        'excerpt': excerpt,
        'featured_media': featured_media_id,
        'tags': tags,
        'status': 'publish'
    }

    response = requests.post(url, headers=headers, data=json.dumps(post_data))

    if response.status_code == 201:
        print(f"Post created successfully! URL: {response.json()['link']}")
    else:
        print(f"Error: Unable to create post. Status code: {response.status_code}")
        print(response.text)


def upload_image_to_wordpress(image_url, token=None):
    """Upload an image to the WordPress website from a given URL."""
    url = f"{WORDPRESS_SITE_URL}/wp-json/wp/v2/media"

    if token is None:
        token = get_jwt_token()

    # Download the image from the URL
    parsed_url = urlparse(image_url)
    image_filename = os.path.basename(parsed_url.path)
    urlretrieve(image_url, image_filename)

    # Read the image data and encode it in base64
    with open(image_filename, "rb") as image_file:
        image_data = image_file.read()

    # Get the content type based on the file extension
    file_extension = os.path.splitext(image_filename)[1]
    content_type = get_content_type(file_extension)

    # Create the headers for the API request
    headers = {
        "Content-Type": content_type,
        "Content-Disposition": f"attachment; filename={image_filename}",
        'Authorization': f"Bearer {token}"
    }

    # Send the POST request to upload the image
    response = requests.post(url, headers=headers, data=image_data)

    # Remove the downloaded image file
    os.remove(image_filename)

    # Check the response and return the uploaded image ID
    if response.status_code == 201:
        image_id = response.json()["id"]
        return image_id
    else:
        raise Exception(
            f"Error uploading image. Status code: {response.status_code}\n{response.text}")


# ---------------------------------------------------------------------------- #
#                                     Tags                                     #
# ---------------------------------------------------------------------------- #

def get_tag_id_by_name(tag_name, token=None):
    if token is None:
        token = get_jwt_token()

    url = f"{WORDPRESS_SITE_URL}/wp-json/wp/v2/tags"
    headers = {
        'Authorization': f"Bearer {token}"
    }

    params = {
        'search': tag_name
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        tags = response.json()
        if tags:
            return tags[0]['id']
    return None


def create_tag(tag_name, token=None):
    if token is None:
        token = get_jwt_token()

    url = f"{WORDPRESS_SITE_URL}/wp-json/wp/v2/tags"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {token}"
    }

    tag_data = {
        'name': tag_name
    }

    response = requests.post(url, headers=headers, data=json.dumps(tag_data))

    if response.status_code == 201:
        return response.json()['id']
    else:
        raise Exception(f"Error creating tag. Status code: {response.status_code}\n{response.text}")


def get_or_create_tags(tag_names, token=None):
    if token is None:
        token = get_jwt_token()

    tag_ids = []
    for tag_name in tag_names:
        tag_id = get_tag_id_by_name(tag_name, token)
        if tag_id is None:
            tag_id = create_tag(tag_name, token)
        tag_ids.append(tag_id)

    return tag_ids
