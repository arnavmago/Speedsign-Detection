from oneM2M_functions import *

uri_cse = "http://127.0.0.1:8080/~/in-cse/in-name"

ae = f"t_ae"
cnt = f"t_cnt"

uri_ae = uri_cse + "/" + ae
create_ae(uri_cse, ae)

uri_cnt = uri_ae + "/" + cnt
create_cnt(uri_ae, cnt)

def push(speed, coords):
    create_data_cin(uri_cnt, f"{coords}-{speed}")

def pull():
    uri_cnt = uri_ae + "/" + cnt

    uri_cnt += "/?rcn=4" #  will give for all content instances under cnt_1

    headers = {
    'X-M2M-Origin': 'admin:admin',
    'Content-type': 'application/json'
    }

