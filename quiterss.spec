Name:           quiterss
Version:        0.12.3
Release:        1%{?dist}
Summary:        RSS/Atom feed reader written on Qt
Summary(ru):    QuiteRSS - быстрая и удобная программа для чтения новостных лент RSS/Atom

License:        GPLv3
URL:            http://code.google.com/p/quite-rss/
Source0:        http://quite-rss.googlecode.com/files/QuiteRSS-%{version}-src.tar.bz2
Patch0:         quiterss-el6-compile.patch

BuildRequires:  qt-devel
BuildRequires:  qtwebkit-devel
BuildRequires:  pkgconfig
BuildRequires:  desktop-file-utils


%description
Quite fast and comfortable to user RSS/Atom feed reader written on Qt.

%description -l ru
Быстрая и удобная программа для чтения новостных лент RSS/Atom, написанная
на Qt.

%prep
%setup -q -n QuiteRSS-%{version}-src
#%if %{defined rhel} && 0%{?rhel} < 7
#%patch0 -p1 -b .el6-compile
#%endif
chmod -x AUTHORS COPYING README


%build
lrelease-qt4 QuiteRSS.pro
qmake-qt4
make %{?_smp_mflags}


%install
make install INSTALL_ROOT=%{buildroot}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache -f %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache -f %{_datadir}/icons/hicolor &>/dev/null || :


%files
%doc AUTHORS COPYING README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}


%changelog
* Mon Mar 18 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 0.12.3-1.R
- update to 0.12.3

* Thu Mar 14 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 0.12.2-1.R
- update to 0.12.2

* Fri Sep 21 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.10.2-1.R
- update to 0.10.2

* Wed Aug 22 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.10.1-2.R
- added patch for compile in el6

* Tue Aug 21 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.10.1-1.R
- update to 0.10.1
- added gtk-update-icon-cache

* Sun Aug 12 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.10.0-1.R
- update to 0.10.0

* Tue Jun 19 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.9.1-1.R
- initial build