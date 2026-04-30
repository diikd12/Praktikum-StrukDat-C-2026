from colorama import Fore, Back, Style, init
init()

print (Fore.RED + "Teks Merah")
print (Fore.GREEN + "Teks Hijau")
print (Fore.BLUE + Back.YELLOW + "Teks Merah, Background Kuning")
print (Style.RESET_ALL + "Kembali Normal")