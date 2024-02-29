from dotenv import load_dotenv
import os
import grpcserver.aio

import model
import payout_pb2
import payout_pb2_grpc
import crud
from database import SessionLocal
import asyncio
load_dotenv()

_cleanup_coroutines = []


def get_db():
    return SessionLocal()


db=get_db()
# a=model.MarketplaceFee(
# tenant_id='abc',
#     parameter=[{"id":1,"value":"Yes"},{"id":2,"value":"absolute"}]
# )
# # db.add(a)
# db.commit()
allfees=db.query(model.MarketplaceFee.calculation_attribute,model.MarketplaceFee.fee_name,model.MarketplaceFee.applicable_date,model.MarketplaceFee.description,model.MarketplaceFee.parameter).filter_by(tenant_id='IN0001').all()
print(allfees)

test=db.query(model.MarketplaceFeesCalcAttributes.attribute_value,model.MarketplaceFee.fee_name,model.MarketplaceFee.applicable_date,model.MarketplaceFee.description,model.MarketplaceFee.parameter).join(model.MarketplaceFeesCalcAttributes,model.MarketplaceFeesCalcAttributes.id==model.MarketplaceFee.calculation_attribute).filter(model.MarketplaceFee.tenant_id=='IN0001').all()
# print(test[0][4])
# test[4]
for i in test:
    print(i[4][0])
# def check_if_role_name_exists(db:Session, tenant_id: str, rolename: str):
#     """
#      Function to check if the rolename exists for particular tenantid
#     :param db: databse connection
#     :param tenant_id: tenant id for rolename
#     :param rolename: rolename
#     :return: True or False
#     """
#     return bool(db.query(model.WorkflowRoles).filter_by(tenant_id = tenant_id, rolename=rolename).scalar())
#
#
# def check_if_role_exists(db:Session, tenant_id: str, roleid: int):
#     """
#     Function to check if role exists for particular tenantid
#     :param db: databse connection
#     :param tenant_id: tenant id for roleid
#     :param roleid: roleid
#     :return: True or False
#     """
#     return bool(db.query(model.WorkflowRoles).filter_by(tenant_id = tenant_id, role_id=roleid).scalar())
#
#
# def check_if_user_exists(db: Session, tenantid: str, userid: int):
#     """
#     Function to check if user exists for particular tenantid
#     :param db: databse connection
#     :param tenantid: tenant id for userid
#     :param userid: userid
#     :return: True or False
#     """
#     return bool(db.query(model.Users).filter_by(tenant_id=tenantid, id=userid).scalar())


# def check_if_role_assigned_to_user_group(db: Session, tenant_id: str, role_id: int, user_group_id:int):
#     """
#     Function to check if role is assigned for user group for a particular tenant id
#     :param db: databse connection
#     :param tenant_id:
#     :param role_id: roleid
#     :param user_group_id: user group id
#     :return: True or False
#     """
#     x = bool(db.query(model.UserRoles).filter_by(tenant_id=tenant_id, role_id=role_id, group_id=user_group_id).first())
#     return x
#     # return bool(db.query(model.UserRoles).filter_by(tenant_id=tenant_id, role_id=role_id, group_id=user_group_id).first())


# def check_if_role_assigned(db: Session, tenant_id: str, role_id: int):
#     """
#      Function to check if role exists for particular tenant
#     :param db: databse connection
#     :param tenant_id: tenant id for role id
#     :param role_id: role id
#     :return: True or False
#     """
#     return bool(db.query(model.UserRoles).filter_by(tenant_id=tenant_id, role_id=role_id).first())
#
# def check_if_user_group_exists(db:Session, tenant_id:str, groupid: int):
#     """
#     Function to check if user group exists for particular tenantid
#     :param db: databse connection
#     :param tenant_id: tenant id for groupid
#     :param groupid: groupid
#     :return: True or False
#     """
#     return bool(db.query(model.Groups).filter_by(tenant_id=tenant_id, id=groupid).scalar())
#
#
# def check_if_role_assigned_to_user(db: Session, tenant_id: str, role_id: int, user_id: int):
#     """
#     Function to check if role is assigned to a user for a particular tenant id
#     :param db: databse connection
#     :param tenant_id: tenant id for roleid and userid
#     :param role_id: roleid
#     :param user_id: userid
#     :return: True or False
#     """
#     return bool(db.query(model.UserRoles).filter_by(tenant_id=tenant_id, role_id=role_id, user_id=user_id).first())
#
#
# def check_if_attribute_exists(db:Session, tenant_id: str, attribute_id:int):
#     """
#     Function to check if attribute exists for particular tenantid
#     :param db: databse connection
#     :param tenant_id: tenant id for attribute id
#     :param attribute_id: attribute id
#     :return: True or False
#     """
#     return bool(db.query(model.Attributes).filter_by(tenant_id=tenant_id,id=attribute_id).scalar())
#
# def check_if_attribute_assigned_to_user(db, tenant_id, user_id, attribute_id):
#     """
#     Function to check if attribute is assigned to a user for a particular tenantid
#     :param db: databse connection
#     :param tenant_id: Tenant id
#     :param user_id:
#     :param attribute_id:
#     :return: True or False
#     """
#     return bool(db.query(model.UserAttributes).filter_by(tenant_id=tenant_id, user_id=user_id, attribute_id=attribute_id).scalar())
#
# def check_if_attribute_group_exists(db:Session, tenant_id:str, attribute_group_id:int):
#     """
#     Function to check if attribute group exists for a particular tenant id
#     :param db: databse connection
#     :param tenant_id: Tenant id
#     :param attribute_group_id: attribute group id
#     :return: True or False
#     """
#     return bool(db.query(model.AttributeGroup).filter_by(tenant_id=tenant_id, id=attribute_group_id).scalar())
#
# def check_if_attribute_group_assigned_to_user(db, tenant_id, user_id, attribute_group_id):
#     """
#     Function to check if attribute group is assigned to a user for a particular tenantid
#     :param db: databse connection
#     :param tenant_id:
#     :param user_id:
#     :param attribute_group_id:
#     :return: True or False
#     """
#     return bool(db.query(model.UserAttributes).filter_by(tenant_id=tenant_id, user_id=user_id, attribute_group_id=attribute_group_id).scalar())
#
#
# def check_if_permission_assigned_to_role(db: Session, roleid: str, tenantid: str):
#     """
#     Function to check if
#     :param db: databse connection
#     :param roleid:
#     :param tenantid:
#     :return: True or False
#     """
#     return bool(db.query(model.RolePermissions).filter_by(role_id=roleid,tenant_id=tenantid).first())
#
# def is_permission_assigned_to_role(db, tenantid:str, roleid:int, module:str, submodule:str, action:str):
#     """
#     Function to check if
#     :param db: databse connection
#     :param tenantid:
#     :param roleid:
#     :param module:
#     :param submodule:
#     :param action:
#     :return: True or False
#     """
#     return bool(db.query(model.RolePermissions).join(model.Permissions, model.Permissions.permission_id ==
#                                                                model.RolePermissions.permissions).join(model.Actions, model.Actions.action_id == model.Permissions.action).filter(model.RolePermissions.tenant_id==tenantid,model.RolePermissions.role_id==roleid,
#                                                                                                                                                                                   model.Permissions.module == module,
#                                                                                                                                                                                   model.Permissions.submodule == submodule,
#                                                                                                                                                       model.Actions.action_name == action).scalar())
#
# def check_if_category_exists(db: Session, tenant_id: str, category_id: int):
#     """
#     Function to check if category exists for particular tenantid
#     :param db: databse connection
#     :param tenant_id:
#     :param category_id:
#     :return: True or False
#     """
#     return bool(db.query(model.Categories).filter_by(tenant_id=tenant_id, id=category_id).scalar())
#
#
# def check_if_category_assigned_to_user(db, tenant_id, user_id, category_id):
#     """
#     Function to check if
#     :param db: databse connection
#     :param tenant_id:
#     :param user_id:
#     :param category_id:
#     :return: True or False
#     """
#     return bool(db.query(model.UserCategories).filter_by(tenant_id=tenant_id, user_id=user_id, category_id=category_id).scalar())
#
# def check_if_role_in_any_workflow(db, tenant_id, role_id):
#     """
#     Function to check if
#     :param db: databse connection
#     :param tenant_id: tenant id for role id
#     :param role_id: role id
#     :return: True or False
#     """
#     return bool(db.query(model.Workflow).filter_by(tenant_id=tenant_id, role_id=role_id).first())
#
# def check_if_workflow_exists(db, category_id, tenant_id):
#     """
#     Function to check if workflow is assigned to a category for a particular tenant id
#     :param db: databse connection
#     :param category_id:
#     :param tenant_id:
#     :return: True or False
#     """
#     return bool(db.query(model.Workflow).filter_by(tenant_id=tenant_id, category_id=category_id).first())
#
# def check_if_sku_category_attribute_group_exists(db, tenant_id, sku, category_id, attribute_group_id):
#     """
#     Function to check if
#     :param db: databse connection
#     :param tenant_id:
#     :param sku:
#     :param category_id:
#     :param attribute_group_id:
#     :return: True or False
#     """
#     return bool(db.query(model.Dataflow).filter_by(tenant_id = tenant_id, sku_id=sku, category_id=category_id, attribute_group_id=attribute_group_id).scalar())
#
#
# def check_if_sku_category_attribute_exists(db, tenant_id, sku, category_id, attribute_id):
#     """
#     Function to check if
#     :param db: databse connection
#     :param tenant_id:
#     :param sku:
#     :param category_id:
#     :param attribute_id:
#     :return: True or False
#     """
#     return bool(db.query(model.Dataflow).filter_by(tenant_id = tenant_id, sku_id=sku, category_id=category_id, attribute_id=attribute_id).scalar())
#
#
# def check_if_sku_in_last_stage(db, sku):
#     """
#     Function to check if the SKU is in last stage of workflow
#     :param db: databse connection
#     :param sku: SKU
#     :return: True or False
#     """
#     return (db.query(model.Workflow.last_stage).filter(model.Workflow.tenant_id == sku.tenant_id, model.Workflow.category_id == sku.category_id, model.Workflow.depth == sku.workflow_stage).first())[0]



