from dataclasses import dataclass
from office365.sharepoint.client_context import ClientContext
from config import SHAREPOINT_URL, USER_CREDENTIAL, USER_PASSWORD


@dataclass
class SharePoint:
    @staticmethod
    def connect_to_service():
        # site_url = SHAREPOINT_URL
        # ctx = ClientContext(site_url).with_credentials(UserCredential(USER_CREDENTIAL, USER_PASSWORD))
        # web = ctx.web
        # ctx.load(web)
        # ctx.execute_query()
        # print("Web title: {0}".format(web.properties['Title']))
        ctx = ClientContext(SHAREPOINT_URL).with_user_credentials(USER_CREDENTIAL, USER_PASSWORD)
        web = ctx.web.get().execute_query()
        print(web.url)
