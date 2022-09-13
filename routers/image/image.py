from fastapi import APIRouter, Form,Request
from typing import Optional
import uuid
from enum import Enum

from utils.response_manipulator import CustomResponse
from utils.exception import Exception
from utils.upload.upload_to_gcp import gcp_presigned_upload

from db.image.image_engine import * 

from routers.image.image_service import * 

imageRoute = APIRouter()

@imageRoute.post('/generate-presigned', description="Api to generate a Presigned_url provided certain image_name to generate its presigned_url")
def presigned(request: Request,image_name: str=Form(...),update: Optional[bool]=Form(False),image_id: Optional[str]=Form("")):
    try:

        if update:
            update_result=update_image(request,image_id=image_id)
            if not update_result.get('status'):
                data={
                    'image_id':image_id
                }
                return CustomResponse(request=request,status_code=400, data=data,message=update_result.get('message') ).customResp()
            else:
                image_name=update_result.get('data').get('image_name')

        image_id=str(uuid.uuid4())
        presigned_result=gcp_presigned_upload("images/cat/",image_name)
        data={
            "presigned_url":presigned_result.get('presigned_url'),
            "image_url":presigned_result.get('image_url'),
            "image_id":image_id
        }
        insert_url_to_upload(request,image_name=image_name,image_url=presigned_result.get('image_url'),image_id=image_id)
        
        return CustomResponse(request=request,status_code=200, data=data,message="Success" ).customResp()

                
    except:
        raise Exception().raise_exception(request_id=request.state.request_token)


@imageRoute.put('/update-status',description="Api to Change status of a particular image")
def status(request: Request,image_id: str=Form(...),status: Optional[Statuses]=Form(Statuses.uploaded)):
    try:
        change_image_status(request,image_id=image_id,status=status)
        return CustomResponse(request=request,status_code=200,message=status ).customResp()
    except:
        raise Exception().raise_exception(request_id=request.state.request_token)

@imageRoute.get("/{image_id}/data" ,description="Api to get data of a particular image")
def image_data(request: Request,image_id):
    try:
        image_result=get_image(request,image_id=image_id)
        if image_result.status:
            data=image_result.data
            return CustomResponse(request=request,data=data,status_code=200,message="Success" ).customResp()
        else:
            return CustomResponse(request=request,status_code=404,message="Not Found" ).customResp()
    except:
        raise Exception().raise_exception(request_id=request.state.request_token)


@imageRoute.get("/list",description="Api to get data of all the images")
def image_list(request: Request, page_no: int=0 ,limit_per_page:int = 10):
    try:
        image_result=get_image_list(request,page_no=page_no,limit_per_page=limit_per_page)
        if image_result.status:
            data={
                "image_list":image_result.data
            }
            return CustomResponse(request=request,data=data,status_code=200,message="Success" ).customResp()
        else:
            return CustomResponse(request=request,status_code=404,message="Not Found" ).customResp()
    except:
        raise Exception().raise_exception(request_id=request.state.request_token)
