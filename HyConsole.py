#!/usr/bin/python3
import requests, sys, time, psutil, os
import pytermgui as gui
from pytermgui import WindowManager, Window
# The program will be used in order to gather data on players from the Hypixel server via the command line
# The program has 0 affiliation by Hypixel

#Detecting if program has been ran via py.exe (possibly indicating that it was ran from cmd prompt)
#Or if it was ran via Python IDLE (Which would cause a load ton of errors)
ppid = os.getppid()
if psutil.Process(ppid).name() == "py.exe":
    print("Program possibly ran via cmd prompt - please note that running from CMD will cause a ton of errors.")
elif psutil.Process(ppid).name() == "pythonw.exe":
    print("Program ran via Python IDLE - this will cause a ton of errors.")
    print("Exitting...")
    exit()

print("Enter your API key: ")
apikey = str(input())
print("Enter your username: ")
username = str(input())
manager = WindowManager()
#setting up windows that will be opened later
#All the games for the leaderboards:

UHC = (
    Window(min_width=50)
    +"UHC Leaderboard Options"
    )
SURVIVAL_GAMES = (
    Window(min_width=50)
    +"Survival Games Leaderboard Options")
QUAKECRAFT = (
    Window(min_width=50)
    +"QuakeCraft Leaderboard Options")
TNTGAMES = (
    Window(min_width=50)
    +"TNT Games Leaderboard Options")
WALLS = (
    Window(min_width=50)
    +"Walls Leaderboard Options")
MURDER_MYSTERY = (
    Window(min_width=50)
    +"Murder Mystery Leaderboard Options")
BUILD_BATTLE = (
    Window(min_width=50)
    +"Build Battle Leaderboard Options")
ARCADE = (
    Window(min_width=50)
    +"Arcade Leaderboard Options")
BEDWARS = (
    Window(min_width=50)
    +"BedWars Leaderboard Options")
DUELS = (
    Window(min_width=50)
    +"Duels Leaderboard Options")
ARENA = (
    Window(min_width=50)
    +"Arena Leaderboard Options")
SPEED_UHC = (
    Window(min_width=50)
    +"Speed UHC Leaderboard Options")
SKYWARS = (
    Window(min_width=50)
    +"SkyWars Leaderboard Options")
#sorry for the length but I couldn't think of a better way to do this part
LeaderboardMenu = (
    Window(min_width=50)
    +"Use this menu to navigate Leaderboards"
    + ["UHC", lambda *_: manager.add(UHC.copy().center())]
    + ["Survival Games", lambda *_: manager.add(UHC.copy().center())] 
    + ["Quakecraft", lambda *_: manager.add(SURVIVAL_GAMES.copy().center())]
    + ["TNT Games", lambda *_: manager.add(TNTGAMES.copy().center())]
    + ["Walls", lambda *_: manager.add(WALLS.copy().center())]
    + ["Murder Mystery", lambda *_: manager.add(MURDER_MYSTERY.copy().center())]
    + ["Build Battle", lambda *_: manager.add(BUILD_BATTLE.copy().center())]
    + ["Arcade", lambda *_: manager.add(ARCADE.copy().center())]
    + ["BedWars", lambda *_: manager.add(BEDWARS.copy().center())]
    + ["Duels", lambda *_: manager.add(DUELS.copy().center())]
    + ["Arena", lambda *_: manager.add(ARENA.copy().center())]
    + ["Speed UHC", lambda *_: manager.add(SPEED_UHC.copy().center())]
    + ["SkyWars", lambda *_: manager.add(SKYWARS.copy().center())]
    + ["Exit", lambda *_: sys.exit(0)]
)

BedWars = (Window(min_width=50))
SkyWars = (Window(min_width=50))
Duels = (Window(min_width=50))
Build_Battle = (Window(min_width=50))
uhc = (Window(min_width=50))

ProfileMenu = (
    Window(min_width=50)
    +"Profile Menu"
    +""
    + ["BedWars", lambda *_: manager.add(BedWars.copy().center())]
    + ["SkyWars", lambda *_: manager.add(SkyWars.copy().center())]
    + ["Duels", lambda *_: manager.add(Duels.copy().center())]
    + ["Build Battle", lambda *_: manager.add(Build_Battle.copy().center())]
    + ["UHC", lambda *_: manager.add(uhc.copy().center())]
    + ["Exit", lambda *_: sys.exit(0)]
)

pets = (Window(min_width=50))

coins = (Window(min_width=50))

FarmingS = (Window(min_width=50))
MiningS = (Window(min_width=50))
CombatS = (Window(min_width=50))
ForagingS = (Window(min_width=50))
FishingS= (Window(min_width=50))
EnchantingS= (Window(min_width=50))
AlchemyS= (Window(min_width=50))
TamingS= (Window(min_width=50))
DungeonS = (Window(min_width=50))

skills = (
    Window(min_width=50)
    + ["UHC", lambda *_: manager.add(uhc.copy().center())]
    + ["UHC", lambda *_: manager.add(uhc.copy().center())]
    + ["UHC", lambda *_: manager.add(uhc.copy().center())]
    + ["UHC", lambda *_: manager.add(uhc.copy().center())]
    + ["UHC", lambda *_: manager.add(uhc.copy().center())]

)
FarmingC = (Window(min_width=50))
MiningC = (Window(min_width=50))
CombatC = (Window(min_width=50))
ForagingC = (Window(min_width=50))
FishingC = (Window(min_width=50))
BossC = (Window(min_width=50))

collections = (Window(min_width=50))

SkyblockMenu = (
    Window(min_width=50)
    +"Choose a profile to view"
    +gui.InputField(prompt="")
    + ["Exit", lambda *_: sys.exit(0)]
)
Mainmenu = (
    Window(min_width=50)
    + "Welcome to HyConsole!"
    + ""
    + ["Profile", lambda *_: manager.add(ProfileMenu.copy().center())]
    + ["Leaderboard", lambda *_: manager.add(LeaderboardMenu.copy().center())]
    + ["Skyblock", lambda *_: manager.add(SkyblockMenu.copy().center())]
    + ["Exit", lambda *_: sys.exit(0)]
)
#starting the window
validitytest = requests.get(url = f"https://api.mojang.com/users/profiles/minecraft/{username}?").json()
try:
    validitytest = str(validitytest["name"])
    if validitytest == username:
        print("Valid")
except Exception:
    print("Invalid or Wrong Username!")
    exit()

playerdata = requests.get(
    url = "https://api.hypixel.net/player", params = {
        "key": apikey,
        "name": username}).json()
uuid = requests.get(url = f"https://api.mojang.com/users/profiles/minecraft/{username}?").json()
uuid = str(uuid["id"])
skyblockdata = requests.get(
    url = "https://api.hypixel.net/skyblock", params = {
        "key": apikey,
        "uuid": uuid}).json()
leaderboarddata = requests.get(
                        url = "https://api.hypixel.net/leaderboards", params = {
                                "key": apikey
                        }
                ).json()

        
manager.add(Mainmenu)
manager.run()
