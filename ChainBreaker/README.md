# ChainBreaker (Zinciri Kırma)

A powerful habit tracking and breaking app that helps users break bad habits and build good ones.

![Platform](https://img.shields.io/badge/Platform-iOS%20%7C%20Android-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## Overview

ChainBreaker is a comprehensive habit tracking application designed to help users break bad habits and develop positive ones. With features like progress tracking, social support, and detailed analytics, it provides all the tools needed for successful habit transformation.

## Key Features

### Core Features 🎯
- Habit tracking and management
- Daily, weekly, and monthly goals
- Progress statistics and analytics
- Achievement badges and rewards

### Social Features 👥
- Friend connections
- Achievement sharing
- Group challenges
- Motivational messages

### Analytics & Insights 📊
- Detailed progress tracking
- Success rate analysis
- Custom recommendations
- Visual progress charts

## Technical Stack

### iOS
- Swift 5.0
- SwiftUI
- Core Data
- iOS 14.0+

### Android
- Kotlin
- Jetpack Compose
- Room Database
- Android 8.0+

### Backend
- Firebase
  - Authentication
  - Realtime Database
  - Cloud Storage
  - Analytics

## Project Structure

```
ChainBreaker/
├── src/
│   ├── ios/           # iOS application source
│   ├── android/       # Android application source
│   └── shared/        # Shared business logic
├── assets/           # Images, fonts, and other resources
├── docs/            # Documentation
└── README.md        # This file
```

## Getting Started

### Prerequisites
- Xcode 13+ (for iOS)
- Android Studio Arctic Fox+ (for Android)
- Firebase account
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ChainBreaker.git
cd ChainBreaker
```

2. iOS Setup:
```bash
cd src/ios
pod install
open ChainBreaker.xcworkspace
```

3. Android Setup:
```bash
cd src/android
./gradlew build
```

## Development

### Building iOS App
```bash
xcodebuild -workspace ChainBreaker.xcworkspace -scheme ChainBreaker
```

### Building Android App
```bash
./gradlew assembleDebug
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Testing

- Unit Tests: `./gradlew test` (Android) / `xcodebuild test` (iOS)
- UI Tests: Included in the respective platform projects
- Integration Tests: Firebase Test Lab

## Roadmap

- [x] Project Setup
- [ ] Basic UI Implementation
- [ ] Core Features Development
- [ ] Social Features Integration
- [ ] Analytics Implementation
- [ ] Beta Testing
- [ ] App Store Release

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Your Name - [@yourusername](https://twitter.com/yourusername)
Project Link: [https://github.com/yourusername/ChainBreaker](https://github.com/yourusername/ChainBreaker)

## Acknowledgments

- Firebase team for the backend infrastructure
- The open source community
- All our beta testers and contributors 