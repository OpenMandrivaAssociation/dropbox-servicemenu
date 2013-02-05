Name:           dropbox-servicemenu
Version:        0.16.1
Release:        2
Summary:        Dropbox servicemenu for Konqueror and Dolphin
Group:          Applications/Internet
License:        GPLv3+
#peace's latest fix
Url:            http://kde-apps.org/content/show.php/Dropbox+ServiceMenu?content=124416
Source0:        http://dl.dropbox.com/u/4127065/DropboxServiceMenu-0.16.1_peace.tar.gz
BuildArch:      noarch
BuildRequires:  kdebase4, desktop-file-utils
Requires:       kdebase4, python, xdg-utils, sqlite3-tools, klipper

%description
Dropbox ServiceMenu is a servicemenu which allows easy access to most
of Dropbox features.

%prep
%setup -q -n DropboxServiceMenu-0.16.1_peace
rm install-it.sh
rm deinstall.sh

%build
# nothing to build


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/kde4/services/ServiceMenus/
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 dropbox-scripts/pyndexer.py $RPM_BUILD_ROOT%{_bindir}/pyndexer.py
install -m 755 dropbox-scripts/dropbox.py $RPM_BUILD_ROOT%{_bindir}/dropbox.py
install -m 755 dropbox-scripts/dropbox-notify.py $RPM_BUILD_ROOT%{_bindir}/dropbox-notify.py
install -m 755 dropbox-scripts/dropbox_menu.sh $RPM_BUILD_ROOT%{_bindir}/dropbox_menu.sh
install -m 755 dropbox-scripts/dropbox_menu_translations.sh $RPM_BUILD_ROOT%{_bindir}/dropbox_menu_translations.sh

install -m 644 dropbox_all.desktop $RPM_BUILD_ROOT%{_datadir}/kde4/services/ServiceMenus/
install -m 644 dropbox_directories.desktop $RPM_BUILD_ROOT%{_datadir}/kde4/services/ServiceMenus/
install -m 644 dropbox_files.desktop $RPM_BUILD_ROOT%{_datadir}/kde4/services/ServiceMenus/


%files
%defattr(-,root,root,-)
%doc LICENSE Changelog THANKS pEACEFIX
%{_bindir}/pyndexer.py
%{_bindir}/dropbox.py
%{_bindir}/dropbox-notify.py
%{_bindir}/dropbox_menu.sh
%{_bindir}/dropbox_menu_translations.sh
%{_datadir}/kde4/services/ServiceMenus/dropbox_all.desktop
%{_datadir}/kde4/services/ServiceMenus/dropbox_directories.desktop
%{_datadir}/kde4/services/ServiceMenus/dropbox_files.desktop


%changelog

