import time
import menus ,client,admin
username={'admin':'admin'}
print("""
           █ █ █ █▀▀ █   █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█
           ▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █ ▀ █ ██▄    █  █▄█

 $$$$$$\  $$$$$$$\   $$$$$$\        $$$$$$$\   $$$$$$\  $$\   $$\ $$\   $$\ 
$$  __$$\ $$  __$$\ $$  __$$\       $$  __$$\ $$  __$$\ $$$\  $$ |$$ | $$  |
$$ /  $$ |$$ |  $$ |$$ /  \__|      $$ |  $$ |$$ /  $$ |$$$$\ $$ |$$ |$$  / 
$$$$$$$$ |$$$$$$$\ |$$ |            $$$$$$$\ |$$$$$$$$ |$$ $$\$$ |$$$$$  /  
$$  __$$ |$$  __$$\ $$ |            $$  __$$\ $$  __$$ |$$ \$$$$ |$$  $$<   
$$ |  $$ |$$ |  $$ |$$ |  $$\       $$ |  $$ |$$ |  $$ |$$ |\$$$ |$$ |\$$\  
$$ |  $$ |$$$$$$$  |\$$$$$$  |      $$$$$$$  |$$ |  $$ |$$ | \$$ |$$ | \$$\ 
\__|  \__|\_______/  \______/       \_______/ \__|  \__|\__|  \__|\__|  \__|
""")
loading = "[████████████████████████████████████████████████████████████████]"
print('Loading : ',end=' ')
for i in loading:
    print(i,end='')
    time.sleep(0.02)
print('100%')
menus.main_menu()