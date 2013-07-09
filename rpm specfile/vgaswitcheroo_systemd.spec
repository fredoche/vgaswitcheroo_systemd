%global checkout 20130708gite5cd187

Name:		vgaswitcheroo_systemd
Version:	1.3
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
these pretty simple files to solve this problem.

%prep
%setup -q -n %{name}-%{version}-%{checkout}

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
* Mon Jul 08 2013 Simone Sclavi <darkhado@gmail.com> 1.3-1.20130708gite5cd187
- Update to release 1.3

* Thu Jun 27 2013 Simone Sclavi <darkhado@gmail.com> 1.2-2.20130311gitf52fa0d
- Fixed License

* Sun Jun 02 2013 Simone Sclavi <darkhado@gmail.com> 1.2-1.20130311gitf52fa0d
- Initial build
