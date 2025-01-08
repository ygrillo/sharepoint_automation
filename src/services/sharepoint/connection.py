from dataclasses import dataclass
from office365.sharepoint.client_context import ClientContext
from config import SHAREPOINT_URL, USER_CREDENTIAL, USER_PASSWORD


@dataclass
class SharePoint:
    @staticmethod
    def connect_to_service():
        # ctx = ClientContext(test_site_url).with_client_credentials(
        # test_client_id, test_client_secret
        # )
        # target_web = ctx.web.get().execute_query()
        # print(target_web.url)
        ctx = ClientContext(SHAREPOINT_URL).with_user_credentials(USER_CREDENTIAL, USER_PASSWORD)
        web = ctx.web.get().execute_query()
        print(web.url)
