%define oname  flac
%define version 1.2.1
%define release %mkrel 6

%define major  8
%define libname %mklibname %{oname} %{major}

Name: xmms-flac
Summary: Xmms plugin to play FLAC files
Version:  %version
Release:  %release
License: GPLv2+
Group:  Sound
URL: http://flac.sourceforge.net/
Source: http://prdownloads.sourceforge.net/flac/flac-%{version}.tar.gz
Patch0: flac-1.2.1-gcc43.patch
Patch1: flac-1.2.1-format-strings.patch
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: xmms-devel 
BuildRequires: libogg-devel
BuildRequires: nasm
BuildRequires: libid3lib-devel
BuildRequires: gtk-devel
BuildRequires: gettext-devel
BuildRequires: automake1.8
Requires: xmms
Requires: %libname = %version
Provides: flac-xmms
Obsoletes: flac-xmms

%description
FLAC is an Open Source lossless audio codec developed by Josh Coalson.

FLAC is comprised of 1) `libFLAC', a library which implements
reference encoders and decoders, licensed under the GNU Lesser
General Public License (LGPL); 2) `flac', a command-line program for
encoding and decoding files, licensed under the GNU General public
License (GPL); 3) `metaflac', a command-line program for editing
FLAC metadata, licensed under the GPL; 4) player plugins for XMMS
and Winamp, licensed under the GPL; and 5) documentation, licensed
under the GNU Free Documentation License.


%prep
%setup -q -n %oname-%version
%autopatch -p1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
cd src/plugin_xmms/
%makeinstall_std
rm -f %buildroot%_libdir/xmms/Input/*.la

%clean
rm -rf %{buildroot}


%files
%defattr(-, root, root)
%doc AUTHORS COPYING* README
%_libdir/xmms/Input/*.so


