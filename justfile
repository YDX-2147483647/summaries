set windows-shell := ["pwsh", "-NoLogo", "-Command"]
set dotenv-load

mkdocs := env_var_or_default('MKDOCS', 'mkdocs')


# List available recipes
@default:
    just --list


# Start the live-reloading docs server
serve:
    {{ mkdocs }} serve

# Build the docs site
build:
    {{ mkdocs }} build
