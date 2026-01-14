# Portage

Core of the gentoo operating system
Main commands
- `emerge`
- `emaint`
- `dispatch-conf`
Others
- `archive-conf`, `ebuild`, `egencache`, `emerge-webrsync`, `emirrordist`, `env-update`, `etc-update`, `fixpackages`, `glsa-check`, `gpkg-sign`, `portageq`, `quickpkg`, `regenworld`, `repoman`
## ebuild Repository
File structure that can provide packages for installation
[Gentoo ebuild repository](https://gitweb.gentoo.org/repo/gentoo.git/tree)
[Project:GURU ebuild repository](https://gitweb.gentoo.org/repo/proj/guru.git)
Sync between daily and weekly
Last time Gentoo ebuild repository was synchronized: `/var/db/repos/gentoo/metadata/timestamp.chk`
## Emerge
Main CLI interface to portage with many uses
### Installing Packages
Emerge installs packages by default
Flags
- a = ask
- v = verbose
- p = pretend
- t = tree (show dependency tree)
Calculating dependencies
- U = upgraded
- D = downgraded
- R = re-emerged
- N = new package
`--resume` - resumes previously failed installation from the package it failed on
`--oneshot (-1)` - install a package without adding it to the @world set
`--with-bdeps=y` - also update build dependencies
### Search Packages
`--search (-s)` - can use regular expressions
`--searchdesc`
### Uninstall Packages
`--depclean (-c)`
Use the -a and -p flags to preview what will be removed
Use --noreplace to specify packages that should not be removed
`--unmerge (-C)` - unsafe way to remove packages
### Get System Info
`emerge --info`
### Updating world set
i.e. update all packages in the world set
`emerge -avuDN @world`
Use U instead of N to skip some packages where the only changes are USE flags added to or dropped from the repo
## `emaint`
Sync ebuild repositories
`emerge --sync` = `emaint sync --auto` (sync all repos with are configured with auto sync in `/etc/portage/repos.conf`)
`emaint sync --allrepos` (sync repos regardless of auto sync)
Be sure to run `emerge --regen` to regenerate the metadata cache to speed up dependency resolution
`emerge-webrsync` - downloads recent snapshot of Gentoo repository that's at most one day old
`eix-sync` - sync repos and also update cache used by eix
## `dispatch-conf`
Manage configuration files after updates
Add `diff="diff --color=always -Nu '%s' '%s'"` to `/etc/dispatch-conf.conf` for color diffing
Add `merge="nvim -d -c'saveas %s' -c next -c'setlocal noma readonly' -c prev %s %s"` to `/etc/dispatch-conf.conf` to use NeoVim to merge files
## Profiles
Default state of use flags and all variables found in `/etc/portage/make.conf`
Defines a `@system` set
## Package Sets
Lists of packages used by Portage
- `@system` and `@profile` - Defined by Gentoo development team as packages that are required for the base system
- `@selected*` - all packages that have been intentionally installed
- `@world`- Everything
`emerge --list-sets` - list packages sets

# Gentoolkit
Suite of tools for making Gentoo (mostly Portage) easier to administer
Some of the more useful tools
- `eclean` - Remove old source files and binary packages to free space
- `equery` - Display package dependencies, metadata, and installed files
- `eread`- Display elog files from Portage
    - Must setup `/etc/portage/make.conf` first
- `euse` - Get/set info about USE flags in make.conf without having to open the file directly
# `eix`
Faster alternative to emerge --search
Caveat: depends on a binary cache that has to be updated (`eix-update`) after every Portage sync
`eix [--compact] @<set>` - show package listings for system, selected, or world package sets
Look up how to run `eix-update` automatically after each sync
Other commands
- `eix-update`
- `eix-sync`
- `eix-remote`
Configure eix to update after each portage sync. Add script to `/etc/portage/postsync.d` directory and it will be automatically executed with Portage's postsync hook
```bash
#!/usr/bin/env bash
if [[ -e /var/cache/eix/portage.eix ]]; then
    rsync -ca /var/cache/eix/portage.eix /var/cache/eix/previous.eix;
fi
eix-update
if [[ -e /var/cache/eix/previous.eix ]]; then
    eix-diff;
fi
```
Be sure to `chmod +x` the file
# `eselect`
Tool for administering a Gentoo system (switching profiles, kernels, reading news, etc)
# PFL (Portage File List)

- `e-file <file>` - search for packages that will install the specified file
- `pfl` - send updates to the PFL website
# `genlop`
Portage installation logs
`genlop -l` - recent emerges
`genlop -t <package>` - how long an emerge took
`genlop -pU @world` - estimate how long `emerge -uND --with-bdeps=y @world` will take
`watch genlop -unc` - watch latest merging ebuild during an upgrade
# Overlays (ebuild repositories??)
Install `app-eselect/eselect-repository`
`eselect repository list` - list all available overlays
`eselect repository list -i` - list all installed overlays
# Listing packages
`qlist -IRv` - list installed packages with version number and name of overlay
`eix --world --color -c | less -R` - view packages in world set
`glsa-check --test all` - test against some security vulnerabilities
`equery list '*'`
`equery d <package>` - list packages that depend on a package
`eix <package>` - get information about a package

TL;DR
- Run `emaint sync --allrepos` often
- Run `emerge --regen` to update metadata caches
- Run `emerge -avuDN @world` to ensure everything is up to date
# Personal modifications
- Install zsh
- set -o vi
- alias l=ls -lA
- tmux, set vi keys for copy mode
- Neovim with LazyVim