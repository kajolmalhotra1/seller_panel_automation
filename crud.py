import os
import sys
import model
from sqlalchemy.orm import Session
from datetime import datetime
from logs import Logger
import payout_pb2
import generaterules.grpcserver.static as static
from google.protobuf.json_format import MessageToDict

def get_slab_list(db: Session, request):
    try:
        slab_list = db.query(model.SlabList.id, model.SlabList.calculation_attribute,
                                  model.Slablist.slab_name, model.SlabList.description,
                                  model.SlabList.slab_start, model.SlabList.slab_end, model.SlabList.value_type, model.SlabList.created_by).filter(
            model.SlabList.tenant_id == request.tenant_id).all()
        all_slab_list = [

            seller_pb2.SlabList(id=i[0], fee_type=i[1], fees_name=i[2], rules_attributes=i[3],
                                     applicable_date=i[4], created_by=i[5]) for i in slab_list]
        return {
            "status_code": static.ResponseStatusCode.success, "status": static.ResponseStatus.success,
            "message": static.ResponseMessage.success, "data": all_slab_list
        }

    except Exception as e:
        db.rollback()
        exception_message = str(e)
        exception_type, exception_object, exception_traceback = sys.exc_info()
        filename = os.path.split(exception_traceback.tb_frame.f_code.co_filename)[1]
        Logs("Seller_Panel_GR_crud").error(
            f"{exception_message} {exception_type} {filename}, Line {exception_traceback.tb_lineno}")
        raise e

def create_slab_list(db: Session, request: seller_pb2.SlabList):
    try:
        slab_list = model.SlabList(
            fees_type=request.fees_type,
            fees_name=request.fees_name,
            rules_attributes=request.rules_attributes,
            applicable_date=datetime.strptime(request.applicable_date, '%Y-%m-%d %H:%M:%S'),
            created_by=request.created_by,
            tenant_id=request.tenant_id,
            Status=True
        )
        db.add(Slab_List)
        db.commit()
        return {"status_code": static.ResponseStatusCode.created, "status": static.ResponseStatus.success,
                "message": static.ResponseMessage.slablist_created}
    except Exception as e:
        db.rollback()
        exception_message = str(e)
        exception_type, exception_object, exception_traceback = sys.exc_info()
        filename = os.path.split(exception_traceback.tb_frame.f_code.co_filename)[1]
        Logger("seller_panel_GRS_crud").error(
            f"{exception_message} {exception_type} {filename}, Line {exception_traceback.tb_lineno}")
        raise e











