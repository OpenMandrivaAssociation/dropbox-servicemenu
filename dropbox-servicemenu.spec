%define date	%(echo `LC_ALL="C" date +"%a %b %d %Y"`)
%define release %mkrel 1
%define version	0.15.4
%define name dropbox-servicemenu

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Dropbox servicemenu for Konqueror and Dolphin
Group:          Applications/Internet
License:        GPLv3+
URL:            http://kde-apps.org/content/show.php/Dropbox+ServiceMenu?content=124416
Source0:        http://kde-apps.org/CONTENT/content-files/124416-DropboxServiceMenu-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  kdebase4, desktop-file-utils
Requires:       kdebase4, xdg-utils, python-m2crypto, sqlite3-tools

%description
Dropbox ServiceMenu is a servicemenu which allows easy access to most
of Dropbox features.

%prep
%setup -q -n DropboxServiceMenu-%{version}
rm install-it.sh
rm deinstall.sh

%build
# nothing to build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_kde_services}/ServiceMenus/
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 dropbox-scripts/pyndexer.py $RPM_BUILD_ROOT%{_bindir}/pyndexer.py
install -m 755 dropbox-scripts/dropbox.py $RPM_BUILD_ROOT%{_bindir}/dropbox.py
install -m 755 dropbox-scripts/dropbox-notify.py $RPM_BUILD_ROOT%{_bindir}/dropbox-notify.py
install -m 755 dropbox-scripts/dropbox_menu.sh $RPM_BUILD_ROOT%{_bindir}/dropbox_menu.sh
install -m 755 dropbox-scripts/dropbox_menu_translations.sh $RPM_BUILD_ROOT%{_bindir}/dropbox_menu_translations.sh

install -m 644 dropbox_all.desktop $RPM_BUILD_ROOT%{_kde_services}/ServiceMenus/
install -m 644 dropbox_directories.desktop $RPM_BUILD_ROOT%{_kde_services}/ServiceMenus/
install -m 644 dropbox_files.desktop $RPM_BUILD_ROOT%{_kde_services}/ServiceMenus/


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE Changelog THANKS
%{_bindir}/pyndexer.py
%{_bindir}/dropbox.py
%{_bindir}/dropbox-notify.py
%{_bindir}/dropbox_menu.sh
%{_bindir}/dropbox_menu_translations.sh
%{_kde_services}/ServiceMenus/dropbox_all.desktop
%{_kde_services}/ServiceMenus/dropbox_directories.desktop
%{_kde_services}/ServiceMenus/dropbox_files.desktop
