import os
import glob
import subprocess as sp
os.system("color b")
def hasPHP():
    try:
        sp.check_call(['php', '-v'])
        return True
    except:
        return False
if(os.path.isdir("output") == False):
    os.mkdir("output")
    print("generating Folder called 'output'")
if(os.path.isdir("bin")):
    print("We are going to use the bin folder as PHP source")
    php = "bin\php\php.exe"
elif(hasPHP()):
    print("since there is no folder called 'bin', we are using the installed PHP version")
    php = "php"
else:
    print("No PHP installed and No Directonary called 'bin' found")
    print("to use this code pls install PHP or copy the bin Folder by Pocketmine into this Folder")
    exit("Exit: 'NO PHP FOUND'")

if(os.path.isdir("virions")):
    virions = glob.glob("virions/*.phar")
    print(len(virions), "Virions Detected:")
    if(len(virions) == 0):
        exit("There are no virions to inject")
    for i in virions:
        print("===> ", i)
    if(os.path.isdir("plugins")):
        plugins = glob.glob("plugins/*.phar")
        print(len(plugins), "Plugins Detected:")
        if (len(plugins) == 0):
            exit("There are no plugins to be injected")
        elif(len(plugins) > 1):
            print("There are more then 1 Plugins in the Plugin Folder")
            x = input("Should We inject all Virions into Every Plugin? Y/[N]")
            if(x != "Y"):
                exit("If u want to inject the virions to only one Plugin, pls remove the other Plugins from the Plugins_folder")
        for p in plugins:
            print("")
            print("===> ", p)
            ap = p.replace("plugins", "")
            bp = "output" + ap
            ccmd = "copy" + " " + p + " " + bp
            os.system(ccmd)
            print("")
            print("")
            for v in virions:
                print("===> ","Injecting", v, "into", p)
                cmd = php + " -dphar.readonly=0 " + v + " " + bp
                os.system(cmd)
    else:
        os.mkdir("plugins")
        exit("Error: Folder 'plugins' not Found")
else:
    os.mkdir("virions")
    if (os.path.isdir("plugins") == False):
        os.mkdir("plugins")
    exit("Error: Folder 'virions' not Found")
print("")
print("finnished Injecting")
