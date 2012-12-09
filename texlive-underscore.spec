# revision 18261
# category Package
# catalog-ctan /macros/latex/contrib/underscore
# catalog-date 2010-06-07 08:23:51 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-underscore
Version:	20100607
Release:	2
Summary:	Control the behaviour of "_" in text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/underscore
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/underscore.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/underscore.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
With the package, \_ in text mode (i.e., \textunderscore)
prints an underscore so that hyphenation of words either side
of it is not affected; a package option controls whether an
actual hyphenation point appears after the underscore, or
merely a break point. The package also arranges that, while in
text, '_' itself behaves as \textunderscore (the behaviour of _
in maths mode is not affected.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/underscore/underscore.sty
%doc %{_texmfdistdir}/doc/latex/underscore/miscdoc.sty
%doc %{_texmfdistdir}/doc/latex/underscore/underscore.pdf
%doc %{_texmfdistdir}/doc/latex/underscore/underscore.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100607-2
+ Revision: 757284
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100607-1
+ Revision: 719847
- texlive-underscore
- texlive-underscore
- texlive-underscore

