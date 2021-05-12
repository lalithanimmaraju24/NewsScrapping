from jsonrpcclient.clients.http_client import HTTPClient



client = HTTPClient("http://localhost:6060/")

def classify(text):
    topic = client.call('classify', text)
    print ("Topic: %s" % str(topic))
    return topic
