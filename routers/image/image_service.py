from email.mime import image
from enum import Enum

from db.image.image_engine import *

class Statuses(str, Enum):
    uploaded = "uploaded"
    deleted = "deleted"



def update_image(request,*args,**kwargs):
    resp={
        "status":False,
        
    }
    image_id=kwargs.get('image_id')
    if not image_id:
        resp['message']="Bad Request (image_id required for update)"
        return resp
    
    image_result=get_image(request,image_id=image_id)
    if image_result.status:
        change_image_status(request,image_id=image_id,status='replaced')
        resp['data']=image_result.data
        resp['status']=True
        return resp
    else:
        resp['message']="Image_id does not exists"
        return resp
    pass