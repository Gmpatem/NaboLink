#!/usr/bin/env python3
"""Lightweight stdlib governance checks. This does not prove runtime functionality."""
from pathlib import Path
import re,sys
ROOT=Path(__file__).resolve().parents[1]
required=['chatgpt-project/PROJECT_VISION.md','chatgpt-project/PROJECT_PRINCIPLES.md','docs/REMOTE_CONTEXT_AND_BRANCH_POLICY.md','AGENTS.md','README.md','docs/PROJECT_STATE.md','docs/DECISION_LOG.md','docs/ARCHITECTURE.md','docs/ENGINEERING_PLAYBOOK.md','docs/CONTEXT_SYNC_PROTOCOL.md','docs/tasks/ACTIVE_TASK.md','docs/handoffs/LATEST.md','docs/contracts/01-subscriber-lifecycle.md','docs/templates/AGENT_TASK_TEMPLATE.md']
errors=[]
for p in required:
 f=ROOT/p
 if not f.exists() or not f.read_text(encoding='utf8').strip(): errors.append(f'Missing/empty: {p}')
state=(ROOT/'docs/PROJECT_STATE.md').read_text()
active=(ROOT/'docs/tasks/ACTIVE_TASK.md').read_text()
contract=(ROOT/'docs/contracts/01-subscriber-lifecycle.md').read_text()
if 'M0' not in state: errors.append('Project state must declare milestone')
if 'Status:' not in active: errors.append('Active task missing status')
if not re.search(r'Status:\s*\*\*(DRAFT|APPROVED|SUPERSEDED)',contract): errors.append('Contract missing explicit status')
if 'APPROVED' not in contract: errors.append('Contract must specify approval status')
if any((ROOT/p).exists() for p in ['.env','.env.local']): errors.append('Potential local secrets in repository root')
for f in (ROOT/'docs/adr').glob('*.md'):
 if f.name=='README.md':continue
 if not re.search(r'(?im)^\*\*?Status\*\*?:|^Status:',f.read_text()): errors.append(f'ADR missing status: {f.name}')
if errors:
 print('FAIL governance checks:')
 for e in errors:print(' -',e)
 sys.exit(1)
print(f'PASS governance checks ({len(required)} mandatory files, declared statuses, no root .env)')
print('Note: no application tests, deployment, legal or network certifications were performed.')
