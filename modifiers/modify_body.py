def add_disclaimer(blog_body):
    disclaimer = """
    <hr>
    <p><em>This blog post was generated autonomously by an AI program. The source code is published on my <a href="https://github.com/justinmerrell" target="_blank" rel="noopener noreferrer">GitHub page</a>. If you like this content, please consider following me and sponsoring my work.</em></p>
    """

    return blog_body + disclaimer
