@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
set SOURCEDIR=source
set BUILDDIR=build
set PYTHONWARNINGS=
:: set ALLSPHINXOPTS=-d %BUILDDIR%/doctrees %SPHINXOPTS% source
:: set SPHINXPROJ=playground

if "%1" == "" goto help

REM Check for sphinx-build
%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The Sphinx module was not found. Make sure you have Sphinx installed,
	echo.then set the SPHINXBUILD environment variable to point to the full
	echo.path of the 'sphinx-build' executable. Alternatively you may add the
	echo.Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.http://sphinx-doc.org/
	exit /b 1
)

::if "%1" == "clean" (
::	for /d %%i in (%BUILDDIR%\*) do rmdir /q /s %%i
::	del /q /s %BUILDDIR%\*
::	goto end
::)

::if "%1" == "html" (
::	%SPHINXBUILD% -b html %ALLSPHINXOPTS% %BUILDDIR%/html
::	if errorlevel 1 exit /b 1
::	echo.
::	echo.Build finished. The HTML pages are in %BUILDDIR%/html.
::	goto end
::)

::if "%1" == "doctest" (
::	%SPHINXBUILD% -b doctest %ALLSPHINXOPTS% %BUILDDIR%/doctest
::	if errorlevel 1 exit /b 1
::	echo.
::	echo.Testing of doctests in the sources finished, look at the ^
::results in %BUILDDIR%/doctest/output.txt.
::	goto end
::)

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS%
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS%

:end
popd
