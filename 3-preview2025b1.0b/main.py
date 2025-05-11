print('made by L.Doyun')
try:
    import time,sys,os
except Exception as error:
    print(f'error:{error}')

print('loaded')

riteml=['stone']
item={'stone':0}
item_money={'stone':50}

time.sleep(2)

main_cmd=0
while True:
    print('                 M  Y  S  T  A  T  U  S                   ')
    print("made by L.Doyun. Don't reupload!")
    print('1.singlplay.')
    print('2.setings.')
    print('3.exit.')
    try:
        main_cmd=input(':')
        main_cmd=int(main_cmd)
    except Exception:
        print(f'enter correct number.')
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
    print('1.exit.')
    print('2.see your status.')
    print('3.go to the store.')
    print('4.go to the mine.')
    try:
        cmd=input(':')
        cmd=int(cmd)
    except Exception:
        print(f'enter correct number.')
        pass
    if cmd==1:
        sys.exit()
    elif cmd==2:
        print(f'level:{level}')
        print(f'money:{money}')
        print(f'your item:{item}')
    elif cmd==3:
        store_main_cmd=0
        print('1.sell')
        print('2.exit')
        try:
            store_main_cmd=input(':')
            store_main_cmd=int(store_main_cmd)
        except Exception:
            print('enter correct number.')
            pass
        if store_main_cmd==1:
            print(f'your item:{item}')
            print('Enter the name of the item to sell.')
            try:
                store_cmd=input(':')
            except Exception:
                print('enter correct item name.')
                pass
            if store_cmd in riteml:
                print(f'this item price is {item_money[store_cmd]}')
                print(f'do you want to sell {store_cmd}?(y or n)')
                store_yorn=input(':')
                if store_yorn=='y':
                    item[store_cmd]-=1
                    money+=item_money[store_cmd]
                    level+=0.1
                    print(f'your item({store_cmd})is selled.')
                    pass
                elif store_yorn=='n':
                    pass
        elif store_main_cmd==2:
            break
    elif cmd==4:
        mine_cmd=0
        while True:
            print('Here is mine.')
            print('1.break stone.')
            print('2.exit.')
            try:
                mine_cmd=input(':')
                mine_cmd=int(mine_cmd)
            except Exception:
                print(f'enter correct number.')
                pass
            if mine_cmd==1:
                print('breaking...')
                time.sleep(2)
                print('breaked.')
                item['stone']+=1
            elif mine_cmd==2:
                break