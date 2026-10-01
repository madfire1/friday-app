[app]
title = Friday AI
package.name = fridayai
package.domain = org.madfire
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,google-genai,jnius

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a

# Permessi speciali per microfono e background a schermo spento
android.permissions = RECORD_AUDIO, WAKE_LOCK, FOREGROUND_SERVICE, FOREGROUND_SERVICE_MICROPHONE

android.minapi = 21
android.ndk_api = 21
android.private_storage = True
android.skip_update_buildozer = False

[buildozer]
log_level = 2
warn_on_root = 1
