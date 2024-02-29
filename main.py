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


class sellerPayout(payout_pb2_grpc.seller_panelServicer):

    async def GetSlabList(self, request, context):
        db = get_db()
        result = crud.get_slab_list(db, request)
        return payout_pb2.SlabListResponse(status_code=result['status_code'], status=result['status'],
                                                      message=result['message'], data=result['data'])

    async def CreateSlabList(self, request, context):
        db=get_db()
        result=crud.create_slab_list(db,request)
        return payout_pb2.StatusResponse(status_code=result['status_code'], status=result['status'], message=result['message'])

    async def DeleteSlabList(self, request, context):
        db=get_db()
        result=crud.create_slab_list(db,request)
        return payout_pb2.StatusResponse(status_code=result['status_code'], status=result['status'], message=result['message'])

async def serve():
    server = grpc.aio.server()
    payout_pb2_grpc.add_seller_panelServicer_to_server(sellerPayout(), server)
    grpc_port = f"{os.getenv('SERVER')}:{int(os.getenv('GRPC_PORT'))}"
    server.add_insecure_port(grpc_port)
    await server.start()


    async def server_graceful_shutdown():
        print("gracefully shutting Down ")
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

