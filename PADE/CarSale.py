
from pade.misc.utility import display_message, start_loop, call_later
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID

class CarSale(Agent):

		
    def __init__(self, aid):
        self.carPrice = 1500000 
        self.wealth = 0
        super(CarSale, self).__init__(aid=aid, debug=False)


    def react(self, message):
        super(CarSale, self).react(message)
        
        sender_name = message.sender.name.split('@')[0]
        if sender_name == "nuwan":

                display_message(self.aid.localname, 'Message received from {}'.format(message.sender.name.split('@')))
                
                if message.content == "I need to buy the car. What is the price?":
                        data = self.carPrice
                        self.sending_message(data)
                elif message.content == "Here is the money?":
                        data = "Thank You"
                        self.wealth = self.carPrice
                        self.carPrice = 0
                        self.sending_message(data)

   
    def sending_message(self,content):
        message = ACLMessage(ACLMessage.INFORM)
        message.add_receiver(AID('nuwan'))
        message.set_content(content)
        self.send(message)




