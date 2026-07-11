%global tl_name xpatch
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	Extending etoolbox patching commands
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xpatch
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xpatch.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xpatch.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xpatch.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(etoolbox)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package generalises the macro patching commands provided by Philipp
Lehmann's etoolbox.

