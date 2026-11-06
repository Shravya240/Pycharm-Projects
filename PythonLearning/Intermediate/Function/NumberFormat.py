

def clean_phone_number(ph_number):
    ph_number.replace("+", "")
    # todo
    return ph_number

def is_valid_Number(number):
    if len(number)<10 or len(number) >15:   # Check Condidtion
        return "Invalid Number"
    else:
        number.startswith("00")


def process_number():
    ph_number = "+49 (176) 123-4567"
    ph_number = clean_phone_number(ph_number)
    ph_number = is_valid_Number(ph_number)