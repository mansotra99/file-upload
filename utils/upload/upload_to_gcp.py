from google.cloud import storage
import datetime,os

CLIENT = storage.Client.from_service_account_json(os.getenv('GCP_SERVICE_JSON'))

def gcp_presigned_upload(path,image_name):
    bucket = CLIENT.bucket(os.getenv('BUCKET_NAME'))
    blob = bucket.blob(os.path.join(path+image_name)) # name of file to be saved/uploaded to storage

    presigned_url = blob.generate_signed_url(
        version="v4",
        expiration=datetime.timedelta(minutes=10080),# 10080 is 7 days in minutes max expiry presigned_upload provides
        method="PUT",
        content_type="application/octet-stream",
    )
    image_url=presigned_url.split('?')[0]
    result={
        "image_url":image_url,
        "presigned_url":presigned_url
    }
    return result