import boto3
from utils import ExecutionEngine


# A lambda function to interact with AWS RDS MySQL
def lambda_handler(event, context):
    try:
        print('event:', event)
        engine = ExecutionEngine.from_region(secret_name="prod/mysql", region_name=boto3.session.Session().region_name)

        client_id = event['query']['client_id']
        sql = """
        SELECT Description, Location, Archive_Email, IT_Email, Logistics_Email, Support_Email, 
            Units, IT_Contact, Logistics_Contact, Support_Contact, Alerts_On, HR_Alerts_On, SBP_Alerts_On,
            DBP_Alerts_On, RR_Alerts_On, SPO2_Alerts_On, CI_Alerts_On, CO_Alerts_On, SV_Alerts_On, SVR_Alerts_On,
            Interval_Auto_Change, Organization_Interval, Organization_Default_Interval
        FROM Clients WHERE Clients = {client_id} 
         """
        params = {
            "client_id": client_id
        }
        result = engine.read_value(sql, params)
        print(result)
        result.Alerts_On = int(result.Alerts_On)
        result.HR_Alerts_On = int(result.HR_Alerts_On)
        result.SBP_Alerts_On = int(result.SBP_Alerts_On)
        result.DBP_Alerts_On = int(result.DBP_Alerts_On)
        result.RR_Alerts_On = int(result.RR_Alerts_On)
        result.SPO2_Alerts_On = int(result.SPO2_Alerts_On)
        result.CI_Alerts_On = int(result.CI_Alerts_On)
        result.CO_Alerts_On = int(result.CO_Alerts_On)
        result.SV_Alerts_On = int(result.SV_Alerts_On)
        result.SVR_Alerts_On = int(result.SVR_Alerts_On)
        result.Interval_Auto_Change = int(result.Interval_Auto_Change)
        result.Organization_Interval = int(result.Organization_Interval)
        result.Organization_Default_Interval = int(result.Organization_Default_Interval)
        #result.Alerts_On = int(result.Alerts_On)
        #print(result.to_dict())
        return result.to_dict()
    except Exception as e:
        raise e
    finally:
        engine.close_conn()
