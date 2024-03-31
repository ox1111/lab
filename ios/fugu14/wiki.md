

## Q&A

### _really_ stupid question: 

```
I saw the explanation that Fugu14 can't be ported to 14.1 
because the kernel exploit isn't available there. 
Which part of the kernel exploit is missing? I thought iOS 14.1 has DriverKit?
```
### Ah, that's why:

```
Fugu14 prints "Failed to create Memory Descriptor!"
when run on iOS 14.1. Guess DriverKit on iOS 14.1 is different?
```


### OK, I see:
```
CreateMemoryDescriptorFromClient, which Fugu14 exploits,
is only introduced on macOS 12.0:
https://developer.apple.com/documentation/driverkit/iouserclient/3674819-creatememorydescriptorfromclient
iOS 14.2 and above has the method,
but not iOS 14.1 (I double-checked: the IOUserClient::_Dispatch method doesn't have the method at all)
```
### Ah, that's why:
```
 Fugu14 prints "Failed to create Memory Descriptor!"
when run on iOS 14.1. Guess DriverKit on iOS 14.1 is different?
```

### CreateMemoryDescriptorFromClient
```
virtual kern_return_t CreateMemoryDescriptorFromClient
(uint64_t memoryDescriptorCreateOptions, uint32_t segmentsCount, const IOAddressSegment segments[32], IOMemoryDescriptor **memory);

```
