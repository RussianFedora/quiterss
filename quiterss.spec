Name:           quiterss
Version:        0.10.1
Release:        1%{?dist}
Summary:        RSS/Atom feed reader written on Qt
Summary(ru):    QuiteRSS - быстрая и удобная программа для чтения новостных лент RSS/Atom

License:        GPLv3
URL:            http://code.google.com/p/quite-rss/
Source0:        http://quite-rss.googlecode.com/files/QuiteRSS-%{version}-src.tar.gz

BuildRequires:  qt-devel >= 4.7
BuildRequires:  qtwebkit-devel
BuildRequires:  pkgconfig


%description
Quite fast and comfortable to user RSS/Atom feed reader written on Qt.

%description -l ru
Быстрая и удобная программа для чтения новостных лент RSS/Atom, написанная
на Qt.

%prep
%setup -q -n QuiteRSS-%{version}-src
chmod -x AUTHORS COPYING README


%build
lrelease-qt4 QuiteRSS.pro
qmake-qt4
make %{?_smp_mflags}


%install
make install INSTALL_ROOT=%{buildroot}

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
%{_datadir}/%{name}


%changelog
* Tue Aug 21 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.10.1-1.R
- update to 0.10.1
- added gtk-update-icon-cache

* Sun Aug 12 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.10.0-1.R
- update to 0.10.0

* Tue Jun 19 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.9.1-1.R
- initial build