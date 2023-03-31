Name:		texlive-epigrafica
Version:	17210
Release:	2
Summary:	A Greek and Latin font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/greek/epigrafica
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epigrafica.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epigrafica.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Epigrafica is forked from the development of the MgOpen font
Cosmetica, which is a similar design to Optima and includes
Greek. Development has been supported by the Laboratory of
Digital Typography and Mathematical Software, of the Department
of Mathematics of the University of the Aegean, Greece.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/epigrafica/Epigrafica-Entona.afm
%{_texmfdistdir}/fonts/afm/public/epigrafica/Epigrafica-EntonaReonta.afm
%{_texmfdistdir}/fonts/afm/public/epigrafica/Epigrafica-Ortha.afm
%{_texmfdistdir}/fonts/afm/public/epigrafica/Epigrafica-Pezokefalaia.afm
%{_texmfdistdir}/fonts/afm/public/epigrafica/Epigrafica-Reonta.afm
%{_texmfdistdir}/fonts/enc/dvips/epigrafica/epigraficahellenic.enc
%{_texmfdistdir}/fonts/map/dvips/epigrafica/epigrafica.map
%{_texmfdistdir}/fonts/tfm/public/epigrafica/epigraficab8a.tfm
%{_texmfdistdir}/fonts/tfm/public/epigrafica/epigraficab8r.tfm
%{_texmfdistdir}/fonts/tfm/public/epigrafica/epigraficabi8a.tfm
%{_texmfdistdir}/fonts/tfm/public/epigrafica/epigraficabi8r.tfm
%{_texmfdistdir}/fonts/tfm/public/epigrafica/epigraficabo8a.tfm
%{_texmfdistdir}/fonts/tfm/public/epigrafica/epigraficabo8r.tfm
%{_texmfdistdir}/fonts/tfm/public/epigrafica/epigraficac8a.tfm
%{_texmfdistdir}/fonts/tfm/public/epigrafica/epigraficac8r.tfm
%{_texmfdistdir}/fonts/tfm/public/epigrafica/epigraficahb7a.tfm
%{_texmfdistdir}/fonts/tfm/public/epigrafica/epigraficahb7r.tfm
%{_texmfdistdir}/fonts/tfm/public/epigrafica/epigraficahbi7a.tfm
%{_texmfdistdir}/fonts/tfm/public/epigrafica/epigraficahbi7r.tfm
%{_texmfdistdir}/fonts/tfm/public/epigrafica/epigraficahbo7a.tfm
%{_texmfdistdir}/fonts/tfm/public/epigrafica/epigraficahbo7r.tfm
%{_texmfdistdir}/fonts/tfm/public/epigrafica/epigraficahc7a.tfm
%{_texmfdistdir}/fonts/tfm/public/epigrafica/epigraficahc7r.tfm
%{_texmfdistdir}/fonts/tfm/public/epigrafica/epigraficahi7a.tfm
%{_texmfdistdir}/fonts/tfm/public/epigrafica/epigraficahi7r.tfm
%{_texmfdistdir}/fonts/tfm/public/epigrafica/epigraficahn7r.tfm
%{_texmfdistdir}/fonts/tfm/public/epigrafica/epigraficaho7a.tfm
%{_texmfdistdir}/fonts/tfm/public/epigrafica/epigraficaho7r.tfm
%{_texmfdistdir}/fonts/tfm/public/epigrafica/epigraficai8a.tfm
%{_texmfdistdir}/fonts/tfm/public/epigrafica/epigraficai8r.tfm
%{_texmfdistdir}/fonts/tfm/public/epigrafica/epigrafican8a.tfm
%{_texmfdistdir}/fonts/tfm/public/epigrafica/epigrafican8r.tfm
%{_texmfdistdir}/fonts/tfm/public/epigrafica/epigraficao8a.tfm
%{_texmfdistdir}/fonts/tfm/public/epigrafica/epigraficao8r.tfm
%{_texmfdistdir}/fonts/tfm/public/epigrafica/gepigraficahn7a.tfm
%{_texmfdistdir}/fonts/type1/public/epigrafica/Epigrafica-Entona.pfb
%{_texmfdistdir}/fonts/type1/public/epigrafica/Epigrafica-EntonaReonta.pfb
%{_texmfdistdir}/fonts/type1/public/epigrafica/Epigrafica-Ortha.pfb
%{_texmfdistdir}/fonts/type1/public/epigrafica/Epigrafica-Pezokefalaia.pfb
%{_texmfdistdir}/fonts/type1/public/epigrafica/Epigrafica-Reonta.pfb
%{_texmfdistdir}/fonts/vf/public/epigrafica/epigraficab8r.vf
%{_texmfdistdir}/fonts/vf/public/epigrafica/epigraficabi8r.vf
%{_texmfdistdir}/fonts/vf/public/epigrafica/epigraficabo8r.vf
%{_texmfdistdir}/fonts/vf/public/epigrafica/epigraficac8r.vf
%{_texmfdistdir}/fonts/vf/public/epigrafica/epigraficahb7r.vf
%{_texmfdistdir}/fonts/vf/public/epigrafica/epigraficahbi7r.vf
%{_texmfdistdir}/fonts/vf/public/epigrafica/epigraficahbo7r.vf
%{_texmfdistdir}/fonts/vf/public/epigrafica/epigraficahc7r.vf
%{_texmfdistdir}/fonts/vf/public/epigrafica/epigraficahi7r.vf
%{_texmfdistdir}/fonts/vf/public/epigrafica/epigraficahn7r.vf
%{_texmfdistdir}/fonts/vf/public/epigrafica/epigraficaho7r.vf
%{_texmfdistdir}/fonts/vf/public/epigrafica/epigraficai8r.vf
%{_texmfdistdir}/fonts/vf/public/epigrafica/epigrafican8r.vf
%{_texmfdistdir}/fonts/vf/public/epigrafica/epigraficao8r.vf
%{_texmfdistdir}/tex/latex/epigrafica/epigrafica.sty
%{_texmfdistdir}/tex/latex/epigrafica/lgrepigrafica.fd
%{_texmfdistdir}/tex/latex/epigrafica/ot1epigrafica.fd
%doc %{_texmfdistdir}/doc/fonts/epigrafica/README
%doc %{_texmfdistdir}/doc/fonts/epigrafica/doc.zip
%doc %{_texmfdistdir}/doc/fonts/epigrafica/epigrafica.pdf
%doc %{_texmfdistdir}/doc/fonts/epigrafica/epigrafica.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
