import os
import logging
import requests

from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger("blog")

HEALTH_URL = os.getenv("HEALTHCHECKS_URL", "http://localhost:8000/health")
BLOG_HEALTH_ID = os.getenv("BLOG_HEALTHCHECKS_ID", None)


def send_healthcheck(fail=False):
    '''
    Send a healthcheck to healthchecks
    '''
    if BLOG_HEALTH_ID is None:
        logging.warning("No healthcheck ID provided. Skipping healthcheck.")
        return

    if fail:
        logging.info("Sending failed healthcheck.")
        requests.get(f"{HEALTH_URL}/{BLOG_HEALTH_ID}/fail", timeout=5)
        return

    logging.info("Sending successful healthcheck.")
    requests.get(f"{HEALTH_URL}/{BLOG_HEALTH_ID}", timeout=5)
