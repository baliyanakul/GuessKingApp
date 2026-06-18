[app]
title = Guess King
package.name = guessking
package.domain = org.baliyanakul
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0
requirements = python3,kivy

orientation = portrait
fullscreen = 1

# Android configurations (Stable Versions Localized)
android.api = 33
android.minapi = 21
android.sdk = 33
android.build_tools_version = 33.0.0
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# Python for android settings
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
