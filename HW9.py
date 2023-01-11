CONTACTS = {}

def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except KeyError:
            print("This command does not exist")
        except ValueError:
            print("Enter correct phone number")
        except NameError:
            print("Enter correct name")
        except IndexError:
            print("Enter valid command")

    return wrapper

@input_error
def hello(*args):
  return 'How can I help you?'

@input_error
def add_contact(*args):
    name = args[0]
    phone = args[1]
    if phone.isdigit():
        CONTACTS.update({name: phone})
    else:
        raise ValueError
    
    return CONTACTS

@input_error
def change_contact(*args):
    name = args[0]
    phone = args[1]
    if name in CONTACTS:
        if phone.isdigit():
            CONTACTS[name] = phone
        else:
            raise ValueError
    else:
        raise NameError

    return CONTACTS

@input_error
def show_phone(*args):
    name = args[0]
    return CONTACTS[name]

@input_error
def show_all_phones(*args):
    for k, v in CONTACTS.items():
        print(f"{k.title()}: {v}")

COMMANDS = {
    add_contact: 'add',
    change_contact: 'change',
    show_phone: 'phone',
    show_all_phones: 'show all',
    hello: 'hello'}


def command_parser(user_input: str):
    for command, key_word in COMMANDS.items():
        if user_input.startswith(key_word):
            return command, user_input.replace(key_word, '').strip().split(' ')


def main():
    while True:
        user_input = input('Enter your command: ')
        if user_input in ['good bye', 'close', 'exit', '.']:
            print('Good bye!')
            break
        command, data = command_parser(user_input)
        print(command(*data))

if __name__ == 'main':
    main()