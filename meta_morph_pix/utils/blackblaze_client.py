from b2sdk.v2 import InMemoryAccountInfo, B2Api

from meta_morph_pix.config import backblaze


def get_b2_client():
    account_info = InMemoryAccountInfo()
    b2_api = B2Api(account_info)
    b2_api.authorize_account(
        "production",
        backblaze.application_key_id,
        backblaze.application_key
    )
    return b2_api
