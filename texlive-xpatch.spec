# revision 27897
# category Package
# catalog-ctan /macros/latex/contrib/xpatch
# catalog-date 2012-03-12 18:26:56 +0100
# catalog-license lppl1.3
# catalog-version 0.2
Name:		texlive-xpatch
Version:	0.2
Release:	6
Summary:	Extending etoolbox patching commands
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xpatch
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xpatch.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xpatch.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xpatch.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package generalises the macro patching commands provided by
Philipp Lehmann's etoolbox.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/xpatch/xpatch.sty
%doc %{_texmfdistdir}/doc/latex/xpatch/README
%doc %{_texmfdistdir}/doc/latex/xpatch/xpatch.pdf
#- source
%doc %{_texmfdistdir}/source/latex/xpatch/xpatch.dtx
%doc %{_texmfdistdir}/source/latex/xpatch/xpatch.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
