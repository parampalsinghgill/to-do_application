class AuthMenu:
    """Menu to interact with auth module"""

    def __init__(self):
        """Initializes AithMenu with instance variables"""
        self.auth_menu_options = {
            "1": self.login,
            "2": self.signup
        }

    def login(self):
        """Logs in existing user"""
        pass

    def signup(self):
        """Sign up a new user"""
        pass
