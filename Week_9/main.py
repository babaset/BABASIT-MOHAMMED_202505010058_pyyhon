from ticket import create_ticket
from display import display_ticket

def main():
    ticket_data = create_ticket()
    
    
    if ticket_data:
        display_ticket(ticket_data)

if __name__ == "__main__":
    main()