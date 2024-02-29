import os
import sys
from datetime import datetime
import model
import static
import seller_pb2
from sqlalchemy.orm import Session
from logger.logs import Logger


def get_generate_rules(db: Session, request):
    try:
        generate_rules = db.query(model.GenerateRules.id, model.GenerateRules.fees_type,
                                  model.GenerateRules.fees_name, model.GenerateRules.rules_attributes,
                                  model.GenerateRules.applicable_date, model.GenerateRules.created_by).filter(
            model.GenerateRules.tenant_id == request.tenant_id).all()
        all_generate_rule = [

            seller_pb2.GenerateRules(id=i[0], fee_type=i[1], fees_name=i[2], rules_attributes=i[3],
                                     applicable_date=i[4], created_by=i[5]) for i in generate_rules]
        return {
            "status_code": static.ResponseStatusCode.success, "status": static.ResponseStatus.success,
            "message": static.ResponseMessage.success, "data": all_generate_rules
        }

    except Exception as e:
        db.rollback()
        exception_message = str(e)
        exception_type, exception_object, exception_traceback = sys.exc_info()
        filename = os.path.split(exception_traceback.tb_frame.f_code.co_filename)[1]
        Logger("Seller_Panel_GR_crud").error(
            f"{exception_message} {exception_type} {filename}, Line {exception_traceback.tb_lineno}")
        raise e


def create_generate_rules(db: Session, request: seller_pb2.GenerateRules):
    try:
        generate_rules = model.GenerateRules(
            fees_type=request.fees_type,
            fees_name=request.fees_name,
            rules_attributes=request.rules_attributes,
            applicable_date=datetime.strptime(request.applicable_date, '%Y-%m-%d %H:%M:%S'),
            created_by=request.created_by,
            tenant_id=request.tenant_id,
            Status=True
        )
        db.add(generate_rules)
        db.commit()
        return {"status_code": static.ResponseStatusCode.created, "status": static.ResponseStatus.success,
                "message": static.ResponseMessage.generaterules_created}
    except Exception as e:
        db.rollback()
        exception_message = str(e)
        exception_type, exception_object, exception_traceback = sys.exc_info()
        filename = os.path.split(exception_traceback.tb_frame.f_code.co_filename)[1]
        Logger("seller_panel_GRS_crud").error(
            f"{exception_message} {exception_type} {filename}, Line {exception_traceback.tb_lineno}")
        raise e
