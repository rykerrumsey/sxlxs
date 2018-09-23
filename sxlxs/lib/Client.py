class Client:
    def __init__(self, firstname, lastname, email, phone, payment_method, payment_status, issues, notes):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.payment_method = payment_method
        self.payment_status = payment_status
        self.issues = issues
        self.notes = notes

    def __str__(self):
        pass

    def print_client(self):
        print('{0} {1} has {2} issues.'.format(self.firstname, self.lastname, self.issues))
