from flask import Blueprint, request
from google.cloud.storage import Client

from environment import PROJECT_ID, BUCKET_NAME

file_uploader_bp = Blueprint('file_uploader', __name__)


@file_uploader_bp.post('/upload')
def upload_file():
    uploaded_file = request.files['file']
    if not uploaded_file:
        return {"message": "No file uploaded!"}, 400

    storage_client = Client(project=PROJECT_ID)
    buckets = storage_client.bucket(BUCKET_NAME)
    blob = buckets.blob(uploaded_file.filename)
    blob.upload_from_string(uploaded_file.read(),
                            content_type=uploaded_file.content_type)

    return {"message": "File uploaded successfully!"}, 200
