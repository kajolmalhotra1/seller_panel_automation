import datetime
from fastapi import Body
from typing import Optional, List, Union
from pydantic import BaseModel,StrictStr

class Statusmessage(BaseModel):
    status_code: int
    status: StrictStr
    message: StrictStr

class FlatFeeRequest(BaseModel):
    fee_name:StrictStr
    description:StrictStr
    applicable_date:StrictStr
    value_type:StrictStr
    value:StrictStr
    created_by:StrictStr
    tenant_id:StrictStr

class FlatFee(BaseModel):
    id:int
    fee_name=StrictStr
    description:StrictStr
    application_date:datetime.datetime
    value_type:StrictStr
    value:StrictStr

class FlatFeeResponse(BaseModel):
    status_code: int
    status: StrictStr
    message: StrictStr
    data:List[FlatFee]

class Tenant_id(BaseModel):
    tenant_id:StrictStr


class AttributesValue(BaseModel):
    id:int
    attribute_value:StrictStr
class CalculationAttributesResponse(BaseModel):
    status_code: int
    status: StrictStr
    message: StrictStr
    data: List[AttributesValue]



class ParameterValue(BaseModel):
    id:int
    value:StrictStr

class ParameterValueData(BaseModel):
    id:int
    Parameter_name:StrictStr
    Parameter_type:StrictStr
    Parameter_value:List[ParameterValue]
class ParameterValueResponse(BaseModel):
    status_code: int
    status: StrictStr
    message: StrictStr
    data: List[AttributesValue]


class DeleteRequest(BaseModel):
    tenant_id:StrictStr
    id:int


class ParameterValueMarketPlace(BaseModel):
    param_id:int
    param_value:StrictStr
class MarketPlaceData(BaseModel):
    id:int
    calculation_attribute:StrictStr
    fee_name:StrictStr
    applicable_date:StrictStr
    description:StrictStr
    parameter_value=List[ParameterValueMarketPlace]
class MarketPlaceFeeResponse(BaseModel):
    status_code: int
    status: StrictStr
    message: StrictStr
    data: List[MarketPlaceData]


class Columns(BaseModel):
    id:int
    Parameter_name:StrictStr

class ColumnsResponse(BaseModel):
    status_code: int
    status: StrictStr
    message: StrictStr
    data: List[Columns]

class Parameter(BaseModel):
    param_id:int
    param_value:StrictStr
class MarketPlaceFeesReuest(BaseModel):
    tenant_id:StrictStr
    calculation_attribute:int
    fee_name:StrictStr
    applicable_date:StrictStr
    description:StrictStr
    created_by:StrictStr
    parameter_value:List[Parameter]

class PromotionRequest(BaseModel):
    tenant_id:StrictStr
    promotion_name:StrictStr
    start_date:StrictStr
    end_date:StrictStr
    value_type:StrictStr
    value:int
    created_by:StrictStr


