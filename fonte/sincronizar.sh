#!/bin/bash
# copia o deck montado para a pasta da prévia local (porta 4783)
rsync -a --delete --exclude fonte --exclude src --exclude .git "/Volumes/hd caique becker/Mac Caique/Projetos/bordon-enlatados-trade/" "${1:-/private/tmp/claude-501/-Users-caiquebecker-Library-Application-Support-Claude-scratch-workspaces-d8c84072-0a93-4bec-aa4a-be232e759264-85d7197a-19bb-42e8-a873-f1560b7cb451-scratch-2026-11-16-bfd1e1/2f6dea44-9c9e-4671-88a5-e15d12b1699a/scratchpad/preview}/"
