username = 'admin'
password = 'bkcloud'
tenant_name = 'admin'
auth_url = 'http://bkcloud12:35357/v3'

from keystoneauth1.identity import v3
from keystoneauth1 import session

auth = v3.Password(auth_url=auth_url,
		    		user_domain_name='default',
                    username=username,
                    password=password,
		    		project_domain_name='default',
                    project_name=tenant_name)

sess = session.Session(auth=auth)
