from repos.base_repo import BaseRepository
from models.ticket_model import Ticket

class TicketRepository(BaseRepository):
    def __init__(self, db_session=None):
        super().__init__(Ticket, db_session)

    def mark_as_used(self, ticket_id: int):
        ticket = self.get_by_id(ticket_id)        
        if ticket:
            ticket.isUsed = True                  
            self.db_session.commit()              
        return ticket                            

    def find_by_event_name(self, event_name: str):
        return self.db_session.query(self.model).filter_by(eventName=event_name).first()
