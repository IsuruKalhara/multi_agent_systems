from pade.misc.utility import display_message, start_loop, call_later
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from Nuwan import Nuwan
from LandOwner import LandOwner
from CarSale import CarSale
if __name__ == '__main__':

    agents = list()
    port = 4004
    nuwan = Nuwan(AID(name='nuwan@localhost:{}'.format(port)))
    agents.append(nuwan)

    port += 1
    carSale = CarSale(AID(name='car_sale@localhost:{}'.format(port)))
    agents.append(carSale)

    port += 1
    landOwner = LandOwner(AID(name='land_owner@localhost:{}'.format(port)))
    agents.append(landOwner)
    start_loop(agents)
