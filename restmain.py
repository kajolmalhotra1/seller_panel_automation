from dotenv import load_dotenv
import json
import sys
import os
sys.path.append(os.getcwd())
from google.protobuf import json_format
import grpc
from google.protobuf.json_format import MessageToDict
import payout_pb2 as payout_pb2
import payout_pb2_grpc as payout_pb2_grpc
import schema
import uvicorn
from fastapi import FastAPI
load_dotenv()

grpc_port = f"{os.getenv('SERVER')}:{int(os.getenv('GRPC_PORT'))}"
channel=grpc.insecure_channel(grpc_port)
client= payout_pb2_grpc.PayoutStub(channel)

app = FastAPI()

@app.post('/createflatfees',response_model=schema.Statusmessage)
async def create_flat_fees(flatfee:schema.FlatFeeRequest):
    request=payout_pb2.FlatFeesRequest()
    request=json_format.ParseDict(flatfee.dict(),request)
    response=client.CreateFlatFees(request)
    result=MessageToDict(response,including_default_value_fields=True,preserving_proto_field_name=True)
    return result

@app.post('/getflatfees',response_model=schema.FlatFeeResponse)
async def get_flat_fees(tenant_id:schema.Tenant_id):
    request=payout_pb2.TenantId()
    request=json_format.ParseDict(tenant_id.dict(),request)
    response=client.GetFlatFees(request)
    result=MessageToDict(response,including_default_value_fields=True,preserving_proto_field_name=True)
    return result

@app.post('/getcalculationattributes',response_model=schema.CalculationAttributesResponse)
async def get_calculation_attributes(tenant_id:schema.Tenant_id):
    request = payout_pb2.TenantId()
    request = json_format.ParseDict(tenant_id.dict(), request)
    response = client.GetCalculationAttributes(request)
    result = MessageToDict(response, including_default_value_fields=True, preserving_proto_field_name=True)
    return result


@app.post('getparametervalue',response_model=schema.ParameterValueResponse)
async def get_parameter_value(tenant_id:schema.Tenant_id):
    request = payout_pb2.TenantId()
    request = json_format.ParseDict(tenant_id.dict(), request)
    response = client.GetParameterValue(request)
    result = MessageToDict(response, including_default_value_fields=True, preserving_proto_field_name=True)
    return result


@app.post('deleteflatfees',response_model=schema.Statusmessage)
async def delete_flat_fees(deleteflatfee:schema.DeleteRequest):
    request = payout_pb2.DeleteFlatFeeRequest()
    request = json_format.ParseDict(deleteflatfee.dict(), request)
    response = client.DeleteFlatFees(request)
    result = MessageToDict(response, including_default_value_fields=True, preserving_proto_field_name=True)
    return result


@app.post('/getmarketplacefees',response_model=schema.MarketPlaceFeeResponse)
async def get_marketplace_fees(marketplacefee:schema.Tenant_id):
    request = payout_pb2.TenantId()
    request = json_format.ParseDict(marketplacefee.dict(), request)
    response = client.GetMarketPlaceFees(request)
    result = MessageToDict(response, including_default_value_fields=True, preserving_proto_field_name=True)
    return result


@app.post('/getcolumnsformarketplacefees',response_model=schema.ColumnsResponse)
async def get_column(column:schema.Tenant_id):
    request = payout_pb2.TenantId()
    request = json_format.ParseDict(column.dict(), request)
    response = client.GetMarketPlaceFees(request)
    result = MessageToDict(response, including_default_value_fields=True, preserving_proto_field_name=True)
    return result

@app.post('/createmarketplacefees',response_model=schema.Statusmessage)
async def create_marketplace_fees(marketplacefees:schema.MarketPlaceFeesReuest):
    request = payout_pb2.MarketPlaceFeeRequest()
    request = json_format.ParseDict(marketplacefees.dict(), request)
    response = client.GetMarketPlaceFees(request)
    result = MessageToDict(response, including_default_value_fields=True, preserving_proto_field_name=True)
    return result

@app.post('/deletemarketplacefees',response_model=schema.Statusmessage)
async def delete_marketplace_fees(deletefees:schema.DeleteRequest):
    request = payout_pb2.DeleteFlatFeeRequest()
    request = json_format.ParseDict(deletefees.dict(), request)
    response = client.GetMarketPlaceFees(request)
    result = MessageToDict(response, including_default_value_fields=True, preserving_proto_field_name=True)
    return result


@app.post('createpromotion',response_model=schema.Statusmessage)
async def create_promotion(createpromotion:schema.PromotionRequest):
    request = payout_pb2.PromotionsRequest()
    request = json_format.ParseDict(createpromotion.dict(), request)
    response = client.GetMarketPlaceFees(request)
    result = MessageToDict(response, including_default_value_fields=True, preserving_proto_field_name=True)
    return result






if __name__=="__main__":
    uvicorn.run(app,host=os.getenv("SERVER"),port=int(os.getenv("RESTPORT")))