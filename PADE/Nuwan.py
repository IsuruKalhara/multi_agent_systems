from pade.misc.utility import display_message, start_loop, call_later
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID


class Nuwan(Agent):

    def __init__(self, aid):

        self.nuwanSalary = 50000
        self.nuwanWealth = 5000000
        self.landPrice = 0
        self.carPrice = 0
        super(Nuwan, self).__init__(aid=aid, debug=False)
        display_message(self.aid.localname, 'Here is Nuwan. He has '+str(self.nuwanWealth) + ' and a job with '+ str(self.nuwanSalary) + ' salary')

    def on_start(self):
        super(Nuwan, self).on_start()
        display_message(self.aid.localname, 'sending Message...')
				
        call_later(8.0, self.asking_land_price)
        call_later(10.0, self.buy_the_land)
        call_later(12.0, self.asking_car_price)
        call_later(14.0, self.buy_the_car)

    def asking_land_price(self):
        display_message(self.aid.localname, 'Going to meet land owner')
        msg = "I need to buy the house. What is the price?"
        message = ACLMessage(ACLMessage.INFORM)
        message.add_receiver(AID('land_owner'))
        message.set_content(msg)
        self.send(message)

    def asking_car_price(self):

        display_message(self.aid.localname, 'Going to the car sale')
        msg = "I need to buy the car. What is the price?"
        message = ACLMessage(ACLMessage.INFORM)
        message.add_receiver(AID('car_sale'))
        message.set_content(msg)
        self.send(message)

    def buy_the_car(self):
        
        display_message(self.aid.localname, 'Giving money to the car sale')
        msg = "Here is the money?"
        message = ACLMessage(ACLMessage.INFORM)
        message.add_receiver(AID('car_sale'))
        message.set_content(msg)
        self.send(message)


    def buy_the_land(self):

        display_message(self.aid.localname, 'Giving money to the land owner')
        msg = "Here is the money?"
        message = ACLMessage(ACLMessage.INFORM)
        message.add_receiver(AID('land_owner'))
        message.set_content(msg)
        self.send(message)

    def react(self, message):
        super(Nuwan, self).react(message)
        
        if (message.sender.name.split('@')[0]=="land_owner"):

            display_message(self.aid.localname, 'Message received from {}'.format(message.sender.name.split('@')))

            print("Msg from Land Owner = ",message.content)
            if message.content == "Thank You" :
                self.nuwanWealth -= self.landPrice
                display_message(self.aid.localname, "I bought the land")
        			
            else:
                self.landPrice = message.content 
                print("Land price is ",message.content )
                display_message(self.aid.localname, "I'm going to buy the land")

        elif (message.sender.name.split('@')[0]=="car_sale"):

            display_message(self.aid.localname, 'Message received from {}'.format(message.sender.name.split('@')))
            
            print("Msg from Car Sale = ",message.content)
            if message.content == "Thank You" :
                self.nuwanWealth -= self.carPrice
                display_message(self.aid.localname, "I bought the car")
            		
            else:
                self.carPrice = message.content 
                print("Car price is ",message.content )
                display_message(self.aid.localname, "I'm going to buy the car")
           
