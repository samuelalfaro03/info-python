
#1. **Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.**

def ticket_code():
    print("Welcome! Please enter the ticket code")
    ticket_access()

def ticket_access():
    print("Thank you! Your receipt will be sent via email")
    ticket_code()
