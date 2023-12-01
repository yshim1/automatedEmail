class UserPass:
    def __init__(self, email, password):
        self.email = email
        self.__password = password
        
    def get_email(self):
        return self.email
    
    def change_email(self):
        self.email = input('Retype your email: ')
    
    def change_password(self):
        self.__password = input('Retype your password: ')