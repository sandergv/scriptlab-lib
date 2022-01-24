from scriptmanager.action_pb2 import TestMessage
from scriptmanager.action_pb2_grpc import ActionHandlerStub
import grpc

req = TestMessage(message="prueba")

print(req.message)

channel = grpc.insecure_channel("localhost:8080")
client = ActionHandlerStub(channel)
for i in range(1000):
    res = client.Test(req)
    print(res)

