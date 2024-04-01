## 원본
https://worthdoingbadly.com/hv/


<main class="page-content" aria-label="Content" style="position: relative">
      <div class="wrapper">
        <article class="post h-entry" itemscope itemtype="http://schema.org/BlogPosting">

  <header class="post-header">
    <h1 class="post-title p-name" itemprop="name headline">Hardware-accelerated virtual machines on jailbroken iPhone 12 / iOS 14.1</h1>
    <p class="post-meta">
      <time class="dt-published" datetime="2022-06-06T00:00:00+00:00" itemprop="datePublished">Jun 6, 2022
      </time></p>
  </header>

  <div class="post-content e-content" itemprop="articleBody">
    <p>I unlocked <a href="https://developer.apple.com/documentation/hypervisor?language=objc">Hypervisor.framework</a> on my jailbroken phone and modified <a href="https://getutm.app">UTM</a>, a popular <a href="https://www.qemu.org">QEMU</a> port for iOS, to run arm64 Linux in a VM at full native speed. …for the clickbait - and to show iPhone’s untapped potential.</p>

<p>iPhone 12’s A14 CPU supports virtualization, just like Apple Silicon Macs. Virtualization support is disabled in the kernel, but can be re-enabled with a jailbreak. VMs on iPhone 12 are limited to 900MB of RAM, however.</p>

<p>Here’s a video of my iPhone 12 running the modified UTM, booting a Fedora 36 VM, and showing the requisite Neofetch and LibreOffice demo.</p>

https://www.youtube-nocookie.com/embed/yrRR7reUseo

<h1 id="information">Information</h1>

<h4 id="is-this-practical">Is this practical?</h4>

<p>Absolutely not. This is a proof-of-concept that targets iPhone 12 on iOS 14.1 only. It’s also really unstable (VMs can only use 900MB of RAM, and if it goes over, often the whole phone crashes and reboots).</p>

<h4 id="how-much-faster-is-hardware-accelerated-virtualization-compared-to-utms-jit-mode">How much faster is hardware accelerated virtualization compared to UTM’s JIT mode?</h4>

<p>Single-core score in Geekbench 5:</p>

<ul>
  <li>Native iPhone 12: <a href="https://browser.geekbench.com/ios_devices/iphone-12">1573</a></li>
  <li>Hypervisor.framework: <a href="https://browser.geekbench.com/v5/cpu/15319609">1504</a> to <a href="https://browser.geekbench.com/v5/cpu/15298464">1511</a></li>
</ul>

<p>This is almost native speed.</p>

<p>I did not try running Geekbench in JIT-only mode on my phone. However, an Apple Silicon Mac gets a Geekbench score of <a href="https://khronokernel.github.io/apple/silicon/2021/01/17/QEMU-AS.html">68</a> when emulating x86 with QEMU/UTM JIT. Emulating arm64 would have a smaller overhead, but I’d still expect a 5x to 10x slowdown.</p>

<p>One disadvantage of hardware accelerated virtualization: double the RAM overhead. iOS terminates the VM when it uses more than 1GB of RAM. In non-hardware accelerated mode, VMs can use 2GB of RAM. (I tried increasing this limit, but this caused kernel panics)</p>

<h4 id="can-this-be-ported-to-other-devices">Can this be ported to other devices?</h4>

<p>A14 (iPhone 12) on jailbroken iOS 14.7 and below:</p>
<ul>
  <li>The kernel unlock can be ported to iOS versions supposed by Fugu14</li>
  <li>(the unlock won’t work on iOS 15 since the hypervisor heap was moved to read-only memory)</li>
  <li>I did not attempt to handle different kernel versions in my proof-of-concept</li>
  <li>to make this usable on other devices/versions, you’ll need to implement patchfinding for offsets</li>
  <li>if you have any questions, I’ll be happy to help.</li>
</ul>

<p>M1 (iPad Pro 2021/iPad Air 2022) on jailbroken iOS 14/15:</p>
<ul>
  <li>These devices already have Hypervisor support unlocked in the kernel</li>
  <li>so any jailbreak should work, not just Fugu14</li>
  <li>sign with the <code class="language-plaintext highlighter-rouge">com.apple.private.hypervisor</code> entitlement and include the decompiled Hypervisor.framework</li>
</ul>

<p>All other devices:</p>
<ul>
  <li>CPUs before A14/M1 do not have hardware accelerated virtualization support</li>
</ul>

<h4 id="will-it-run-crysis">Will it run Crysis?</h4>

<p>No.</p>

<p>Believe me, I tried. Windows arm64 refused to boot on my decompiled Hypervisor.framework, and I don’t have time to troubleshoot why.</p>

<p>Even if Windows were to boot, software rendered Crysis runs at 1fps at 640x480 on my M1 Mac Mini with 4 performance cores… so on an iPhone with 2 performance cores, it’d be 0.5fps.</p>

<p>(I also tried booting Android - I spent several days trying to run <a href="https://waydro.id">Waydroid</a> in my Linux VM without success. The lack of RAM prevents it from working anyways.)</p>

<h1 id="how-this-works">How this works</h1>

<p>Unlocking Hypervisor.framework required three parts:</p>

<ul>
  <li><a href="https://github.com/ox1111/Fugu14_zhuowei_ver">A modified Fugu14 jailbreak</a> to call hypervisor functions in the kernel</li>
  <li><a href="https://github.com/ox1111/HvDecompile">A hand-decompiled Hypervisor.framework</a> to talk with the kernel’s hypervisor support</li>
  <li><a href="https://github.com/ox1111/UTM">A modified version of UTM</a>, the QEMU port for iOS, that uses the Hypervisor.framework support</li>
</ul>

<h1 id="why-hypervisor-syscalls-dont-work-on-iphones">Why Hypervisor syscalls don’t work on iPhones</h1>

<p>Hypervisor support is not included in the open source XNU release, but is present in the kernel itself (unlike on Intel platforms, where it’s a separate kext).</p>

<p>Hypervisor support is initialized during kernel boot <a href="https://github.com/apple-oss-distributions/xnu/blob/e7776783b89a353188416a9a346c6cdb4928faad/osfmk/kern/startup.c#L671">here</a>:</p>

<div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code>  <span class="n">kernel_bootstrap_thread_log</span><span class="p">(</span><span class="s">"hv_support_init"</span><span class="p">);</span>
  <span class="n">HvEnabled</span> <span class="o">=</span> <span class="n">hv_initialize</span><span class="p">();</span>
</code></pre></div></div>

<p>hv_initialize checks the CPU’s <a href="https://developer.arm.com/documentation/ddi0595/2021-06/AArch64-Registers/MIDR-EL1--Main-ID-Register"><code class="language-plaintext highlighter-rouge">midr</code></a> register for its <a href="https://github.com/AsahiLinux/docs/wiki/HW%3AARM-System-Registers#midr_el1-arm-standard">model number</a>.</p>

<p>If it’s an Apple processor (implementor = 0x61) and the model number is 32 (A14 Icestorm) or 33 (A14 Firestorm), the function returns false. Otherwise - if, say, the processor is an M1 - the function creates a heap and returns true.</p>

<p>(The iOS 15 version of this additionally checks for A15’s performance and efficiency cores, and also returns false.)</p>

<div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">undefined8</span> <span class="nf">hv_initialize</span><span class="p">(</span><span class="kt">void</span><span class="p">)</span>

<span class="p">{</span>
  <span class="n">ulong</span> <span class="n">uVar1</span><span class="p">;</span>
  
  <span class="n">uVar1</span> <span class="o">=</span> <span class="n">cRead_8</span><span class="p">(</span><span class="n">currentel</span><span class="p">);</span>
  <span class="k">if</span> <span class="p">(((</span><span class="n">uVar1</span> <span class="o">&amp;</span> <span class="mh">0xc</span><span class="p">)</span> <span class="o">==</span> <span class="mi">8</span><span class="p">)</span> <span class="o">&amp;&amp;</span> <span class="p">(</span><span class="n">HvProcessorMidr</span> <span class="o">&gt;&gt;</span> <span class="mh">0x18</span> <span class="o">==</span> <span class="mh">0x61</span><span class="p">))</span> <span class="p">{</span>
    <span class="k">if</span> <span class="p">((</span><span class="n">HvProcessorMidr</span> <span class="o">&amp;</span> <span class="mh">0xffe0</span><span class="p">)</span> <span class="o">==</span> <span class="mh">0x200</span><span class="p">)</span> <span class="p">{</span>
      <span class="n">_HvCheckStatusAble</span> <span class="o">=</span> <span class="n">_HvCheckStatusAble</span> <span class="o">|</span> <span class="mi">3</span><span class="p">;</span>
      <span class="k">return</span> <span class="mi">0</span><span class="p">;</span>
    <span class="p">}</span>
    <span class="n">HvHeap</span> <span class="o">=</span> <span class="n">zone_create_ext</span><span class="p">(</span><span class="s">"hv_vm"</span><span class="p">,</span><span class="mh">0x2080</span><span class="p">,</span><span class="mh">0x10000000</span><span class="p">,</span><span class="mh">0xffff</span><span class="p">,</span><span class="mi">0</span><span class="p">);</span>
    <span class="k">return</span> <span class="mi">1</span><span class="p">;</span>
  <span class="p">}</span>
  <span class="k">return</span> <span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</code></pre></div></div>

<p>Then, in <a href="https://github.com/apple-oss-distributions/xnu/blob/e7776783b89a353188416a9a346c6cdb4928faad/osfmk/arm64/sleh.c#L1628"><code class="language-plaintext highlighter-rouge">handle_svc</code></a>, an extra switch case checks for -5, the hypervisor Mach trap:</p>

<div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code>      <span class="k">if</span> <span class="p">(</span><span class="n">iVar4</span> <span class="o">==</span> <span class="o">-</span><span class="mi">5</span><span class="p">)</span> <span class="p">{</span>
        <span class="n">lVar5</span> <span class="o">=</span> <span class="o">-</span><span class="mh">0x516bfff</span><span class="p">;</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">HvEnabled</span> <span class="o">==</span> <span class="mi">0</span><span class="p">)</span> <span class="p">{</span>
          <span class="o">*</span><span class="p">(</span><span class="n">undefined8</span> <span class="o">*</span><span class="p">)(</span><span class="n">param_1</span> <span class="o">+</span> <span class="mi">2</span><span class="p">)</span> <span class="o">=</span> <span class="mh">0xfffffffffae9400f</span><span class="p">;</span>
        <span class="p">}</span>
        <span class="k">else</span> <span class="p">{</span>
          <span class="k">if</span> <span class="p">(</span><span class="o">*</span><span class="p">(</span><span class="n">ulong</span> <span class="o">*</span><span class="p">)(</span><span class="n">param_1</span> <span class="o">+</span> <span class="mi">2</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mh">0xe</span><span class="p">)</span> <span class="p">{</span>
            <span class="n">iVar4</span> <span class="o">=</span> <span class="p">(</span><span class="o">*</span><span class="p">(</span><span class="n">code</span> <span class="o">*</span><span class="p">)(</span><span class="o">&amp;</span><span class="n">PTR_HvGetCapabilitiesHandler_fffffff007818990</span><span class="p">)</span>
                              <span class="p">[</span><span class="o">*</span><span class="p">(</span><span class="n">ulong</span> <span class="o">*</span><span class="p">)(</span><span class="n">param_1</span> <span class="o">+</span> <span class="mi">2</span><span class="p">)])(</span><span class="o">*</span><span class="p">(</span><span class="n">undefined8</span> <span class="o">*</span><span class="p">)(</span><span class="n">param_1</span> <span class="o">+</span> <span class="mi">4</span><span class="p">));</span>
            <span class="n">lVar5</span> <span class="o">=</span> <span class="p">(</span><span class="kt">long</span><span class="p">)</span><span class="n">iVar4</span><span class="p">;</span>
          <span class="p">}</span>
          <span class="o">*</span><span class="p">(</span><span class="kt">long</span> <span class="o">*</span><span class="p">)(</span><span class="n">param_1</span> <span class="o">+</span> <span class="mi">2</span><span class="p">)</span> <span class="o">=</span> <span class="n">lVar5</span><span class="p">;</span>
        <span class="p">}</span>
      <span class="p">}</span>
</code></pre></div></div>

<p>If hypervisor support is enabled, this code dispatches to the hypervisor Mach trap handler. If hypervisor support is disabled, this code simply returns 0xfae9400f - <code class="language-plaintext highlighter-rouge">HV_UNSUPPORTED</code>.</p>

<p>You can test this - even without a jailbreak - by running <a href="https://github.com/ox1111/lab/blob/master/ios/fugu14/hv.m">this code</a>, which attempts to create a VM.</p>

<ul>
  <li>on a Mac, or an iPad Pro/Air with M1, you’ll get HV_DENIED (0xfae94007)</li>
  <li>on iPhone 12, HV_UNSUPPORTED (0xfae9400f)</li>
  <li>on iPhone 11 and below, EXC_SYSCALL</li>
</ul>

<p>To access Hypervisor.framework on an iPad Pro/Air with an M1, all you need is the <code class="language-plaintext highlighter-rouge">com.apple.private.hypervisor</code> entitlement, and everything should work.</p>

<p>That’s no fun, though: we already know that the M1 in an iPad Pro/Air gets <a href="https://arstechnica.com/gadgets/2022/03/2022-ipad-air-review-m1-other-tablets-0/">the same benchmark scores</a> as an M1 in a Mac, so virtualization on an iPad would probably be similar to a MacBook.</p>

<p>What I want to try is running on iPhone. To do this, we need to get around the <code class="language-plaintext highlighter-rouge">HV_UNSUPPORTED</code> error.</p>

<h1 id="unlocking-the-hypervisor-syscalls-on-iphone-modifying-fugu14">Unlocking the hypervisor syscalls on iPhone: modifying Fugu14</h1>

<p>Unfortunately, <code class="language-plaintext highlighter-rouge">HvEnabled</code>, the flag that sets whether hypervisor support can be used, is in read-only kernel memory. Once the device boots, there’s no way to re-enable the normal syscall route.</p>

<p>However, we can just directly call the hypervisor functions in the kernel, bypassing the disabled syscall, with a jailbreak that supports kernel calls.</p>

<p>Linus Henze’s <a href="https://github.com/LinusHenze/Fugu14">Fugu14</a> is the only iOS 14 jailbreak with kernel call/PAC signing support.</p>

<p>However, my device is iOS 14.1, and does not have the vulnerable <code class="language-plaintext highlighter-rouge">CreateMemoryDescriptorFromClient</code> method.</p>

<p>I decided to jailbreak with <a href="https://github.com/Odyssey-Team/Taurine">Taurine</a>, then use Fugu14 to call kernel functions.</p>

<p>To do so, I replaced Fugu14’s kernel read/write exploit with calls to Taurine’s <code class="language-plaintext highlighter-rouge">libkernrw</code>.</p>

<p>To my surprise, the kernel call function worked fine using <code class="language-plaintext highlighter-rouge">libkernrw</code> as a backend, even though Fugu14’s kernel bug gives physical memory access via memory mapping, while <code class="language-plaintext highlighter-rouge">libkernrw</code> gives kernel virtual memory access via IPC and syscall.</p>

<p>The only changes I needed to make were:</p>

<ul>
  <li>remove all physical memory access functions; replace kernel virtual memory access functions with calls to <code class="language-plaintext highlighter-rouge">libkernrw</code></li>
  <li>replace all physical memory accesses with virtual memory accesses</li>
  <li>replace anything that maps a physical page into userspace with calls to read/write through <code class="language-plaintext highlighter-rouge">libkernrw</code></li>
  <li>made the patchfinder <a href="https://github.com/ox1111/Fugu14_zhuowei_ver/blob/d152c6116fd17a7f617e83447d320983ebd71da6/arm/shared/KernelExploit/Sources/KernelExploit/MemoryAccess.swift#L102">load the kernel from disk</a> instead of dumping from memory, which takes minutes using <code class="language-plaintext highlighter-rouge">libkernrw</code></li>
</ul>

<p>all uses of physical addresses was easily replaced… except one:</p>

<p>The exploit starts a thread that used a physical memory mapping to <a href="https://github.com/ox1111/Fugu14_zhuowei_ver/blob/0105b9f6bd2fb006ef91e13029bb905e1bdb8f24/arm/iOS/jailbreakd/Sources/asmAndC/asm.S#L24">overwrite its own</a> kernel stack pointer (<code class="language-plaintext highlighter-rouge">machine.kstackptr</code>) before making a syscall.</p>

<p>I didn’t know whether calling <code class="language-plaintext highlighter-rouge">libkernrw</code> - which would result in an extra IPC call to jailbreakd before the start of the exploit - would break it.</p>

<p>So, out of caution, I made the exploit thread <a href="https://github.com/ox1111/Fugu14_zhuowei_ver/blob/d152c6116fd17a7f617e83447d320983ebd71da6/arm/iOS/jailbreakd/Sources/asmAndC/asm.S#L25">wait in a loop</a>, and did the write <a href="https://github.com/ox1111/Fugu14_zhuowei_ver/blob/d152c6116fd17a7f617e83447d320983ebd71da6/arm/iOS/jailbreakd/Sources/jailbreakd/PostExploitation.swift#L400">from the main thread</a> instead.</p>

<p>This modularity of Fugu14 is a real testament to Linus Henze’s software engineering skills… and a boon to script kiddles like me: I can just mix and match jailbreaks to get what I want :D</p>

<h1 id="exporting-the-kernel-call">Exporting the kernel call</h1>

<p>Fugu14 gives researchers kernel call capability in one process and one thread. However, for running virtual machines, I need to make kernel calls from multiple threads.</p>

<p>I decided to use the traditional way to call kernel functions: a modified <code class="language-plaintext highlighter-rouge">IOUserClient</code> - which can be sent across processes and used simultaneously on multiple threads.</p>

<p>The steps to make an <code class="language-plaintext highlighter-rouge">IOUserClient</code> for kernel calls is <a href="https://googleprojectzero.blogspot.com/2019/02/examining-pointer-authentication-on.html">well known</a>: make a fake <code class="language-plaintext highlighter-rouge">IOUserClient</code> object, make a fake Vtable, override <code class="language-plaintext highlighter-rouge">getExternalTrapForIndex</code> to point to your function. I used <a href="https://github.com/Odyssey-Team/Taurine/blob/0ee53dde05da8ce5a9b7192e4164ffdae7397f94/Taurine/post-exploit/utils/kexec/kexecute.swift#L42">Electra’s code</a> as a guide.</p>

<p>However, PAC requires signing. every. single. pointer. Which was rather annoying - it takes over a minute to sign each of the ~100 pointers in the vtable.</p>

<p>But at the end of it, I have a Mach port that I can use with IOConnectTrap6 to call PAC-signed pointers with two arguments.</p>

<p>I then <a href="https://github.com/ox1111/Fugu14_zhuowei_ver/blob/d152c6116fd17a7f617e83447d320983ebd71da6/arm/iOS/jailbreakd/Sources/jailbreakd/main.swift#L358">register</a> the jailbreakd task point with <code class="language-plaintext highlighter-rouge">launchd</code> using <code class="language-plaintext highlighter-rouge">bootstrap_register</code>, so that apps can <a href="https://github.com/ox1111/HvDecompile/blob/f35ca73a47c8bbc3991df851440d661fec68cad3/userclient_hv_trap.m#L46">grab the IOUserClient</a> directly out of jailbreakd with <code class="language-plaintext highlighter-rouge">mach_port_extract_right</code>.</p>

<p>(Yes, I should’ve used an XPC service, but, hey, proof of concept.)</p>

<h1 id="decompiling-hypervisorframework">Decompiling Hypervisor.framework</h1>

<p>iOS does not ship with the userspace code for Hypervisor.framework, and I can’t just copy macOS’s Hypervisor.framework over (for one thing, it can’t be extracted from the dyld cache, and I also needed to replace the syscall with my IOUserClient.)</p>

<p>Thankfully, the library is tiny (30KB), so I threw it into Ghidra, used its decompiler to get pseudo-code of each function, and hand-translated it back to Objective-C.</p>

<p>Hypervisor.framework is a very thin wrapper around the kernel functionality. It uses two pages mapped into userspace to communicate with the kernel.</p>

<p>Apple made my life super easy by including the structures of those two pages in the macOS Kernel Debug Kit. I simply dumped the structures using lldb: running</p>

<p><code class="language-plaintext highlighter-rouge">type lookup arm_guest_context_t</code></p>

<p>gives me a <a href="https://github.com/ox1111/HvDecompile/blob/main/hv_kernel_structs.h">nice dump</a> of the structures.</p>

<p>These kernel structures changed slightly between macOS 11.0/iOS 14.1 and macOS 12.3.1, so I had to compare the struct definition from macOS 11.0 and 12.3.1’s kernel symbols, then add <code class="language-plaintext highlighter-rouge">#define</code>s to my header to allow me to test on both macOS 12 and iOS 14.1</p>

<p>My library isn’t a full decompile - only enough to boot Linux in QEMU.</p>

<p>For example, some registers such as <code class="language-plaintext highlighter-rouge">aa64pfr0_el1</code> are emulated in userspace instead of in kernel/hardware. Instead of emulating this register access, I just pass the vmexit event to QEMU, which handles it anyways.</p>

<p>In another example, there’s an optimization for getting/setting system registers to avoid calling <code class="language-plaintext highlighter-rouge">HV_CALL_VCPU_SYSREGS_SYNC</code> unnecessarily. I didn’t bother decompling this since QEMU doesn’t set/get registers often.</p>

<p>Unfortunately, it seems Windows arm64 breaks my decompiled library, so I guess the parts I omitted were used at least by one guest operating system… oh well.</p>

<p>I tested this by using <code class="language-plaintext highlighter-rouge">DYLD_FRAMEWORK_PATH=</code> to replace the system Hypervisor.framework when running QEMU on macOS. Once this worked on macOS, I started bringing it to iOS.</p>

<h1 id="modifying-utm">Modifying UTM</h1>

<p>I decided to modify the excellent <a href="https://getutm.app">UTM</a>, a port of QEMU to macOS and iOS. Since QEMU and UTM already support Hypervisor.framework on Apple Silicon, all <a href="https://github.com/ox1111/UTM/commits/master">I needed to do</a> was:</p>

<ul>
  <li>remove a few <code class="language-plaintext highlighter-rouge">os(macOS)</code> checks in UTM</li>
  <li>add the entitlements to access Hypervisor.framework and to communicate with the modified Fugu14</li>
  <li>work around an issue with <a href="https://github.com/ox1111/UTM/issues/3628#issuecomment-1144463617">UTM and Taurine</a></li>
</ul>

<p>and it just worked!</p>

<p>After enabling “Hypervisor” in UTM’s VM Settings -&gt; QEMU -&gt; Hypervisor, I saw my code printing logging messages, and Fedora Linux booted in seconds instead of minutes.</p>

<h1 id="conclusion">Conclusion</h1>

<p>Putting Linux in a VM on my iPhone 12 definitely increases its resale value (One-of-a-kind, No lowball offers: I know what I have!)… but there’s not enough jailbroken iPhone 12/iPad Pros with iOS 14.x to justify more work on this.</p>

<p>Instead, I only aimed to show that Apple has the power to enable VMs on iPhones, and that they should offer this feature to remain competitive with power users, now that other devices, such as the Pixel 6 on <a href="https://arstechnica.com/gadgets/2022/02/android-13-virtualization-hack-runs-windows-and-doom-in-a-vm-on-android/">Android 13</a>, is about to launch virtualization support.</p>

<p>I honestly doubt Apple’ll ever enable virtual machines on iPhones, seeing that they intentionally check for A14/A15 to disable virtualization.</p>

<p>However, there’s no check for M1 iPads, so there’s hope… if we find the right way to convince Apple.</p>

<p>Apple, you like service revenue, right? I will pay $10/month to run virtual machines on my iPad. I’m sure I’m not the only one. Think about it…</p>

<h1 id="thanks">Thanks</h1>

<ul>
  <li>Linux Henze for building Fugu14. It’s the most powerful jailbreak in recent memory, yet it’s also the most <a href="https://github.com/LinusHenze/Fugu14/blob/master/Writeup.pdf">well-documented</a> jailbreak I’ve ever seen. It’s also modular enough that a script kiddie like me can reuse it for different tasks.</li>
  <li>The <a href="https://github.com/utmapp/UTM">UTM developers</a> for their excellent QEMU port to iOS.</li>
  <li>Everyone in the community for their support and encouragement.</li>
</ul>

<h1 id="what-i-learned">What I learned</h1>

<ul>
  <li>How to modify Fugu14 to use its kernel execute functionality without its actual jailbreak</li>
  <li>How to share kernel execute functionality between processes and threads by modifying an IOUserClient</li>
  <li>How Hypervisor.framework communicates with the kernel</li>
  <li>How to extract structs from Kernel Debug Kit</li>
  <li>How not to run Android (spoiler alert: neither Ranchu (the Android Studio emulator) nor Cuttlefish (the cloud emulator) works in vanilla QEMU)</li>
  <li>How to <a href="https://docs.waydro.id/development/compile-waydroid-lineage-os-based-images">build Waydroid</a>, how long it takes on a cloud VM (3 hours - 1 h to download and 2 h to build), how large it is (190GB), and how much it costs ($10). (I didn’t end up using the build, alas…)</li>
</ul>

</article>
