set windows-shell := ["pwsh", "-NoLogo", "-Command"]
set dotenv-load

mkdocs := env_var_or_default('MKDOCS', 'mkdocs')
python := env_var_or_default('PYTHON', 'python')
pip := env_var_or_default('PIP', 'pip')


# List available recipes
@default:
    just --list


# Install MkDocs plugins and markdown extensions with pip
install-ext:
    {{ pip }} install mdx_truly_sane_lists

# Start the live-reloading docs server
serve:
    {{ mkdocs }} serve

# Build the docs site
build:
    {{ mkdocs }} build

# Normalize markdown files
[no-cd]
normalize +FILES:
    {{ python }} '{{ justfile_directory() }}/scripts/normalize.py' {{ FILES }}

# Normalize all markdown files in current directory
[windows]
[no-cd]
normalize-all:
    just normalize (ls *.md -Name | Join-String -Separator ' ')
