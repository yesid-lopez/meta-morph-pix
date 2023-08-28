from ..config import backblaze
from ..utils.blackblaze_client import get_b2_client


def upload_image(buffer, image_name):
    b2_client = get_b2_client()
    bucket = b2_client.get_bucket_by_name(backblaze.bucket_name)
    response = bucket.upload_bytes(buffer.getvalue(), f"transformed/{image_name}", content_type='image/jpeg')
    print(b2_client.get_file_info(response.id_))
