with import <nixpkgs> {};
{
  primeDiceBot = stdenv.mkDerivation {
    name = "primeDiceBot";
    buildInputs = [
      pythonFull
      python27Packages.requests
    ];

  LC_CTYPE="en_US.UTF-8";
  LANG="en_US.UTF-8";
  LOCALE_ARCHIVE = "${pkgs.glibcLocales}/lib/locale/locale-archive";
  
  shellHook = ''
        unset http_proxy
        export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
        export GIT_SSL_CAINFO=/etc/ssl/certs/ca-certificates.crt
    '';
  };
}
