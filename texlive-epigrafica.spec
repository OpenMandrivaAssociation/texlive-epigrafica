%global tl_name epigrafica
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.01
Release:	%{tl_revision}.1
Summary:	A Greek and Latin font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/greek/epigrafica
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/epigrafica.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/epigrafica.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Epigrafica is forked from the development of the MgOpen font Cosmetica,
which is a similar design to Optima and includes Greek. Development has
been supported by the Laboratory of Digital Typography and Mathematical
Software, of the Department of Mathematics of the University of the
Aegean, Greece.

