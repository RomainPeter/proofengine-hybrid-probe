from __future__ import annotations

from typing import Any, Dict, List

from pydantic import BaseModel, Field


class ProofRef(BaseModel):
    kind: str  # "unit_test" | "policy" | "static"
    path: str


class Justification(BaseModel):
    # V = ([0,∞]^n, ≥, +, 0) — simple demo vector of costs
    exec_time_est: float = 0.0
    audit_cost_est: float = 0.0
    security_risk_est: float = 0.0
    info_loss_est: float = 0.0
    tech_debt_est: float = 0.0


class PCAP(BaseModel):
    action: str = "code_change"
    context_hash: str
    obligations: Dict[str, Any] = Field(default_factory=dict)
    proofs: List[ProofRef] = Field(default_factory=list)
    justification: Justification = Field(default_factory=Justification)
    metadata: Dict[str, Any] = Field(default_factory=dict)
