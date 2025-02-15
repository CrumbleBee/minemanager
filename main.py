import requests
import os
import config
import shutil
from colorama import Fore
from datetime import datetime

# Clear terminal
def createserver():
    if config.clear_terminal == True:
        clearlinux = os.system("clear")
        clearwindows = os.system("cls")
        try:
            clearlinux()
            clearwindows()
        except:
            pass

    # Show server jar menu
    print(Fore.CYAN + "\n[0 To return]\t\tServer Creator" + Fore.WHITE + "\n\n[1] CraftBukkit \t\t\t\t[8] Purpur\n[2] Fabric\t\t\t\t\t[9] Quilt\n[3] Folia\t\t\t\t\t[10] Spigot\n[4] Forge\t\t\t\t\t[11] Vanilla\n[5] Neoforge\t\t\t\t\t[12] Velocity\n[6] Paper\t\t\t\t\t[13] Waterfall\n[7] Pufferfish")
    jarchoice = input("\nWhat server jar do you want?: ")
    if jarchoice == "0":
        mainmenu()
    if jarchoice == "1":
        jartype = "craftbukkit"
    elif jarchoice == "2":
        jartype = "fabric"
    elif jarchoice == "3":
        jartype = "folia"
    elif jarchoice == "4":
        jartype = "forge"
    elif jarchoice == "5":
        jartype = "neoforge"
    elif jarchoice == "6":
        jartype = "paper"
    elif jarchoice == "7":
        jartype = "pufferfish"
    elif jarchoice == "8":
        jartype = "purpur"
    elif jarchoice == "9":
        jartype = "quilt"
    elif jarchoice == "10":
        jartype = "spigot"
    elif jarchoice == "11":
        jartype = "vanilla"
    elif jarchoice == "12":
        jartype = "velocity"
    elif jarchoice == "13":
        jartype = "waterfall"
    else:
        print(Fore.RED + "Invalid input.")
        print(Fore.WHITE + "Exiting...")
        exit()
    print("Server jar "+jartype+" chosen")
    # Ask for Minecraft version
    version = input("What version do you want?: ")
    print("Version "+version+" chosen.")

    # Check for custom names in config and if so, ask for name
    if config.custom_names == True:
        servername = input("Server folder name: ")
        directory = os.path.join("servers", f"{servername}")

    # Set name as server type and Minecraft version
    else:
        directory = os.path.join("servers", f"{jartype}_{version}")

    # Make folder with name
    os.makedirs(directory, exist_ok=True)
    print(Fore.GREEN + "Folder successfully created.")

    # Download jar file
    url = "https://mcutils.com/api/server-jars/"+jartype+"/"+version+"/download"
    r = requests.get(url, allow_redirects=True)
    response = str(r)
    if response == "<Response [500]>":
        print(Fore.RED + "ERROR OBTAINING JAR!")
        print(Fore.WHITE + "Aborting...")
        os.rmdir(directory)
        print(Fore.WHITE + "Deleted folder.")
    else:
        pass
    jarpath = os.path.join(directory, "server.jar")
    with open(jarpath, "wb") as serverjar:
        serverjar.write(r.content)
    serverjar.close()
    print(Fore.GREEN + "Server jar "+jartype+" saved.")

    # Make start script
    if config.make_start_bat_script == True:
        max_ram = config.max_ram
        min_ram = config.min_ram
        startscriptpath = os.path.join(directory, "start.bat")
        with open(startscriptpath, "w") as file:
            file.write(f"java -Xmx{max_ram} -Xms{min_ram} -jar server.jar nogui\npause")
        file.close()
        print(Fore.GREEN + "start.bat sucessfully created.")
    if config.make_start_sh_script == True:
        max_ram = config.max_ram
        min_ram = config.min_ram
        startscriptpathsh = os.path.join(directory, "start.sh")
        with open(startscriptpathsh, "w") as file:
            file.write(f"screen -S Minecraft java -Xms{min_ram} -Xmx{max_ram} -jar server.jar")
        file.close()
        print(Fore.GREEN + "start.sh sucessfully created.")

    # Accept EULA
    if config.accept_eula == True:
        eulapath = os.path.join(directory, "eula.txt")
        with open(eulapath, "w") as eula:
            eula.write('eula=true')
            eula.close()
        print(Fore.GREEN + "EULA.txt sucessfully created.")

    print(Fore.GREEN + "Server created successfully!")
    print(Fore.WHITE + f"Server location: {directory}")

# Clear terminal function
def clear():
    if config.clear_terminal == True:
        clearlinux = os.system("clear")
        clearwindows = os.system("cls")
        try:
            clearlinux()
            clearwindows()
        except:
            pass

# List servers function
def serverlist():
    clear()
    print(Fore.CYAN + "\n[0] To return\t\tServer Manager\n")
    serversdirectory = os.path.join("servers")
    serverlist = os.listdir(serversdirectory)
    for (i, item) in enumerate(serverlist, start=1):
        print(Fore.WHITE + f"[{i}]", f"{item}")
    selectedserverstring = input("Which server would you like to select?: ")
    if selectedserverstring == "0":
        serveroptions()
    else:
        selectedserver = int(selectedserverstring)
        server = (serverlist[selectedserver - 1])
        return server


# List possible server imports
def possibleserverimports():
    clear()
    print(Fore.CYAN + "\n[0] To return\t\tServer Manager\n")
    importdirectory = os.path.join("imports", "servers")
    importlist = os.listdir(importdirectory)
    for (i, item) in enumerate(importlist, start=1):
        print(Fore.WHITE + f"[{i}]", f"{item}")
    selectedimportstring = input("Which import would you like to select?: ")
    if selectedimportstring == "0":
        serveroptions()
    else:
        selectedimport = int(selectedimportstring)
        importedserver = (importlist[selectedimport - 1])
        return importedserver
    
# List possible world imports
def possibleworldimports():
    clear()
    print(Fore.CYAN + "\n[0] To return\t\tServer Manager\n")
    importdirectory = os.path.join("imports", "worlds")
    importlist = os.listdir(importdirectory)
    for (i, item) in enumerate(importlist, start=1):
        print(Fore.WHITE + f"[{i}]", f"{item}")
    selectedimportstring = input("Which import would you like to select?: ")
    if selectedimportstring == "0":
        serveroptions()
    else:
        selectedimport = int(selectedimportstring)
        importedworld = (importlist[selectedimport - 1])
        return importedworld

# Import server
def serverimport(importedserver):
    serversdirectory = os.path.join(os.getcwd(), "servers")
    importsdirectory = os.path.join(os.getcwd(), "imports", "servers")
    servername = input("Server name?: ")
    serverdir = os.path.join(serversdirectory, servername)
    importdir = os.path.join(importsdirectory, importedserver)
    shutil.unpack_archive(importdir, serverdir)

# Import world
def worldimport(importedworld, server):
    worlddirectory = os.path.join(os.getcwd(), "servers", server)
    importsdirectory = os.path.join(os.getcwd(), "imports", "worlds")
    worlddir = os.path.join(worlddirectory, "world")
    importdir = os.path.join(importsdirectory, importedworld)
    shutil.unpack_archive(importdir, worlddir)
    print(f"World imported to {server}.")

# Export server
def serverexport(server):
    serversdirectory = os.path.join(os.getcwd(), "servers")
    exportsdirectory = os.path.join(os.getcwd(), "exports", "servers")
    serverdir = os.path.join(serversdirectory, server)
    date = datetime.today().strftime(" %d-%m-%Y %H-%M")
    exportname = (server + date)
    export = os.path.join(exportsdirectory, exportname)
    shutil.make_archive(export, "zip", serverdir)
    print(f"{server} exported.")

# Export world
def worldexport(server):
    serversdirectory = os.path.join(os.getcwd(), "servers")
    exportsdirectory = os.path.join(os.getcwd(), "exports", "worlds")
    worlddir = os.path.join(serversdirectory, server, "world")
    date = datetime.today().strftime(" %d-%m-%Y %H-%M")
    exportname = (server + date)
    export = os.path.join(exportsdirectory, exportname)
    shutil.make_archive(export, "zip", worlddir)
    print(f"{server} world exported.")

# Delete server
def serverdelete(server):
    serversdirectory = os.path.join(os.getcwd(), "servers")
    serverdir = os.path.join(serversdirectory, server)
    print(Fore.RED + "THIS WILL DELETE THE FOLDER OF THE SERVER AND ALL OF IT'S CONTENTS, ARE YOU SURE YOU WANT TO DO THIS?")
    answer = input(Fore.WHITE + "y/n: ")
    if answer == "y":
        shutil.rmtree(serverdir)
        print(f"{server} deleted.")
    else:
        print("Deletion aborted.")

# Delete world
def worlddelete(server):
    serversdirectory = os.path.join(os.getcwd(), "servers")
    worlddir = os.path.join(serversdirectory, server, "world")
    print(Fore.RED + "THIS WILL DELETE THE WORLD (AND PLAYER DATA) OF THE SERVER AND ALL OF IT'S CONTENTS, ARE YOU SURE YOU WANT TO DO THIS?")
    answer = input(Fore.WHITE + "y/n: ")
    if answer == "y":
        shutil.rmtree(worlddir)
        print(f"{server}'s world deleted.")
    else:
        print("Deletion aborted.")

# Rename server
def serverrename(server):
    serversdirectory = os.path.join(os.getcwd(), "servers")
    original = os.path.join(serversdirectory, server)
    name = input("New name: ")
    new = os.path.join(serversdirectory, name)
    os.rename(original, new)
    print(f"{name} renamed to {new}.")

# Unban all
def unban(server):
    serversdirectory = os.path.join(os.getcwd(), "servers")
    bannedplayers = os.path.join(serversdirectory, server, "banned-players.json")
    bannedips = os.path.join(serversdirectory, server, "banned-ips.json")
    os.remove(bannedplayers)
    os.remove(bannedips)
    print(f"All users unbanned from {server}.")

# Deop all
def deop(server):
    serversdirectory = os.path.join(os.getcwd(), "servers")
    ops = os.path.join(serversdirectory, server, "ops.json")
    os.remove(ops)
    print(f"All users deoped from {server}.")

# Copy server.properties template
def serverproperties(server):
    serversdirectory = os.path.join(os.getcwd(), "servers")
    serverdirectory = os.path.join(serversdirectory, server)
    template = os.path.join("template")
    properties = os.path.join(template, "server.properties")
    serverproperties = os.path.join(serverdirectory, "server.properties")
    shutil.copy(properties, serverproperties)
    print("Updated server.properties from template.")

# List options
def serveroptions():
    clear()
    print(Fore.CYAN + "\n[0] To return\t\tServer Manager" + Fore.WHITE + "\n\n[1] Import server \t\t\t\t[6] Import world\n[2] Export server\t\t\t\t[7] Export world\n[3] Delete server\t\t\t\t[8] Delete world\n[4] Rename server\t\t\t\t[9] Unban all\n[5] Update server.properties\t\t\t[10] Deop all")
    choice = input("\nWhat server tool do you want to use?: ")
    if choice == "0":

        # Return
        mainmenu()
    if choice == "1":

        # Import server
        imported_server = possibleserverimports()
        serverimport(imported_server)
    elif choice == "2":

        # Export server
        selected_server = serverlist()
        serverexport(selected_server)
    elif choice == "3":

        # Delete server
        selected_server = serverlist()
        serverdelete(selected_server)
    elif choice == "4":

        # Rename server
        selected_server = serverlist()
        serverrename(selected_server)
    elif choice == "5":

        # Update server.properties
        selected_server = serverlist()
        serverproperties(selected_server)
    elif choice == "6":

        # Import world
        selected_server = serverlist()
        imported_world = possibleworldimports()
        worldimport(imported_world, selected_server)
    elif choice == "7":

        #Export world
        selected_server = serverlist()
        worldexport(selected_server)
    elif choice == "8":

        # Delete world
        selected_server = serverlist()
        worlddelete(selected_server)
    elif choice == "9":

        # Unban all
        selected_server = serverlist()
        unban(selected_server)
    elif choice == "10":

        # Deop all
        selected_server = serverlist()
        deop(selected_server)
    else:
        print(Fore.RED + "INVALID INPUT.")
        print(Fore.WHITE + "Please pick a number 1-10.")

def mainmenu():
    clear()
    print(Fore.CYAN + "\n\t\t\tMineManager" + Fore.WHITE + "\n\n[1] Create server \t\t\t\t[2] Manage server")
    choice = input("\nWhat tool do you want to use?: ")
    if choice == "1":
        createserver()
    elif choice == "2":
        serveroptions()
    else:
        print(Fore.RED + "INVALID INPUT.")
        print(Fore.WHITE + "Please pick a number 1-2.")
        exit()
os.makedirs("exports", exist_ok=True)
os.makedirs("imports", exist_ok=True)
os.makedirs("servers", exist_ok=True)
mainmenu()