#------------------------------------#
#__DEVOLPER__ = ___MAHDI HASAN SHUVO___'
#__FACEBOOK__ = ___MAHDI HASAN [www.facebook.com/bk4human]'
#__DEVOLPER__ = ___MAHDI HASAN SHUVO___'
#__GitHub_____= ___Shuvo-BBHH___'
#___V___= 1
#------------------------------------#
# YOU Must RUN " pip install mahdixn " Beafore Run THIS FILE
import mahdix,re
logo=mahdix.mlog()
def fff():
    mahdix.clear()
    print(logo)
    print(f' {mahdix.LI_YELLOW}   Wellcome  To Auto Password Changer ')
    cok=input(f'{mahdix.LI_GREEN}Cookies :{mahdix.LI_WHITE} ')
    print(mahdix.mahdilinx())
    oldps=input(f'{mahdix.LI_YELLOW}INPUT Old pass :{mahdix.LI_GREEN} ')
    print(mahdix.mahdilinx())
    newpass=input(f'{mahdix.LI_YELLOW}INPUT New pass :{mahdix.LI_GREEN} ')
    mahdix.clear()
    # cokix=cok.replace(' ', '')
    # cokie = cokix+';';mahdix.flw(coki)
    # try:
    #     datr=cokie.split('datr=')[1].split(';')[0];fr=cokie.split('fr=')[1].split(';')[0];c_user=cokie.split('c_user=')[1].split(';')[0];xs=cokie.split('xs=')[1].split(';')[0];cokiee='datr='+datr+';'+'fr='+fr+';'+'c_user='+c_user+';'+'xs='+xs+';'
    # except:
    #     datr=cokie.split('datr=')[1].split(';')[0];c_user=cokie.split('c_user=')[1].split(';')[0];xs=cokie.split('xs=')[1].split(';')[0];cokiee='datr='+datr+';'+'c_user='+c_user+';'+'xs='+xs+';'
    coki=cok
    mahdix.fb_lang_cng(coki)
    mahdiid=coki.split('c_user=')[1]
    cid=mahdiid[0:15];mahdix.flw(coki)
    url="https://mbasic.facebook.com/settings/security/password"
    s=mahdix.requests.Session()
    s.headers.update({
    'Host': 'mbasic.facebook.com','method':'GET',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'sec-ch-ua': '"(Not(A:Brand";v="99"','sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"','path':'/security/2fac/setup/intro','sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': mahdix.W_ueragnt(),
    })
    r1=s.get(url,cookies={'cookie':coki}).text
    sp=mahdix.html(r1,"html.parser")
    shuvo_s1=mahdix.requests.Session()
    eav=re.search('eav=(.*?)"', str(sp)).group(1)
    shuvo_s1.headers.update({
        'authority': 'mbasic.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,id;q=0.8','cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded','origin': 'https://mbasic.facebook.com',
        'referer': f'https://mbasic.facebook.com/settings/security/password/?paipv=0&eav={eav}',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-full-version-list': '"Google Chrome";v="117.0.5897.4", "Not;A=Brand";v="8.0.0.0", "Chromium";v="117.0.5897.4"',
        'sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"','sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1','upgrade-insecure-requests': '1',
        'user-agent': mahdix.W_ueragnt(),
        'viewport-width': '475',
    })
    params = {
        'redirect_uri': f'/settings/security/?settings_tracking=unknown%3Asettings_2_0&eav={eav}&paipv=0',
        'paipv': '0',
        'eav': eav,
    }
    data = {
        'fb_dtsg': re.search('name="fb_dtsg" type="hidden" value="(.*?)"', str(sp)).group(1),
        'jazoest': re.search('name="jazoest" type="hidden" value="(.*?)"', str(sp)).group(1),
        'password_change_session_identifier':re.search('name="password_change_session_identifier" style="display:none" type="text" value="(.*?)"', str(sp)).group(1),
        'password_old': oldps,
        'password_new': newpass,
        'password_confirm': newpass,
        'save': 'Save changes',
    }
    cng_pass_response = shuvo_s1.post('https://mbasic.facebook.com/password/change/', params=params, cookies={'cookie':coki}, data=data).text
    cng_pass_response_html=mahdix.html(cng_pass_response,"html.parser")
    if 'Log out of other devices?' in cng_pass_response_html.text:
        print(mahdix.mahdilinx())
        print(f'{mahdix.LI_WHITE}Password ChangeDone')
        print(f'{mahdix.LI_CYAN}UID : {mahdix.LI_GREEN}{cid}')
        print(f'{mahdix.LI_CYAN}PS : {mahdix.LI_GREEN}{newpass}')
        print(mahdix.linex())
        open("/sdcard/pass_changer.txt","a").write(f'--------------------------\n{cid}|{newpass}\n')
    else:
        print(f'{mahdix.LI_RED} Wrong Password :{oldps}')

fff()
