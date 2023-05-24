from employee.views import Empviewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register('employe',Empviewset)

