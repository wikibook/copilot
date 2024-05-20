def clean_number(phone_number):
    phone_number = phone_number.replace("(", "")
    phone_number = phone_number.replace(")", "")
    phone_number = phone_number.replace("-", "")
    return phone_number
