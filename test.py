from keystoneauth1 import loading
from keystoneauth1 import session
from novaclient import client
loader = loading.get_plugin_loader('password')
auth = loader.load_from_options(auth_url=AUTH_URL,
                                username=USERNAME,
                                password=PASSWORD,
                                project_id=PROJECT_ID)
sess = session.Session(auth=auth)
nova = client.Client(VERSION, session=sess)
