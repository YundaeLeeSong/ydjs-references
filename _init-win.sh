#!/usr/bin/env bash
set -euo pipefail


gitignore_folder=".gitignores"
license_folder="LICENSEs"

rm -rf $gitignore_folder
rm -rf $license_folder


# by the system, get year of today, also, ask user to enter one's name

year=$(date +"%Y")
read -rp "Enter your full name (for license headers): " author_name




# --- prerequisites ---
command -v gh >/dev/null 2>&1 || { echo "ERROR: gh not installed" >&2; exit 1; }

# --- auth: only if not logged in (uses GH_TOKEN env var) ---
if ! gh auth status >/dev/null 2>&1; then
  if [[ -n "${GH_TOKEN:-}" ]]; then
    printf "%s" "$GH_TOKEN" | gh auth login --with-token
    # # reduce exposure
    # unset GH_TOKEN
    # echo "Authenticated via GH_TOKEN"
  else
    echo "Not authenticated and GH_TOKEN not set. Set GH_TOKEN or run 'gh auth login' in PowerShell/cmd." >&2
    echo "or this might be your network issue, check it out." >&2
    exit 2
  fi
else
  echo "gh already authenticated"
fi

# --- clone official gitignore repo and copy files ---
git clone https://github.com/github/gitignore.git temp_gitignore
mkdir -p $gitignore_folder
cp -v temp_gitignore/*.gitignore $gitignore_folder/
# stop 1 sec (just in case of FS delay or faster operations)
sleep 1
rm -rf temp_gitignore
echo "Copied .gitignore templates to $gitignore_folder/"



# --- fetch licenses (IMPORTANT: omit leading slash on Windows) ---
mkdir -p $license_folder
# Remove possible CRs from Windows-style output, read safely
gh api licenses --jq '.[].key' | tr -d '\r' | while IFS= read -r key; do
  printf 'Fetching license: %s\n' "$key"
  # Use endpoint WITHOUT leading slash to avoid MSYS path translation
  gh api "licenses/$key" --jq .body > "$license_folder/${key}.txt"  
  # with the year and author_name, populate LICENSE templates
  # [year] or [yyyy] should be substituted
  # [fullname] or [name of copyright owner] should be substituted
  sed -i.bak -e "s/\[year\]/$year/g" \
             -e "s/\[yyyy\]/$year/g" \
             -e "s/<year>/$year/g" \
             -e "s/\[fullname\]/$author_name/g" \
             -e "s/\[name of copyright owner\]/$author_name/g" \
             -e "s/<name of author>/$author_name/g" \
             -e "s/<one line to give the program's name and a brief idea of what it does.>//g" \
             "$license_folder/${key}.txt"
  rm -f "$license_folder/${key}.txt.bak"
done

echo "All done: $gitignore_folder/ and $license_folder/ populated."
