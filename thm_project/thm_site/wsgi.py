# This file is part of JuliaBase-Institute

# For a proper configuration you need to add your projeckt and the
# juliabase package to the python path.
import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path.append("/home/linus/thm_project")
sys.path.append("/home/linus/thm_project/juliabase")

# When the WSGI server loads your projeckt, Django needs to import your
# settings module. So you have to add the settinge module to your server
# configuration or uncomment the following statement.
os.environ["DJANGO_SETTINGS_MODULE"] = "thm_site.settings"

application = get_wsgi_application()
