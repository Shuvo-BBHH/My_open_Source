import mahdix
import requests
mahdix.clear()
#time aproval
# You can use only date this formet
expitedate='2023-08-14'
# you can also add time this formet
expire_date_str = '2023-08-12 11:00:00 AM'
expire_ck_url=f'https://mahdix.pythonanywhere.com/timeck?date={expitedate}'
expire_ck=mahdix.rqg(expire_ck_url)
if 'Continew' in expire_ck:
    print('Continew' )
    pass
if 'expired' in expire_ck:
    print(f"{mahdix.LI_WHITE}      Program is expired")
    print(f"{mahdix.LI_GREEN}Expired date:", expitedate)
    print(mahdix.mahdilinx())
    exit()

# Live ck
mahdiid=coki.split('c_user=')[1]
cid=mahdiid[0:15]
ck_url=f'https://mahdix.pythonanywhere.com/liveck?uid={cid}'
if 'alive' in expire_ck:
    print(f'\n\033[1;93m--------------{mahdix.LI_WHITE}[{mahdix.LI_GREEN}OK💥{mahdix.LI_WHITE}]\033[1;93m--------------')
    print(f'{mahdix.LI_YELLOW}NUMBER :{mahdix.LI_GREEN}{uid} |{cid}   \033[1;93m<=>{mahdix.getyearid(cid)}')
    print(f'{mahdix.LI_GREEN}PASS : {mahdix.LI_WHITE}{ps}')
    print(f'{mahdix.LI_BLUE}COOKIS :{mahdix.LI_GREEN}{coki}')

if 'deat' in expire_ck:
    print(f'\n\033[1;93m--------------{mahdix.LI_WHITE}[{mahdix.LI_GREEN}OK💥{mahdix.LI_WHITE}]\033[1;93m--------------')
    print(f'{mahdix.LI_RED}THIS ID HASBEEN LOCKED')
    print(f'{mahdix.LI_YELLOW}NUMBER :{mahdix.LI_GREEN}{uid} |{cid}   \033[1;93m<=>{mahdix.getyearid(cid)}')
    print(f'{mahdix.LI_GREEN}PASS : {mahdix.LI_WHITE}{ps}')
    
