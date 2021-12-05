import logging as logger
import random
import string
# import ssqaapitest.src.utilities


def generate_random_email_and_password(domain=None, email_prefix=None):
    logger.debug("Generating random email and password")
    if not domain:
        domain = 'supersqa.com'
    if not email_prefix:
        email_prefix = 'testuser'

    random_email_string_length = 10
    random_string = ''.join(random.choice(string.ascii_lowercase) for i in range(random_email_string_length))

    email = email_prefix + '_' + random_string + '@' + domain

    password_length = 20
    password_string = ''.join(random.choice(string.ascii_lowercase) for i in range(password_length))

    random_info = {'email': email, 'password': password_string}
    # logger.debug(f"Randomly generated email and password: {random_info}")

    return random_info
