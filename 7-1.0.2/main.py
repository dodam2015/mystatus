print('made by L.Doyun')
try:
    import time,sys,os,random,pygame
except Exception as error:
    print(f'error:{error}')
version='1.0.2'
try:
    pygame.mixer.init()
    script_dir=os.path.dirname(os.path.abspath(__file__))
    file_path=os.path.join(script_dir,'01000011 00110100 00110001 00111000.wav')
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(-1)
except Exception as e:
    print(f'error:{e}')
    pass
print('loaded')

riteml=['stone','copper_piece','coal_piece','iron_piece','gold_piece','diamond_piece']
item={'stone':0,'copper_piece':0,'coal_piece':0,'iron_piece':0,'gold_piece':0,'diamond_piece':0}
item_money={'stone':25,'copper_piece':50,'coal_piece':75,'iron_piece':100,'gold_piece':200,'diamond_piece':500}

time.sleep(2)

main_cmd=0
while True:
    print('                 M   Y   S   T   A   T   U   S                   ')
    print(f'version:{version}')
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
        print('1.sound')
        try:
            setings_cmd=input(':')
            setings_cmd=int(setings_cmd)
        except Exception:
            print('please enter correct number')
            pass
        if setings_cmd==1:
            print('1.stop')
            try:
                abc=input(':')
                abc=int(abc)
            except Exception:
                print('please enter correct number')
                pass
            if abc==1:
                pygame.mixer.music.stop()
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
    print('5.go to the ')
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
                if item[store_cmd]==0:
                    print(f"you don't have {store_cmd}.")
                    pass
                elif not(item[store_cmd]==0):
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
                if item['stone']==0:
                    time.sleep(7)
                    pass
                else:
                    time.sleep(1)
                rand=random.randrange(0,100)
                #i#f rand<0:
                    #print('air')
                try:
                    if rand<30:
                        print('copper piece breaked!')
                        item['copper_piece']+=1
                    elif rand<50:
                        print('stone breaked.')
                        item['stone']+=1
                    elif rand<70:
                        print('coal piece breaked!!')
                        item['coal_piece']+=1
                    elif rand<85:
                        print('iron piece breaked!!!')
                        item['iron_piece']+=1
                    elif  rand<90:
                        print('gold piece breaked!!!!')
                        item['gold_piece']+=1
                    elif rand==99:
                        print('diamond piece breaked⭐⭐⭐⭐⭐')
                        item['diamond_piece']+=1
                    else:
                        print('stone breaked.')
                        item['stone']+=1
                except Exception:
                    print('key error')

            elif mine_cmd==2:
                break
