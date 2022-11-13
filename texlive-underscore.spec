Name:		texlive-underscore
Version:	18261
Release:	1
Summary:	Control the behaviour of "_" in text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/underscore
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/underscore.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/underscore.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
