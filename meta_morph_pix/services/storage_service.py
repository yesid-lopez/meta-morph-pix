from b2sdk.v2.exception import FileNotPresent

from ..config import backblaze
from ..utils.blackblaze_client import get_b2_client


def upload_image(buffer, image_name) -> str:
    b2_client = get_b2_client()
    bucket = b2_client.get_bucket_by_name(backblaze.bucket_name)
    file_path = f"transformed/{image_name}"

    if check_file_exists(file_path):
        raise FileExistsError(f"Image {file_path} already exists")

    response = bucket.upload_bytes(buffer.getvalue(), file_path, content_type='image/jpeg')
    return response.file_name


def check_file_exists(file_name) -> bool:
    b2_client = get_b2_client()
    bucket = b2_client.get_bucket_by_name(backblaze.bucket_name)
    try:
        bucket.get_file_info_by_name(file_name)
        return True
    except FileNotPresent:
        return False
