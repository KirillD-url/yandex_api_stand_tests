import configuration
import requests
import data
def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)
response1 = get_docs()
print("1----")
print(response1.status_code)
print(response1)

def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,params={"count":20})
response2 = get_logs()
print("2----")
print(response2.status_code)
print(response2.headers)

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
response3 = get_users_table()
print("3----")
print(response3)

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки
response4 = post_new_user(data.user_body);
print("4----")
print(response4.status_code)
print(response4.json())

def post_products_kits(body):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=body,# подставляем полный url
                         headers=data.headers)  # а здесь заголовки
response5 = post_products_kits(data.product_ids);
print("5-----")
print(response5.status_code)
print(response5.json())
