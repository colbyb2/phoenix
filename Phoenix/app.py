import argparse
import openai
from termcolor import colored
from . import config

manager = config.ConfigManager()

#Get any config file data
def check_config():
    if manager.key == None:
        manager.key = input(colored('Paste OpenAI API Key: ', 'light_green'))
        manager.save_config_data()

#Ask ChatGPT question and print response
def ask_question(question):
    prompt = question + 'Keep response to under 100 words.'
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
    print(colored('Phoenix:', 'light_red') + response.choices[0].message.content)

def loop():
    print(colored('Phoenix:', 'light_red') + " Hello, how can I help you?")
    command = False
    while True:
        if command:
            print(colored('Phoenix:', 'light_red') + " Okay, how can I help you?")
        print('')
        prompt = input(colored('~', 'blue'))
        if prompt[0] == ':':
            command = True
        if prompt.lower() == ':quit':
            return
        elif prompt.lower() == ':help':
            print(colored('\nPhoenix Help:', 'light_red'))
            print('Precede all commands with a colon (:).')
            print('Quit: Terminates App.')
            print('Help: Pulls up help menu.')
            print('Key: Edit API Key.\n')
            continue
        elif prompt.lower() == ':key':
            print(colored('Current API Key: ', 'light_green') + manager.key)
            cont = input("Change key? (y/n): ").lower()
            if cont == 'y':
                manager.key = input(colored('Paste OpenAI API Key: ', 'light_green'))
                manager.save_config_data()
                openai.api_key = manager.key
            command = False
            continue
        elif command:
            print(colored('Phoenix:', 'light_red') + " Sorry, that is an invalid command. Use :Help to see options.")
            command = False
            continue
        print('')
        ask_question(prompt)

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--version", action='version', version='%(prog)s 0.2')

    parser.add_argument("-q", dest="question", type=str, help="The question to be asked.", default="NONE")

    args = parser.parse_args()

    check_config()

    openai.api_key = manager.key

    if not args.question == 'NONE':
        ask_question(args.question)
        return
    
    loop()


if __name__ == '__main__':
    main()