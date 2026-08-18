# Stack evidence

Record only files that exist. Do not guess.

| Evidence | Means |
| --- | --- |
| `package.json` | JS/TS (lockfile names the manager) |
| `pyproject.toml`, `requirements.txt`, `Pipfile`, `environment.yml` | Python |
| `go.mod` | Go |
| `Cargo.toml` | Rust |
| `pom.xml`, `build.gradle`, `build.gradle.kts` | JVM |
| `Gemfile` | Ruby |
| `mix.exs` | Elixir |
| `composer.json` | PHP |
| `*.csproj`, `*.sln` | .NET |
| `Package.swift` | Swift |
| `pubspec.yaml` | Dart / Flutter |
| `CMakeLists.txt` | C/C++ |
| `*.tf` | Terraform |
| `flake.nix` | Nix |
| `deno.json` | Deno |
| `nx.json`, `pnpm-workspace.yaml`, `turbo.json` | JS/TS monorepo |
| `Makefile`, `justfile`, `Taskfile.yml` | task runner |
| `docker-compose.yml`, `Dockerfile` | containers |
| `.github/workflows/*`, `.gitlab-ci.yml`, `Jenkinsfile`, `azure-pipelines.yml` | CI |
