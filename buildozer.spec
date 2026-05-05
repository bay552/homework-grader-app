[app]

# (str) Title of your application
title = 作业批改 AI

# (str) Package name
package.name = homeworkgrader

# (str) Package domain (needed for android/ios packaging)
package.domain = org.beibeiqi

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ttf

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy==2.3.0,plyer,pillow,requests,android

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = CAMERA,INTERNET,ACCESS_NETWORK_STATE,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --user for pip installs (android only)
android.pip_args = --index-url=https://pypi.tuna.tsinghua.edu.cn/simple

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
android.ndk_api = 21

# (str) The Android arch to build for
android.archs = arm64-v8a,armeabi-v7a

# (bool) If True, then skip trying to update the Android sdk
android.skip_update = False

# (bool) If True, then automatically accept SDK license
android.accept_sdk_license = True
# (bool) If True, use virtualenv for python dependencies
android.use_virtualenv = False
# (str) Path to a custom keystore
# android.keystore = /path/to/keystore

# (str) Alias name for keystore
# android.keyalias = youralias


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .ipa) storage
bin_dir = ./bin
