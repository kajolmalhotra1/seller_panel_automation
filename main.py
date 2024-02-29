from dotenv import load_dotenv
import os
import grpc.aio
import payout_pb2
import payout_pb2_grpc
import crud
from database import SessionLocal
import asyncio
load_dotenv()

_cleanup_coroutines = []


def get_db():
    return SessionLocal()


class Payout(payout_pb2_grpc.PayoutServicer):
    async def GetFlatFees(self, request, context):
        db = get_db()
        result = crud.get_flat_fees(db)
        return payout_pb2.FlatFeesResponse(status_code=result['status_code'], status=result['status'],
                                           message=result['message'], data=result['data'])

    async def CreateFlatFees(self, request, context):
        db=get_db()
        result=crud.create_flat_fees(db,request)
        return payout_pb2.StatusResponse(status_code=result['status_code'],status=result['status'],message=result['message'])


async def serve():
    server = grpc.aio.server()
    payout_pb2_grpc.add_PayoutServicer_to_server(Payout(), server)
    grpc_port = f"{os.getenv('SERVER')}:{int(os.getenv('GRPC_PORT'))}"
    server.add_insecure_port(grpc_port)
    await server.start()
    # Logger("server").info("server started successfully")

    async def server_graceful_shutdown():
        print("gracefully shutting Down ")
        # Shuts down the server with 5 seconds of grace period. During the
        # grace period, the server won't accept new connections and allow
        # existing RPCs to continue within the grace period.
        await server.stop(5)

    _cleanup_coroutines.append(server_graceful_shutdown())
    await server.wait_for_termination()


if __name__ == '__main__':
    print('starting server')
    # logging.basicConfig(filename="logs.log", level=logging.DEBUG)
    # logging.info("Server started")
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(serve())
    finally:
        loop.run_until_complete(*_cleanup_coroutines)
        loop.close()
