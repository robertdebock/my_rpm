Name: my
Version: 1.0.0
Release: 0
Summary: An RPM to see if building works.
License: Apache
Group: Productivity
URL: https://robertdebock.nl/
Source: https://github.com/robertdebock/my_rpm/blob/master/SOURCES/my-1.0.0.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Build a mock RPM.

%prep
%setup -q

%build
%configure
%install

install -D -m 755 %{SOURCE}/my.a %{buildroot}/bin/my

%files
%defattr(-,root,root,-)
/bin/my

%changelog
