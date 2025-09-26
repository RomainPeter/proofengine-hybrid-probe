# Release v0.1.0

## 🎯 Proof Engine — Public Brief

**Auditable AI slice: Orchestrator/Verifier + PCAP demo. Neutral public brief.**

### ✨ Features

- **Minimal PCAP format** with JSON schemas
- **Orchestrator/Verifier architecture** (deterministic control)
- **Code compliance demo** (unit tests, type checks, lints)
- **Hermetic verification** with workspace isolation
- **Demo attestations** with HMAC signatures

### 🏗️ Architecture

- **Orchestrator**: Builds PCAPs, manages state X
- **Semantic Engine**: LLM stub (candidate generation)
- **Formal Verifier**: Deterministic proof validation

### 🚀 Quick Start

```bash
make setup
make demo.pass   # or: make demo.fail
```

### 📋 What's Included

- PCAP schema and examples
- Verifier (jsonschema, ruff, mypy, pytest)
- Reproducible builds with pinned deps
- CI/CD with artifact uploads
- Neutral positioning (no third-party endorsement)

### 📄 Licenses

- **Code**: BUSL-1.1 (see LICENSES/CODE_LICENSE.txt)
- **Docs**: CC BY-NC-ND 4.0 (see LICENSES/DOCS_LICENSE.txt)

### ⚠️ Limits

- No real LLM (candidate generation stubbed)
- Demo HMAC signing (not production-grade)
- See SECURITY.md for details

---

*Independent research brief. No endorsement by any company.*
