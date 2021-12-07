import pytest
import logging as logger

from ssqaapitest.src.utilities.genericUtilities import generate_random_email_and_password
from ssqaapitest.src.helpers.customers_helper import CustomerHelper
from ssqaapitest.src.do.customers_dao import CustomersDAO

@pytest.mark.tcid29
def test_create_customer_only_email_password():
    logger.info("TEST: Create new customer with email and password")
    logger.debug("TEST: Create new customer with email and password")
    rand_info = generate_random_email_and_password()
    logger.info(rand_info)
    email = rand_info['email']
    password = rand_info['password']

    # make the call
    cust_obj = CustomerHelper()
    cust_api_info = cust_obj.create_customer(email=email, password=password)
    # import pdb; pdb.set_trace()

    # verify email and first name in the response
    assert cust_api_info['email'] == email, f"Create customer api returned wrong email."
    assert cust_api_info['first_name'] == '', f"Create customer api returned a value for first_name" \
                                                f"but it should be empty"

    # verify customer is created in database
    cust_dao = CustomersDAO()
    cust_info = cust_dao.get_customer_by_email(email)

    id_in_api = cust_api_info['id']
    id_in_db = cust_info[0]['ID']
    assert id_in_api == id_in_db, f'Create customer response "id" not same as "ID" in database.' \
        f'Email: {email}'
    # import pdb; pdb.set_trace()

@pytest.mark.tcid47
def test_create_customer_fail_for_existing_email():
    # get existing email from db
    cust_dao = CustomerHelper()
    cust_dao.get_random_customer_from_db()
