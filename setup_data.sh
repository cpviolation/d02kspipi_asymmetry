#!/usr/bin/env bash
set -euo pipefail

usage() {
	echo "Usage: $0 <data_directory> [link_name]"
	echo
	echo "Create or update a symbolic link to the data directory."
	echo "  <data_directory>  Existing directory that contains the data"
	echo "  [link_name]       Symlink name/path to create (default: data)"
}

if [[ ${1:-} == "-h" || ${1:-} == "--help" ]]; then
	usage
	exit 0
fi

if [[ $# -lt 1 || $# -gt 2 ]]; then
	usage
	exit 1
fi

data_dir="$1"
link_name="${2:-data}"

if [[ ! -d "$data_dir" ]]; then
	echo "Error: '$data_dir' is not an existing directory." >&2
	exit 1
fi

# Resolve to an absolute directory path for a stable symlink target.
data_dir_abs="$(cd "$data_dir" && pwd -P)"

if [[ -e "$link_name" && ! -L "$link_name" ]]; then
	echo "Error: '$link_name' exists and is not a symbolic link." >&2
	exit 1
fi

ln -sfn "$data_dir_abs" "$link_name"

echo "Symlink created: $link_name -> $data_dir_abs"

