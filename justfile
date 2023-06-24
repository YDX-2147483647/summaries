set windows-shell := ["pwsh", "-NoLogo", "-Command"]
set dotenv-load := true

python := env_var_or_default('PYTHON', 'python')
pip := python + " -m pip"
mkdocs := python + " -m mkdocs"

# List available recipes
@default:
    just --list

# Install/upgrade MkDocs, its plugins, and markdown extensions
bootstrap:
    {{ pip }} install mkdocs-material --upgrade
    {{ pip }} install mdx_truly_sane_lists mkdocs-rss-plugin mkdocs-redirects --upgrade
    dot -V  # Graphviz / dot is also needed for hooks/relationship.py. https://www.graphviz.org/download/
    {{ pip }} install graphviz --upgrade

# Start the live-reloading docs server
serve *ARGS:
    {{ mkdocs }} serve {{ ARGS }}

# Build the docs site
build:
    {{ mkdocs }} build

# Run pre-commit
check *ARGS:
    pre-commit run {{ ARGS }}

# Normalize markdown files
[no-cd]
normalize +FILES:
    {{ python }} '{{ justfile_directory() }}/scripts/normalize.py' {{ FILES }}

# Normalize all markdown files in current directory
[no-cd]
[windows]
normalize-all:
    just normalize (ls *.md -Name | Join-String -Separator ' ')
