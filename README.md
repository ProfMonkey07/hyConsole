# HypeCli
Hype Cli is a way to get data on players and leaderboards from the Hypixel Minecraft server from the command line. 
Keep in mind I have no affiliation with the Hypixel Server

installation:
  work in progress
  
 syntax: if you have it as an executeable you will use ./hypecli, then use one of various arguments
 using -l will return leaderboard data
 using -p will return player data
 
 -p is still in progress, but -l currently is fully functional
 it will take you through selecting the leaderboard, then print out the leaderboard
 keep in mind this can be quite slow, as the speed varies based on internet connection, etc
 this is because it is required to convert every uuid to a username with the Mojang api one at a time
 I am currently working on fixing this but for now be patient
 A graphical user interface in the command line will be coming soon
