from . import APKParse

a = APKParse('/home/neo/work/xkern/android/app-debug.apk')
a.work()
print(a.version_code, a.version_name, a.version_id, a.release_type)
print(a.bundle_id)
print(a.checksum)
