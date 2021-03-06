# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import event_pb2 as event__pb2


class EventHandlerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ExecAction = channel.unary_unary(
                '/EventHandler/ExecAction',
                request_serializer=event__pb2.ExecActionRequest.SerializeToString,
                response_deserializer=event__pb2.ExecActionReply.FromString,
                )
        self.Test = channel.unary_unary(
                '/EventHandler/Test',
                request_serializer=event__pb2.TestMessage.SerializeToString,
                response_deserializer=event__pb2.TestReply.FromString,
                )


class EventHandlerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ExecAction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Test(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EventHandlerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ExecAction': grpc.unary_unary_rpc_method_handler(
                    servicer.ExecAction,
                    request_deserializer=event__pb2.ExecActionRequest.FromString,
                    response_serializer=event__pb2.ExecActionReply.SerializeToString,
            ),
            'Test': grpc.unary_unary_rpc_method_handler(
                    servicer.Test,
                    request_deserializer=event__pb2.TestMessage.FromString,
                    response_serializer=event__pb2.TestReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'EventHandler', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EventHandler(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ExecAction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/EventHandler/ExecAction',
            event__pb2.ExecActionRequest.SerializeToString,
            event__pb2.ExecActionReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Test(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/EventHandler/Test',
            event__pb2.TestMessage.SerializeToString,
            event__pb2.TestReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
