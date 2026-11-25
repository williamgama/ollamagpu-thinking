# V5 standby — optional desktop modules

Source pinned to dc3d6609e27fca7f9667147b37b939ed311bd8d4, after the current cumulative V4 metrics and V5 CLI patches. No workflow modification or build in this branch. Do not merge before Search Engine integration and approval of the consolidated build.

## Staged
- Separate Gama settings card; four persistent module flags in additive SQLite migration 20→21. Existing response metrics on by default; export, resident monitor, prompt picker opt-in.
- Metrics off: no new per-response performance snapshot; preserved historical data.
- Resident monitor: authenticated read-only route, disabled on backend when off, no polling, abort on close.
- Markdown/JSON clipboard export of completed visible user/assistant text, no raw attachment bytes, internal thinking or tool payload; native save-to-file still pending.
- Six compact editable prompt templates, explicit selection only, no scripts or automatic send.
- Custom desktop policy: skip location prompt, avoid new shared login registration, skip upstream update checker and block bundle replacement paths. Existing cache and original installation are not modified. No claim that a previously registered Squirrel helper is fixed.

## Integration instructions (future authorized build)
After cumulative existing workflow patches have been applied to the source checkout, check and then apply:
```sh
python3 standby/v5/apply_productivity.py source --check
python3 standby/v5/apply_productivity.py source
```
When integrating, ensure the repository checkout or patch files are available to the workflow (currently it fetches upstream source directly); pin the commit and use an explicit manual build gate. Run existing V4 regression tests plus TestGamaModulesPersistence and the GamaModules vitest file. Validate generated types after all upstream patches, SQL migration on fresh and existing V4 DB, concurrent native settings updates, disabled endpoint, abort behavior, clipboard in WKWebView, six templates, Thinking, Cmd+Q, startup/reboot, idle RAM/CPU/VRAM and rollback. Do not overwrite the original bundle or remove shared system registrations. No macOS build or runtime testing has occurred for this patch.

## Pending approved features
Search Engine contract/provider benchmark first, then globe integration and citations. Next: per-model/chat presets and system prompt, context budget, conversation search/favorites and native file save, council sequential with ownership-aware scheduler, SKILL.md import and library, projects/memory/RAG, benchmark lab, MCP and multimedia. Do not expose nonfunctional switches. Keep existing engine and no always-on services. No real provider keys or client data in the repository.
