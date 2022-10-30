from oneM2M_functions import *

uri_cse = "http://127.0.0.1:8080/~/in-cse/in-name"

ae1 = "LED1"
cnt1 = "node1"
ae2 = "LED2"
cnt2 = "node2"

create_ae(uri_cse, ae1)
uri_ae_1 = uri_cse + "/" + ae1
create_cnt(uri_ae_1, cnt1)
uri_cnt_1 = uri_ae_1 + "/" + cnt1

create_ae(uri_cse, ae2)
uri_ae_2 = uri_cse + "/" + ae2
create_cnt(uri_ae_2, cnt2)
uri_cnt_2 = uri_ae_2 + "/" + cnt2

delete(uri_ae_1)
delete(uri_ae_2)

headers = {
'X-M2M-Origin': 'admin:admin',
'Content-type': 'application/json'
}