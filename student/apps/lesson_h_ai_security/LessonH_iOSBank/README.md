# Lesson H iOS Bank

Minimal SwiftUI iOS app used for the lesson H MobSF-style iOS task.

## Build

```bash
cd student/apps/lesson_h_ai_security/LessonH_iOSBank
xcodebuild \
  -project LessonH_iOSBank.xcodeproj \
  -scheme LessonH_iOSBank \
  -configuration Debug \
  -destination 'generic/platform=iOS' \
  CODE_SIGNING_ALLOWED=NO \
  build
```

## Artifact

- Built app bundle for analysis: `build/Build/Products/Debug-iphoneos/LessonH_iOSBank.app`
- Signed device build for the connected iPhone: `/Users/jacekkaluzny/Library/Developer/Xcode/DerivedData/LessonH_iOSBank-etfbswpalmqbkwfiteajxejpgwaw/Build/Products/Debug-iphoneos/LessonH_iOSBank.app`

## Notes

- The app uses local mock data only.
- MobSF can analyze the source tree and the built `.app` bundle locally.
- The app is intentionally simple and lesson-oriented, with mock payment fields and buttons.
