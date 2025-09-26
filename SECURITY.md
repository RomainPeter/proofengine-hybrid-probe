# Security and Integrity Notes

This is a public brief and demo:
- Attestations: demo-only HMAC signature using `DEMO_SECRET` env (default "demo-secret").
- Hermeticity: we use a workspace folder and avoid network calls during verification.
- Reproducibility: pinned dependencies; CI reenacts the demo.

Do not rely on this demo for production compliance or signing. For production, use Sigstore / in-toto, Wasm/OCI sandboxes, and hardware-backed keys.