Name:		fermilab-util_makehostkeys
Version:	1.2
Release:	1%{?dist}
Summary:	A utility for generating keytabs

License:	GPL
URL:		https://github.com/fermitools/makehostkeys

Source0:	makehostkeys

BuildRequires:	bash
BuildArch:	noarch
Requires:	krb5-workstation util-linux policycoreutils

%if 0%{?rhel} >= 8
Suggests: fermilab-conf_kerberos
%endif


%description
The makehostkeys utility has a long history at Fermilab.  It is useful
for generating the traditional host/ftp/http principle keytabs.


%prep


%build


%install
%{__install} -D %{SOURCE0} %{buildroot}%{_sbindir}/makehostkeys


%check
bash -n %{buildroot}%{_sbindir}/makehostkeys


%files
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_sbindir}/makehostkeys


%changelog
* Thu Sep 21 2023 Pat Riehecky <riehecky@fnal.gov> 1.2-1
- Run through shellcheck and shfmt

* Fri Feb 25 2022 Pat Riehecky <riehecky@fnal.gov> 1.1-1
- Move to github, bump version to note new workflows
- Add realm switch, set RPM Suggests (and dist tag)

* Wed Dec 1 2021 Pat Riehecky <riehecky@fnal.gov> 1.0-4.1
- Don't generate FTP principal by default

* Mon Nov 21 2016 Olga Terlyga <terlyga@fnal.gov> 1.0-4
- Accepted ENHC0002853

* Wed Feb 24 2016 Frank Nagy <nagy@fnal.gov> 1.0-3
- Accepted by Authentication Services

* Wed Feb 10 2016 Frank Nagy <nagy@fnal.gov> 1.0-2
- Initial review by Authentication Services

* Fri Aug 7 2015 Pat Riehecky <riehecky@fnal.gov> 1.0-1
- Updated for EL7
