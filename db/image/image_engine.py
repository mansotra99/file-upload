from db.engine import DbExecute




def insert_url_to_upload(request,*args,**kwargs):
    query=  ''' INSERT INTO images(image_id,image_name, image_url)VALUES(:image_id,:image_name,:image_url);'''
    value_list={
        "image_id":kwargs.get('image_id'),
        "image_name":kwargs.get('image_name'),
        "image_url":kwargs.get('image_url')
    }
    result=DbExecute().insert(query,value_list)


def change_image_status(request,*args,**kwargs):
    query=''' update images set status=:status,is_hidden=:is_hidden where image_id=:image_id '''
    value_list={
        "status":kwargs.get('status'),
        "image_id":kwargs.get('image_id'),
        "is_hidden":1 if (kwargs.get('status') in ['replaced','deleted']) else 0
    }
    result=DbExecute().update(query,value_list)

def get_image(request,*args,**kwargs):
    query=''' select image_id,image_name,image_url,created_on from images where image_id = :image_id and is_hidden=0 ; '''
    value_list={
        "image_id":kwargs.get('image_id'),
    }
    result=DbExecute().fetchone(query,value_list)
    return result

def get_image_list(request,*args,**kwargs):
    query=''' select image_id,image_name,image_url,created_on from images where is_hidden=0 LIMIT :limit  OFFSET :offset ; '''
    value_list={
        "offset":kwargs.get('page_no'),
        "limit":kwargs.get('limit_per_page')
    }
    result=DbExecute().fetchall(query,value_list)
    return result