Name:		vgaswitcheroo_systemd
Version:	1.3
Release:	1%{?dist}
Summary:	Deactivate discrete graphic adapter on startup

Group:		System Environment/Daemons
License:	GPLv3+
URL:		https://github.com/fredoche/%{name}
Source0:	https://github.com/fredoche/%{name}/archive/master.zip
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
these pretty simple files to solve this problem.

%prep
%setup -q -n %{name}-master

%build

%install
install -Dm644 vgaswitcheroo.service %{buildroot}%{_unitdir}/vgaswitcheroo.service

%post
%systemd_post vgaswitcheroo.service

%preun
%systemd_preun vgaswitcheroo.service

%postun
%systemd_postun vgaswitcheroo.service

%files
%doc README.md LICENSE
%{_unitdir}/vgaswitcheroo.service

%changelog
* Tue Jul 09 2013 Simone Sclavi <darkhado@gmail.com> 1.3-1
- Initial build
