import sys

from getpass import getpass
from instagram_private_api import Client, ClientLoginError, ClientError
from input_state import InputState
from input_states.abstract_input_state import AbstractInputState


class LoginInputState(AbstractInputState):
    def list_info(self):
        self.console.print("\nFill in your Instagram credentials to allow authorization. Type :quit to exit the "
                           "application", style="light_salmon3")

    def handle_input(self, prefix, input_state, client) -> (InputState, Client):
        try:
            username = input("\tUsername: ")
            if username == ":quit":
                sys.exit()

            password = getpass("\tPassword: ")
            if password == ":quit":
                sys.exit()

            self.console.print("\tLogging in...")
            client = Client(username, password)
            self.console.print("\tLogin successful!", style="spring_green3")
            return InputState.MAIN_MENU, client
        except ClientLoginError:
            self.console.print("\tUsername or password were incorrect, try again.", style="red3")
            return input_state, client
        except ClientError:
            self.console.print("\tYou made too many API requests, try again later.", style="red3")
            return input_state, client