Name:		im-chooser
Version:	1.3.1
Release:	2%{?dist}
License:	GPLv2+
URL:		http://fedorahosted.org/im-chooser/
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	gtk2-devel libgnomeui-devel desktop-file-utils intltool gettext
BuildRequires:	imsettings-devel >= 0.106.0

Source0:	http://fedorahosted.org/releases/i/m/%{name}/%{name}-%{version}.tar.bz2
Patch0:		im-chooser-disable-status-icon.patch
Patch1:		im-chooser-fix-translations.patch

Summary:	Desktop Input Method configuration tool
Group:		Applications/System
Obsoletes:	system-switch-im
Requires:	imsettings >= 0.106.0

%description
im-chooser is a GUI configuration tool to choose the Input Method
to be used or disable Input Method usage on the desktop.


%prep
%setup -q
%patch0 -p1 -b .0-status-icon
%patch1 -p2 -b .1-translations

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-install --vendor=fedora                            \
        --add-category=X-GNOME-PersonalSettings                 \
        --delete-original                                       \
        --dir=$RPM_BUILD_ROOT%{_datadir}/applications           \
        $RPM_BUILD_ROOT%{_datadir}/applications/im-chooser.desktop

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT


%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f %{name}.lang
%defattr (-, root, root)
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/im-chooser
%{_datadir}/applications/fedora-im-chooser.desktop
%{_datadir}/applications/xfce4-im-chooser.desktop
%{_datadir}/icons/hicolor/*/apps/im-chooser.png


%changelog
* Tue Aug 10 2010 Akira TAGOH <tagoh@redhat.com> - 1.3.1-2
- Update translations. (#567511)

* Mon Jun 21 2010 Akira TAGOH <tagoh@redhat.com> - 1.3.1-1
- New upstream release.
  - Fallback to the themed icon if no icons are installed
    on the specified path. (#604482)

* Wed May 12 2010 Akira TAGOH <tagoh@redhat.com> - 1.3.0-1
- New upstream release.
  - GTK+ stock icon support. (#528850)

* Tue May  4 2010 Jens Petersen <petersen@redhat.com> - 1.2.7-2
- add new gnome-icon-theme style icons by Lapo Calamandrei and Jakub Steiner
  (mizmo, #587712)
- add scriptlets for icon cache

* Mon Sep 14 2009 Akira TAGOH <tagoh@redhat.com> - 1.2.7-1
- New upstream release.
  - translation updates only.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 25 2009 Akira TAGOH <tagoh@redhat.com> - 1.2.6-3
- Disable the status icon check box.

* Thu Feb 26 2009 Akira TAGOH <tagoh@redhat.com> - 1.2.6-2
- Fix a typo in xfce4-im-chooser.desktop. (#487275)

* Mon Feb 23 2009 Akira TAGOH <tagoh@redhat.com> - 1.2.6-1
- New upstream release.

* Wed Oct 22 2008 Akira TAGOH <tagoh@redhat.com> - 1.2.5-1
- New upstream release.

* Tue Oct 14 2008 Akira TAGOH <tagoh@redhat.com> - 1.2.4-1
- New upstream release.

* Wed Sep 17 2008 Akira TAGOH <tagoh@redhat.com> - 1.2.3-1
- New upstream release.

* Fri Aug 29 2008 Akira TAGOH <tagoh@redhat.com> - 1.2.2-1
- New upstream release.

* Tue Jul 29 2008 Akira TAGOH <tagoh@redhat.com> - 1.2.1-1
- New upstream release.
  - Display IM icon in the list. (#454371)

* Tue Jul  8 2008 Akira TAGOH <tagoh@redhat.com> - 1.2.0-1
- New upstream release.

* Fri Jun 27 2008 Akira TAGOH <tagoh@redhat.com> - 1.1.1-1
- New upstream release.
  - Fix a segfault when no Input Method installed. (#452997)

* Thu Jun 12 2008 Akira TAGOH <tagoh@redhat.com> - 1.1.0-1
- New upstream release.

* Mon May 26 2008 Akira TAGOH <tagoh@redhat.com> - 0.99.6-5
- Fix a typo in the package group of imsettings-xfce. (#448037)

* Wed May 14 2008 Akira TAGOH <tagoh@redhat.com> - 0.99.6-4
- im-chooser-fix-window-border.patch: Display the progress window with
  the certain window border. (#444818)
- imsettings-ignore-error-on-check-running.patch: Fix a crash issue when
  the pidfile doesn't exist. (#445129)

* Tue Apr 29 2008 Akira TAGOH <tagoh@redhat.com> - 0.99.6-3
- im-chooser-0.99.6-sanity-check-on-dbus-conn.patch: Do not abort even if
  getting the bus is failed. (#444494)
- im-chooser-0.99.6-validate-pid.patch: Validate the pid. (#443765)

* Wed Apr 23 2008 Akira TAGOH <tagoh@redhat.com> - 0.99.6-2
- im-chooser-0.99.6-check-if-im-is-running.patch: Do not turn on the check box
  if IM isn't really running. (#443765)
- im-chooser-0.99.6-correct-build-order.patch: Apply to correct the build order.

* Tue Apr  8 2008 Akira TAGOH <tagoh@redhat.com> - 0.99.6-1
- New upstream release.
  - translation updates.
- Remove unnecessary patches:
  - im-chooser-0.99.5-no-xinputrc-update.patch
  - im-chooser-0.99.5-no-crash-on-no-im.patch

* Mon Apr  7 2008 Akira TAGOH <tagoh@redhat.com> - 0.99.5-3
- im-chooser-0.99.5-no-crash-on-no-im.patch: Fix a crash when no IM
  available. (#440519)
- Invoke ReloadConfig to apply changes on DBus services in %%post and %%postun.

* Fri Mar 28 2008 Akira TAGOH <tagoh@redhat.com> - 0.99.5-2
- im-chooser-0.99.5-no-xinputrc-update.patch: real fix for #437732
- ensure invoking xinput.sh after the session bus is established. (#436284)

* Wed Mar 19 2008 Akira TAGOH <tagoh@redhat.com> - 0.99.5-1
- New upstream release.
  - Fix an issue always create .xinputrc at the startup time. (#437732)
  - Add Xfce support.

* Tue Mar 11 2008 Akira TAGOH <tagoh@redhat.com> - 0.99.4-1
- New upstream release.
  - Compress im-chooser.png icon. (#330441)

* Thu Feb 21 2008 Akira TAGOH <tagoh@redhat.com>
- Run ldconfig on scriptlet of imsettings-libs.

* Wed Feb 20 2008 Akira TAGOH <tagoh@redhat.com> - 0.99.3-1
- New upstream release.
  - Fix taking too much CPU power. (#433575)
  - Fix not parsing the multiple command line options in xinput
    script. (#433578)

* Tue Feb 19 2008 Akira TAGOH <tagoh@redhat.com> - 0.99.2-1
- New upstream release.
  - Fix not working the user own .xinputrc properly.

* Fri Feb  8 2008 Akira TAGOH <tagoh@redhat.com> - 0.99.1-1
- New upstream release.
  - Fix some memory leaks and clean up the code. (#431167)
  - Fix the handling of the user own .xinputrc. (#431291)

* Fri Feb  1 2008 Akira TAGOH <tagoh@redhat.com> - 0.99-1
- New upstream release.
  - IMSettings is now enabled. you don't need to restart your desktop after
    changing IM for GTK+ applications. but still need to do for others so far.

* Thu Dec 27 2007 Akira TAGOH <tagoh@redhat.com> - 0.5.5-1
- New upstream release.
  - Rename sr@Latn to sr@latin. (#426540)

* Fri Nov 16 2007 Akira TAGOH <tagoh@redhat.com> - 0.5.4-1
- New upstream release.
  - Improve .desktop file for GNOME HIG compliant (#330431)
  - Improve English label on GUI (#302491)
- Remove the dead link. (#330391)
- Improve a package description. (#330421)

* Mon Oct 15 2007 Akira TAGOH <tagoh@redhat.com>
- Remove the obsolete Norwegian (no) translation. (#332131)

* Thu Oct 11 2007 Akira TAGOH <tagoh@redhat.com> - 0.5.3-1
- New upstream release.
  - Fix an issue that looks like IM can't be disabled on im-chooser. (#324231)

* Tue Oct  2 2007 Akira TAGOH <tagoh@redhat.com> - 0.5.2-3
- Revert the previous change.

* Fri Sep 21 2007 Akira TAGOH <tagoh@redhat.com> - 0.5.2-2
- Bring up IM by default again, except the session is on Live CD. (#250226)

* Tue Sep 18 2007 Akira TAGOH <tagoh@redhat.com> - 0.5.2-1
- New upstream release.
  - Fix to allow users disabling IM.

* Fri Sep 14 2007 Akira TAGOH <tagoh@redhat.com> - 0.5.1-2
- Add README into the package.

* Mon Sep 10 2007 Akira TAGOH <tagoh@redhat.com> - 0.5.1-1
- New upstream release.

* Thu Sep  6 2007 Akira TAGOH <tagoh@redhat.com> - 0.5.0-1
- New upstream release.

* Wed Aug  8 2007 Akira TAGOH <tagoh@redhat.com>
- Update License tag.

* Mon Aug  6 2007 Akira TAGOH <tagoh@redhat.com> - 0.4.1-3
- Own /etc/X11/xinit/xinput.d (#250960)

* Mon Jul 30 2007 Akira TAGOH <tagoh@redhat.com> - 0.4.1-2
- Update Require for xorg-x11-xinit

* Wed Jul 25 2007 Akira TAGOH <tagoh@redhat.com> - 0.4.1-1
- New upstream release.
  - xinput.sh has been moved from xorg-x11-xinit.

* Tue Jan 30 2007 Akira TAGOH <tagoh@redhat.com> - 0.3.4-1
- Translations update release.

* Wed Jan 24 2007 Matthias Clasen <mclasen@redhat.com> - 0.3.3-3
- Add X-GNOME-PersonalSettings to the desktop file categories (#224159)
- Use desktop-file-install

* Mon Oct  2 2006 Akira TAGOH <tagoh@redhat.com> - 0.3.3-2
- added Assamese, Greek and Marathi translation. (#208258)

* Mon Oct  2 2006 Akira TAGOH <tagoh@redhat.com> - 0.3.3-1
- Translations update release. (#208258, #208512)

* Fri Sep  8 2006 Akira TAGOH <tagoh@redhat.com> - 0.3.2-1
- New upstream release.
  - added an icon. (#199337)
- removed the unnecessary patches:
  - im-chooser-r49.patch
  - im-chooser-r53.patch

* Tue Aug 29 2006 Akira TAGOH <tagoh@redhat.com> - 0.3.1-3
- im-chooser-r53.patch: take care of the suffix to appears current selection.
  (#204433)

* Fri Aug 25 2006 Akira TAGOH <tagoh@redhat.com> - 0.3.1-2
- im-chooser-r49.patch: removed MimeType field from .desktop file. (#203982)

* Tue Aug 15 2006 Akira TAGOH <tagoh@redhat.com> - 0.3.1-1
- New upstream release.

* Mon Jul 24 2006 Akira TAGOH <tagoh@redhat.com> - 0.3.0-2
- New upstream release.
- add libgnomeui-devel to BR.
- im-chooser-suffix-r40.patch: applied to support the recent change
  in the xinput files.

* Thu Jul 20 2006 Akira TAGOH <tagoh@redhat.com> - 0.2.2-2
- rebuilt

* Wed Jul 12 2006 Akira TAGOH <tagoh@redhat.com> - 0.2.2-1
- New upstream release.

* Mon Jul 10 2006 Akira TAGOH <tagoh@redhat.com> - 0.2.1-3
- New upstream release.
- improved the package summary and description.
- added intltool to BuildReq.
- added gettext to BuildReq.

* Fri Jul  7 2006 Akira TAGOH <tagoh@redhat.com> - 0.2.0-1
- New upstream release.
- use dist tag.
- registered xinputrc alternatives for none and xim.
- removed the empty docs.
- add Requires: xorg-x11-xinit >= 1.0.2-5.fc6 for new xinput.sh.

* Wed Jun  7 2006 Akira TAGOH <tagoh@redhat.com> - 0.1.1-1
- Initial package.

