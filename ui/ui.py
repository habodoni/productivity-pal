class UserInterface:
    def __init__(self):
        print("Welcome to Productivity Pal!")

    def get_user_command(self):
        return input("Enter a command (e.g., 'focus mode', 'analyze productivity'): ")

    def display_response(self, response):
        print(response)

        #Test for git