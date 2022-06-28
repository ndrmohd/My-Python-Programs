# architecture platform os version processor datetime
# platform version
import datetime
import os
import platform
print("                            ",datetime.datetime.now(),) 
print("                                   ","INFORMATION")
print("1.Current loggedin user-",os.getlogin(),end="__________________________________________")
print("2.Platform-",platform.platform())
print("3.Platform version-",platform.version(),end="____________________________________________") 
print("4.Architecture-",platform.architecture())
print("5.Processor-",platform.processor(),end="__________") 
print("6.Machine-",platform.machine())
print("7.system-",platform.system())