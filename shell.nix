{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python311
    python311Packages.sqlalchemy
    python311Packages.faker
    python311Packages.pytest
  ];

  shellHook = ''
    echo "Spotify App Dev Environment Ready"
    pytest
  '';
}

