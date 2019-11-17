Name:			  redis
Summary:		Redis cluster server
Version:		5.0.4
Release:		1%{?dist}
License:		CPL
Group:			DX
URL:			  https://redis.io/
Source:			http://download.redis.io/releases/redis-5.0.4.tar.gz

%description
Redis is redis cluster package

%prep
%setup -q -n %{name}-%{version}

%install
make -j8
mkdir -p $RPM_BUILD_ROOT/usr/bin
cp %{_topdir}/BUILD/%{name}-%{version}/src/redis-server $RPM_BUILD_ROOT/usr/bin
cp %{_topdir}/BUILD/%{name}-%{version}/src/redis-cli $RPM_BUILD_ROOT/usr/bin
cp %{_topdir}/BUILD/%{name}-%{version}/src/redis-sentinel $RPM_BUILD_ROOT/usr/bin
cp %{_topdir}/BUILD/%{name}-%{version}/src/redis-check-rdb $RPM_BUILD_ROOT/usr/bin
cp %{_topdir}/BUILD/%{name}-%{version}/src/redis-check-aof $RPM_BUILD_ROOT/usr/bin
    
mkdir -p $RPM_BUILD_ROOT/etc/redis
cp %{_topdir}/BUILD/%{name}-%{version}/rpm/*.conf $RPM_BUILD_ROOT/etc/redis

mkdir -p $RPM_BUILD_ROOT/usr/lib/systemd/system
cp %{_topdir}/BUILD/%{name}-%{version}/rpm/redis-server@.service $RPM_BUILD_ROOT/usr/lib/systemd/system

%clean

%preun
for svc in `systemctl list-units -t service |grep "redis-server@" | awk ' { print $1 } '`; do
	systemctl disable $svc
	systemctl stop $svc
done

%postun

%post
mkdir -p /var/log/redis

%pre


%files
%dir %attr(755, root, root)
%{_bindir}/*
/etc/redis/*
/usr/lib/systemd/system/*

%changelog
* Tue Apr 2 2019 Samuel Chen
- initial file created
