
### 최소 요구 사항 및 지원되는 SDK

https://developer.apple.com/kr/support/xcode/

### download 
https://developer.apple.com/download/all/

### 직접 다운로드 
https://download.developer.apple.com/Developer_Tools/Xcode_8.2/Xcode_8.2.xip

https://download.developer.apple.com/Developer_Tools/Xcode_12.2/Xcode_12.2.xip

https://download.developer.apple.com/Developer_Tools/Xcode_12.3/Xcode_12.3.xip

https://download.developer.apple.com/Developer_Tools/Xcode_13.5/Xcode_13.5.xip




# Use previous/older SDKs with Xcode

Since monterey update does not allow us to use Xcode previous than 13, let's show how to "install previous SDKs"

# Needed

Swift toolchains, from https://swift.org/download/

Previous Xcode.xip, from the https://developer.apple.com

Quit Xcode

# Copying older SDKs into the latest Xcode

Note: sudo is only needed if you have installed Xcode from the Mac App Store

```
% sudo cp -a /Applications/Xcode_12.4.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS.sdk /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS14.4.sdk
% sudo cp -a /Applications/Xcode_12.4.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator.sdk /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator14.4.sdk
```

```
% sudo cp -a /Applications/Xcode_12.5.1.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS.sdk /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS14.5.sdk
% sudo cp -a /Applications/Xcode_12.5.1.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator.sdk /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator14.5.sdk
```

Then, let's list them :

```
% xcodebuild -showsdks
2021-10-26 14:52:25.564 xcodebuild[84599:187956] [MT] DVTSDK: Skipped SDK /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator14.4.sdk; its version (14.4) is below required minimum (15.0) for the iphonesimulator platform.
2021-10-26 14:52:25.564 xcodebuild[84599:187956] [MT] DVTSDK: Skipped SDK /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator14.5.sdk; its version (14.5) is below required minimum (15.0) for the iphonesimulator platform.
```

Ok, we need to lower the MinimumSDKVersion:

```
% /usr/libexec/PlistBuddy -c "Print :MinimumSDKVersion" /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Info.plist
15.0
% sudo /usr/libexec/PlistBuddy -c "Set :MinimumSDKVersion 14.4" /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Info.plist
```

Then :
```
% xcodebuild -version
Xcode 13.1
Build version 13A1030d
% xcodebuild -showsdks
DriverKit SDKs:
	DriverKit 21.0.1              	-sdk driverkit21.0.1

iOS SDKs:
	iOS 14.4                      	-sdk iphoneos14.4
	iOS 14.5                      	-sdk iphoneos14.5
	iOS 15.0                      	-sdk iphoneos15.0

iOS Simulator SDKs:
	Simulator - iOS 14.4          	-sdk iphonesimulator14.4
	Simulator - iOS 14.5          	-sdk iphonesimulator14.5
	Simulator - iOS 15.0          	-sdk iphonesimulator15.0

macOS SDKs:
	macOS 12.0                    	-sdk macosx12.0

tvOS SDKs:
	tvOS 15.0                     	-sdk appletvos15.0

tvOS Simulator SDKs:
	Simulator - tvOS 15.0         	-sdk appletvsimulator15.0

watchOS SDKs:
	watchOS 8.0                   	-sdk watchos8.0

watchOS Simulator SDKs:
	Simulator - watchOS 8.0       	-sdk watchsimulator8.0
```

And relaunch Xcode, and you will be able to choose in the "Base SDK" (akka SDKROOT) build setting of your project:
- iOS (15, provided by Xcode, choose default toolchain in Xcode preferences, or Xcode menu -> Toolchains)
- iOS 14.4 (choose swift 5.3.2 toolchain)
- iOS 14.5 (choose swift 5.4.3 toolchain) 

of course it also works for macOS SDKs

# References

Thanks to :
https://developer.apple.com/forums/thread/43381 

https://stackoverflow.com/questions/1480184/how-do-i-determine-which-ios-sdk-i-have/19377753#19377753


## 1
Need to set the min sdk for the device too

% /usr/libexec/PlistBuddy -c "Print :MinimumSDKVersion" /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Info.plist

## 2
For macOS to get 13.sdk back:

Download Xcode 14.3.1

unxip it

cp -a Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX13.3.sdk

unxip Xcode_14.3.1.xip && cp -a Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk 

/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX13.3.sdk


## 3

For macOS to get 13.sdk back:

Download Xcode 14.3.1

unxip it

cp -a Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX13.3.sdk

unxip Xcode_14.3.1.xip && cp -a Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk 

/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX13.3.sdk




