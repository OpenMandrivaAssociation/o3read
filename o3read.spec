%define name o3read
%define version 0.0.4
%define release %mkrel 3

Name: %{name}
Version: %{version}
Release: %{release}
Summary: Converter for OpenOffice and OpenDocument files
Group: Text tools
URL: http://siag.nu/o3read/
Source: http://siag.nu/pub/o3read/%{name}-%{version}.tar.bz2
License: GPL
BuildRoot: %{_tmppath}/%{name}-root

%description
o3read is a standalone converter for OpenOffice.org and OpenDocument
formats. It doesn't depend on OpenOffice.org or any other external 
tools or libraries. It is used by MC viewing these types of file.

%prep
%setup -q

%build
%make

%install
rm -rf %buildroot
%makeinstall BINDIR=%buildroot%_bindir MANDIR=%buildroot%_mandir/man1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%_bindir/*
%_mandir/*/*


