#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-alabama
Version  : 2023.1.0
Release  : 13
URL      : https://cran.r-project.org/src/contrib/alabama_2023.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/alabama_2023.1.0.tar.gz
Summary  : Constrained Nonlinear Optimization
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-numDeriv
BuildRequires : R-numDeriv
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Algorithm for optimizing smooth nonlinear objective functions
        with constraints. Linear or nonlinear equality and inequality
        constraints are allowed.

%prep
%setup -q -n alabama
pushd ..
cp -a alabama buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1692834926

%install
export SOURCE_DATE_EPOCH=1692834926
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/alabama/DESCRIPTION
/usr/lib64/R/library/alabama/INDEX
/usr/lib64/R/library/alabama/Meta/Rd.rds
/usr/lib64/R/library/alabama/Meta/demo.rds
/usr/lib64/R/library/alabama/Meta/features.rds
/usr/lib64/R/library/alabama/Meta/hsearch.rds
/usr/lib64/R/library/alabama/Meta/links.rds
/usr/lib64/R/library/alabama/Meta/nsInfo.rds
/usr/lib64/R/library/alabama/Meta/package.rds
/usr/lib64/R/library/alabama/NAMESPACE
/usr/lib64/R/library/alabama/NEWS
/usr/lib64/R/library/alabama/R/alabama
/usr/lib64/R/library/alabama/R/alabama.rdb
/usr/lib64/R/library/alabama/R/alabama.rdx
/usr/lib64/R/library/alabama/demo/alabama.R
/usr/lib64/R/library/alabama/help/AnIndex
/usr/lib64/R/library/alabama/help/alabama.rdb
/usr/lib64/R/library/alabama/help/alabama.rdx
/usr/lib64/R/library/alabama/help/aliases.rds
/usr/lib64/R/library/alabama/help/paths.rds
/usr/lib64/R/library/alabama/html/00Index.html
/usr/lib64/R/library/alabama/html/R.css
