#!/bin/sh
PKG=vgaswitcheroo_systemd
VER=1.2
git clone git://github.com/fredoche/${PKG}.git
cd $PKG
checkout=$(git log --pretty=format:"%adgit%h" -n1 --date=short|sed 's@-@@g')
git archive --format=tar.gz --prefix=${PKG}-${VER}-$checkout/ --output ../${PKG}-${VER}-$checkout.tar.gz master
mv -v ../${PKG}-${VER}-$checkout.tar.gz ~/rpmbuild/SOURCES
