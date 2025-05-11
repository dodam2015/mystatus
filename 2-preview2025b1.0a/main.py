print('made by L.Doyun')
try:
    import time,sys,os
except Exception as error:
    print(f'error:{error}')

print('loaded')

time.sleep(2)

main_cmd=0
while True:
    print('mystatus')
    print("made by L.Doyun. Don't reupload!")
    print('1.singlplay.')
    print('2.setings.')
    print('3.exit.')
    try:
        main_cmd=input(':')
        main_cmd=int(main_cmd)
    except Exception:
        print(f'enter correct number.')
        pass
    if main_cmd==1:
        break
    elif main_cmd==2:
        setings_cmd=0
    elif main_cmd==3:
        sys.exit()

level=0
money=0
print('status reseted!')

cmd=''
while True:
    print('1.see your status.')
    print('2.go to the store.')
    print('3.exit.')
    try:
        cmd=input(':')
        cmd=int(cmd)
    except Exception:
        print(f'enter correct number.')
        pass
    if cmd==1:
        print(f'level:{level}')
        print(f'money:{money}')
    elif cmd==2:
        print('store.')
    elif cmd==3:
        sys.exit()

