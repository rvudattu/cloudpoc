from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
import pandas as pd
import cx_Oracle
import json
import logging
# Create your views here.

import google.cloud.logging
client = google.cloud.logging.Client()
client.setup_logging()



@api_view(['POST'])
def count_cur_sim(request):
    try:
        '''
        conn = cx_Oracle.connect('Apps/apps@omsddb.cswg.com:1521/omsd_app', encoding="UTF-8")
        query = f"select count(*) from apps.OMS_ALC_CURR_SIM_RESULTS"
        df = pd.read_sql(query, conn)
        res = df.to_dict('records')
        conn.close()
        return JsonResponse({"status": "success", "data": res})
        '''
        # Added a comment to Main by Pgarikap user.
        # Added a comment to Main by rvudattu user.
        # Added a comment on 11-01-2023_14:43
        # Added a comment from uat on 11-01-2022_19:28
#         print('request', request.get_json())
#         request = request.data
        data = json.loads(request.body.decode("utf-8"))
        logging.info(f"request.........{data}")
        print('request', data)
        return JsonResponse({"status": "success", "data": data})

    except Exception as e:
        return JsonResponse({"status": "failed", "msg": str(e)})

@api_view(['GET'])
def getresponse(request):
    try:
        return JsonResponse({"status":"success", "msg": "success."})
    except Exception as e:
        return JsonResponse({"status": "failed", "msg": str(e)})

@api_view(['post'])
def testApi(request):
    try:
        # Added change from sub user on 22-12-2022.
        return JsonResponse({"status":"success", "msg": "code merge ."})
    except Exception as e:
        return JsonResponse({"status": "failed", "msg": str(e)})
