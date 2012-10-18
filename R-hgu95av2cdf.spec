%define		packname	hgu95av2cdf

Summary:	HG_U95Av2.CDF data file
Name:		R-%{packname}
Version:	2.11.0
Release:	1
Group:		Applications/Engineering
License:	LGPL v2+
Source0:	http://www.bioconductor.org/packages/release/data/annotation/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	678ed562ed394d8a967501e840747a40
URL:		http://www.bioconductor.org/packages/release/data/annotation/html/hgu95av2cdf.html
BuildRequires:	R-AnnotationDbi
BuildRequires:	R
BuildRequires:	texlive-latex
Requires:	R-AnnotationDbi
Requires:	R
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Environment representing the HG_U95Av2.CDF file.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}/
%doc %{_libdir}/R/library/%{packname}/html/
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/Meta/
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/R/
%{_libdir}/R/library/%{packname}/help/
%{_libdir}/R/library/%{packname}/data/
