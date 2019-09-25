Title: Cloud-free folder syncing with Unison
Tags: shell, scientific computing
Date: 2016-01-05

Syncing folders between computers can be surprisingly complicated if you
work for [an academic institution that takes a dim view of Dropbox and
other cloud-based solutions](http://www.mrc.ac.uk). You are also sure to
run out of space fast if you use it to sync e.g. neuroimaging data.
[Unison](https://www.cis.upenn.edu/~bcpierce/unison) is a free command-line
solution for direct computer-to-computer sync. It is basically a clever
wrapper around rsync, which takes care of all the niggly details of getting
two-way sync working properly. It also provides a nice command-line
interface for resolving sync conflicts (far better than e.g. Evernote's GUI
for the same thing).

Getting Unison up and running for your setup can be complicated. Here I
present a simple shell script that takes care of the standard case of
syncing two computers over SSH.

In general, my solution assumes that one computer is used to issue the
unison command (the client, which is probably your laptop or home computer)
which then connects and syncs with another computer (the remote, which is
probably a server or a desktop computer at your place of work). You could
set this up to run automatically as a cron or launchd, but I prefer to
issue the command manually at the end of the workday to make sure that I
have saved all changes first.

## Installing unison
Unison is available through various package managers, e.g. macports and
brew. The main stumbling point here is to ensure unison is available on the
remote (the computer you are syncing to). On my setup (brew with OS X
Yosemite), unison returned `bash: unison:
command not found`, even though unison was clearly availabe when connecting
to the remote over SSH. By contrast, `ssh [client] unison` returned an
error, thus revealing that unison was only getting
added to the path in interactive shells ([which are not the same as login
shells used by scripts](http://unix.stackexchange.com/questions/79723/why-do-ssh-host-echo-path-and-printing-the-path-after-sshing-into-the-machi)). In the end I manually added
/usr/local/bin to my path in .bashrc to get around this issue
(.bash_profile wouldn't work since this isn't sourced by non-interactive
shells).

## Configuring unison
The [unisync](https://gist.github.com/jooh/bbdf2b311017b3453830) script
below provides the basic sync functionality for syncing between two folders
named unibox in the user's home directory. The first input argument
specifies the hostname, while the second provides the username for the
remote. By default, the username for client and remote as assumed to be the
same.

[gist:id=bbdf2b311017b3453830]

So for instance, my standard usage is `unisync ucl j.carlin`, where ucl is
an alias or shortcut for my full SSH connection stored in ssh/.config, and
j.carlin is my username which is necessary here because it is different
from my username on the client.
