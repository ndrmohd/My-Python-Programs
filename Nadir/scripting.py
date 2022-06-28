import platform,datetime,os

print('  ____________________________________________________________________________')
print('\n               System Details:')
print('  ____________________________________________________________________________')
print('\n  Username          :  ',os.getlogin())
print('\n  Operating System  :  ',platform.system())
print('\n  Version           :  ',platform.version())
print('\n  Processor         :  ',platform.processor())
print('\n  Platform          :  ',platform.platform())
print('\n  Architecture      :  ',platform.architecture())
print('\n  Machine Number    :  ',platform.machine())

print('\n  Mother Board      :  ',)
print('\n  ____________________________________________________________________________')
print('\n  Date & Time       :  ',datetime.datetime.now())
print(' ') 