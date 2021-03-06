Summary:	Fast and lightweight IDE using GTK+
Name:		geany
Version:	1.24.1
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://download.geany.org/%{name}-%{version}.tar.bz2
# Source0-md5:	d225104cef3973164d70116d46239606
URL:		http://www.geany.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	hicolor-icon-theme
Suggests:	vte2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Geany is a small and lightweight integrated development environment.
It was developed to provide a small and fast IDE, which has only a few
dependencies from other packages. Another goal was to be as
independent as possible from a special Desktop Environment like KDE or
GNOME.

%package devel
Summary:	Geany Development files
Group:		Development/Libraries
Requires:	gtk+-devel

%description devel
Geany Development files.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/geany/*.la
rm -f $RPM_BUILD_ROOT%{_docdir}/geany/{AUTHORS,COPYING,ChangeLog,NEWS,README,THANKS,TODO,ScintillaLicense.txt}
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{lb,pt_PT}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_desktop_database

%postun
%update_icon_cache hicolor
%update_desktop_database

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO scintilla/License.txt
%dir %{_docdir}/geany
%dir %{_libdir}/geany

%attr(755,root,root) %{_bindir}/geany
%attr(755,root,root) %{_libdir}/geany/*.so

%{_datadir}/%{name}
%{_desktopdir}/geany.desktop
%{_iconsdir}/hicolor/*/actions/*.png
%{_iconsdir}/hicolor/*/actions/*.svg
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.svg

%{_docdir}/geany/html
%{_docdir}/geany/manual.txt
%{_mandir}/man1/geany.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/geany
%{_pkgconfigdir}/*.pc

