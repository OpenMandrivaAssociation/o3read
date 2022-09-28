Name: o3read
Version: 0.0.4
Release: 6
Summary: Converter for OpenOffice and OpenDocument files
Group: Text tools
URL: http://siag.nu/o3read/
Source: http://siag.nu/pub/o3read/%{name}-%{version}.tar.gz
License: GPL

%description
o3read is a standalone converter for OpenOffice.org and OpenDocument
formats. It doesn't depend on OpenOffice.org or any other external 
tools or libraries. It is used by MC viewing these types of file.

%prep
%autosetup -p1

%build
%make_build

%install
%makeinstall BINDIR=%buildroot%_bindir MANDIR=%buildroot%_mandir/man1

%files
%defattr(-,root,root)
%_bindir/*
%_mandir/*/*
