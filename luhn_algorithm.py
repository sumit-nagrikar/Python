def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1] # reversing saving entire string

    odd_digits = card_number_reversed[::2] # skipping every other char

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2] # skipping one starting from 1st char not 0 starting from 1
    for digit in even_digits:
        number = int(digit) * 2 # multiplying each digit from even digits
        if number >= 10:
            number = (number // 10) + (number % 10) # extracing & adding first and second digit
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0 # if total equals zero there we are -- VALID

def main():
    card_number = '4111-1111-4555-1144'
    # creating a translation table
    card_translation = str.maketrans({'-': '', ' ': ''})

    # creating translated_card_number using translation table/like in ATM we removed all -- dash and spaces form card number
    translated_card_number = card_number.translate(card_translation)

    # checking the number is valid or not using helper function
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()