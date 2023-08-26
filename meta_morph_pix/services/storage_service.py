from ..utils.blackblaze_client import get_b2_client
from ..config import backblaze


def upload_image(buffer, image_name):
    b2_client = get_b2_client()
    bucket = b2_client.get_bucket_by_name(backblaze.bucket_name)
    bucket.upload_bytes(buffer.getvalue(), "transformed/", content_type='image/jpeg')
