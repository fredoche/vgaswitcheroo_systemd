%global checkout 20130311gitf52fa0d

Name:		vgaswitcheroo_systemd
Version:	1.2
Release:	1.%{checkout}%{?dist}
Summary:	Deactivate discrete graphic adapter on startup

Group:		System Environment/Daemons
License:	GPLv3+
URL:		https://github.com/fredoche/%{name}
Source0:	%{name}-%{version}-%{checkout}.tar.gz
#Source0-generating script
Source1:	%{name}-get-snapshot.sh
Requires:	systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
BuildArch:	noarch

%description
You just bought a shiny new laptop with dual graphics adapter
and want to use a Linux distro with it. Luckily, you can use 
the vgaswitcheroo kernel module to manage the power issues, 
however you'd like to save power and save yourself trouble by 
automatically disabling the discrete adapter on startup. 
If your distribution uses systemd as init daemon, you can use 
these pretty simple files to solve this problem

%prep
%setup -q -n %{name}-%{version}-%{checkout}

%build

%install
install -Dm755 vgaswitcheroo_start.sh %{buildroot}%{_bindir}/vgaswitcheroo_start.sh
install -m755 vgaswitcheroo_stop.sh %{buildroot}%{_bindir}
install -Dm644 vgaswitcheroo.service %{buildroot}%{_unitdir}/vgaswitcheroo.service

%post
%systemd_post vgaswitcheroo.service

%preun
%systemd_preun vgaswitcheroo.service

%postun
%systemd_postun vgaswitcheroo.service

%files
%doc README.md
%{_bindir}/vgaswitcheroo_start.sh
%{_bindir}/vgaswitcheroo_stop.sh
%{_unitdir}/vgaswitcheroo.service

%changelog
* Sun Jun 2 2013 Simone Sclavi <darkhado@gmail.com> 1.2-1.20130311gitf52fa0d
- Initial build
