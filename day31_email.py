# Create a program that checks if a given string is a valid email address.
#import re
# why is it a bad idea to use regex: https://stackoverflow.com/a/48170419
# proper regex is really huge: https://stackoverflow.com/a/201378
# (?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])
# some people use requests to a site like "https://units.d8u.us/email"
# safest is to check if this email can be actually sent email to and use email-validator pypi package

#    #pattern = '[\w\.-]+@\w+\.\w+'
#    #return re.match(pattern, inp) is not None

from email_validator import validate_email, EmailNotValidError
def is_email(email:str, check_deliverability=False):
    """
    Checks if input string is a valid email address.
    """
    if not isinstance(email , str):
        raise TypeError('please provide a string')
   
    # from package info:
    try:
    # Check that the email address is valid. Turn on check_deliverability
    # for first-time validations like on account creation pages (but not
    # login pages).
        emailinfo = validate_email(email, check_deliverability=check_deliverability)
    # After this point, use only the normalized form of the email address,
    # especially before going to a database query.
        email = emailinfo.normalized
        print(f'email {email} is valid')
    except EmailNotValidError as e:
    # The exception message is human-readable explanation of why it's
    # not a valid (or deliverable) email address.
        print(str(e))
    return None
    
if __name__=="__main__":
    is_email(input('your email:'))
