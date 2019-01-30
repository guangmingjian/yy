import ctypes, sys
import yy.tupo as tp

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    tp = tp.ToPo()
    tp.fightnN(5)
else:
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:#in python2.x
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)
