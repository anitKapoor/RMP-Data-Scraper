import RMPClass
import pandas as pd
import logging

instructor = "Bailey, Michael"
aapi = RMPClass.RateMyProfAPI(teacher=instructor)
aapi.retrieveRMPInfo()
print(aapi.getRMPInfo())
