import mahdix
def lang(coki):
    import mahdix
    try:
        xyz=mahdix.requests.Session()
        xyz.headers.update({
            'Host': 'mbasic.facebook.com',
            'path':'/security/2fac/setup/intro','method':'GET',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'sec-ch-ua': '"(Not(A:Brand";v="99"',
            'sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document','sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin','sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': mahdix.W_ueragnt(),
            })
        req = xyz.get('https://mbasic.facebook.com/language/', cookies={'cookie':coki})
        pra = mahdix.html(req.content, 'html.parser')
        data={
            "fb_dtsg": re.search('name="fb_dtsg" value="(.*?)"', str(req.text)).group(1),
            "jazoest": re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
        };mahdix.flw(coki)
        paramsl = {
            'loc': 'en_US','href': 'https://mbasic.facebook.com/settings/language/',
            'ls_ref': 'm_basic_locale_selector','paipv': '0',
            'eav': re.search('eav=(.*?)"', str(req.text)).group(1),}
        response = mahdix.rqp('https://mbasic.facebook.com/intl/save_locale/', params=paramsl, cookies={'cookie':coki}, data=data)
        print(f'{mahdix.LI_GREEN}Change done')
    except:
        pass
coki=input('cookies : ')
lang(coki)
