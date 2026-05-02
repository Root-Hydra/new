[app]

# (str) Title of your application
title = BDCS WiFi Brute

# (str) Package name
package.name = bdcs_wifi_brute

# (str) Package domain (needed for android/ios packaging)
package.domain = org.bdcs.unsung

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 1.0

# (list) Application requirements
# KivyMD এবং Pillow এখানে যুক্ত করা হয়েছে ডিজাইন এবং ইমেজ হ্যান্ডলিংয়ের জন্য
requirements = python3, kivy==2.2.1, kivymd==1.1.1, pillow

# (list) Supported orientations
orientation = portrait

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
# ওয়াইফাই স্ক্যান এবং লোকেশন অ্যাক্সেসের জন্য এই পারমিশনগুলো জরুরি
android.permissions = INTERNET, ACCESS_WIFI_STATE, CHANGE_WIFI_STATE, ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION

# (int) Target Android API
android.api = 33

# (int) Minimum API support (Oppo A83 এর মতো ফোনের জন্য ২১ রাখা হয়েছে)
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use
android.ndk_api = 21

# (bool) Use --private data storage
android.private_storage = True

# (bool) If True, then automatically accept SDK license
android.accept_sdk_license = True

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature
android.allow_backup = True

# (str) The format used to package the app for debug mode
android.debug_artifact = apk

[buildozer]

# (int) Log level (2 = debug mode)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
