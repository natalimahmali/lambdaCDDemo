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
        return result.to_dict()
    except Exception as e:
        raise e
    finally:
        engine.close_conn()
