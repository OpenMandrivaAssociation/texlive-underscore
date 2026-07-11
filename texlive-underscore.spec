%global tl_name underscore
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Control the behaviour of _ in text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/underscore
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/underscore.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/underscore.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
With the package, \_ in text mode (i.e., \textunderscore) prints an
underscore so that hyphenation of words either side of it is not
affected; a package option controls whether an actual hyphenation point
appears after the underscore, or merely a break point. The package also
arranges that, while in text, '_' itself behaves as \textunderscore (the
behaviour of _ in maths mode is not affected).

