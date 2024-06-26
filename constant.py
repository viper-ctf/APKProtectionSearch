SO_FEATURE = {
    "梆梆加固": r"libDexHelper\S*.so|libsecexe\S*.so|libSecShell\S*.so|libsecmain\S*.so",
    "360加固": r"libjiagu\S*.so|libprotectClass\S*.so",
    "通付盾加固": r"libegis\S*.so|libegisboot\S*.so|libegismain\S*.so|libNSaferOnly\S*.so",
    "网秦加固": r"libnqshield\S*.so",
    "腾讯加固": r"libtxRes\S*.so|libshell\S*.so|^libtup.so$|mix\S*.dex|libtosprotection.\S*.so",
    "爱加密加固": r"ijiami\S*.dat|ijiami.ajm|libexec\S*.so",
    "娜迦加固": r"lib\wdog.so|libchaosvmp\S*.so",
    "阿里聚安全加固": r"libmobisec\w*.so|libaliutils\S*.so|aliprotect.dat|libsgmain.so|libsgsecuritybody.so",
    "百度加固": r"libbaiduprotect\S*.so",
    "网易易盾加固": r"libnesec.so|data.db|clazz.jar",
    "APKProtect加固": r"libAPKProtect\S*.so",
    "几维安全": r"libkwscmm.so|libkwscr.so|libkwslinker.so",
    "顶像科技": r"libx3g.so",
    "盛大": r"libapssec.so",
    "瑞星": r"librsprotect.so",
}

APPLICATION_FEATURE = {
    "梆梆加固": r"com.secneo.apkwrapper|com.secneo.guard.ApplicationWrapper|com.secshell.secData.ApplicationWrapper",
    "360加固": r"com.stub.StubApp",
    "通付盾加固": r"com.payegis.ProxyApplication",
    "网秦加固": r"com.nqshield.NqApplication",
    "腾讯加固": r"com.tencent.StubShell.TxAppEntry",
    "爱加密加固": r"com.ijiami.residconfusion.ConfusionApplication|com.shell.SuperApplication|s.h.e.l.l.S",
    "娜迦加固": r"com.edog.AppWrapper|com.chaosvmp.AppWrapper",
    "阿里聚安全加固": r"com.ali.mobisecenhance.StubApplication",
    "百度加固": r"com.baidu.protect.StubApplication",
    "网易易盾加固": r"com.netease.nis.wrapper.MyApplication",
}
NOWRAPPER = "NO WRAPPER"
RESULTSTRING = "This apk might be "
