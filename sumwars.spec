#
# TODO: create ~/.sumwars/save directory and use it to store saved games
#
%define		svn_rev	2169
Summary:	An open source role-playing game
Summary(pl.UTF-8):	Otwarta gra typu RPG
Name:		sumwars
Version:	%{svn_rev}
Release:	0.svn.1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	%{name}-%{version}-svn.tar.gz
# Source0-md5:	cf169a6f0c285d05dba490a80d164ef4
Patch0:		%{name}-paths.patch
URL:		http://www.sumwars.org/
BuildRequires:	CEGUI-Ogre >= 0.7.0
BuildRequires:	OpenAL-devel
BuildRequires:	cmake >= 2.6.0
BuildRequires:	enet-devel >= 1.2
BuildRequires:	freealut-deve
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	lua51-devel
BuildRequires:	ogre-devel >= 1.7.0
BuildRequires:	rpmbuild(macros) >= 1.566
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Summoning Wars is an open source role-playing game, featuring both a
single-player and a multiplayer mode for about 2 to 8 players.

%description -l pl.UTF-8
Summoning Wars jest otwartą grą typu RPG, umożliwiającą grę jednemu
graczowi jak również grę sieciową pozwalającą na grę od 2 do 8 graczy.

%prep
%setup -q -n %{name}
%undos src/gui/application.cpp
%patch0 -p1
%{__sed} -i 's,./resources,resources,;s,./data,data,' resources.cfg

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/games/%{name}}

install build/sumwars $RPM_BUILD_ROOT%{_bindir}
install ogre.cfg plugins.cfg resources.cfg $RPM_BUILD_ROOT%{_datadir}/games/%{name}
install authors.txt $RPM_BUILD_ROOT%{_datadir}/games/%{name}
cp -r resources data $RPM_BUILD_ROOT%{_datadir}/games/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/sumwars
%{_datadir}/games/%{name}
