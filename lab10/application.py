from data import Bank

bank = Bank()
bank.add_customer('Jonathan', 123)
bank.add_customer('theodor', 124)
customer = bank.get_customer(1)
print(customer)
customer = bank.find_customer_by_part_of_name('th')
print(customer[1])

running = True

while True:

    print('1. Skapa en ny kund\n' + '2. Skapa ett nytt konto')
    print('3. Ta bort konto\n' + '4. Sätta in pengar')
    print('5. Ta ut pengar\n' + '6. Överför pengar')
    print('7. Skriv ut alla konton\n' + '8. Sök på kund på del av namn')
    print('9. Skriv ut samtliga kunder och dess konton\n' + '10. Avsluta programmet')
    user_input = input('Välj ett alternativ: ')

    if user_input == '10':
        break