from twisted.internet import reactor
from coc.message.definitions import CoCMessageDefinitions
from coc.server.endpoint import CoCServerEndpoint
from coc.server.factory import CoCServerFactory
from coc.client.endpoint import CoCClientEndpoint
from coc.proxyconfig import ProxyConfig
from coc.replay import Replay

config_file = "config.json"
    
if __name__ == "__main__":

    ProxyConfig.start(config_file)
    Replay.start()
    definitions = CoCMessageDefinitions.read()
    client_endpoint = CoCClientEndpoint(reactor, "game.clashroyaleapp.com", 9339)
    server_endpoint = CoCServerEndpoint(reactor, 9339)
    server_endpoint.listen(CoCServerFactory(client_endpoint, definitions))

    print("listening on {}:{} ...".format(server_endpoint.interface, server_endpoint.port))

    reactor.run()
