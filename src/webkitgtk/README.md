

## how to install

```shell
 sudo dnf --disablerepo='*' --enablerepo=copr:copr.fedorainfracloud.org:ttys3:my-fedora-packages reinstall webkitgtk6.0
```

## legacy versions

we can not remove 4.0 on destktop env now, because:

```shell
❯ sudo dnf list --installed | rg webkit2gtk4.0
webkit2gtk4.0.x86_64                                   2.42.1-1.fc39                              @fedora                                                 
webkit2gtk4.0-devel.x86_64                             2.42.1-1.fc39                              @fedora                                                 
  VPN🟢[ github.com/ttys3/my-fedora-packages]☸ eks-test (im) in ~/repo/fedora/my-fedora-packages/src/webkitgtk on  main [?] 
❯ sudo dnf remove webkit2gtk4.0 webkit2gtk4.0-devel
Dependencies resolved.
===============================================================================================================================
 Package                                 Architecture        Version                       Repository                     Size
===============================================================================================================================
Removing:
 webkit2gtk4.0                           x86_64              2.42.1-1.fc39                 @fedora                        75 M
 webkit2gtk4.0-devel                     x86_64              2.42.1-1.fc39                 @fedora                       5.2 M
Removing dependent packages:
 ulauncher                               noarch              5.15.4-1.fc39                 @updates-testing              6.3 M
 wxGTK-devel                             x86_64              3.2.2.1-5.fc39                @fedora                        74 k
Removing unused dependencies:
 javascriptcoregtk4.0                    x86_64              2.42.1-1.fc39                 @fedora                        28 M
 javascriptcoregtk4.0-devel              x86_64              2.42.1-1.fc39                 @fedora                       753 k
 python3-Levenshtein                     x86_64              0.21.0-3.fc39                 @fedora                       429 k
 python3-inotify                         noarch              0.9.6-32.fc39                 @fedora                       302 k
 wmctrl                                  x86_64              1.07-35.fc39                  @fedora                        66 k
 wxBase-devel                            x86_64              3.2.2.1-5.fc39                @fedora                       6.7 M
 wxGTK-gl                                x86_64              3.2.2.1-5.fc39                @fedora                       111 k
 wxGTK-media                             x86_64              3.2.2.1-5.fc39                @fedora                       144 k
 wxGTK-webview                           x86_64              3.2.2.1-5.fc39                @fedora                       205 k

Transaction Summary
===============================================================================================================================
Remove  13 Packages

Freed space: 123 M
Is this ok [y/N]: 
```