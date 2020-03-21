# Auto-generated System Security Plan (SSP)

This repository contains documents and scripts needed to create a Security Plan (SSP).

## Prerequisites

Docker and docker-compose running locally in a `bash` compatible shell:

```bash
docker --version
docker-compose --version
```

## Generating the documentation from [templates](templates) and [keys](keys)

First, ***activate*** your session run:

```bash
docker-compose pull
source activate
```

Then create/update the frontmatter, components and appendices:

```bash
createfiles -i configuration.yaml -t templates
```

To create the family files and full ssp in the `/docs/controls/`:

```bash
makefamilies
makessp
```

Generate a reponsiblity matrix with:

```bash
creatematrix
```

Optional (and temporary) hack to add a Table of Contents (requires <https://github.com/ekalinin/github-markdown-toc> v0.5+ with `gh-md-toc` in your shell search path):

```bash
./makeDocsTOC.sh
```
