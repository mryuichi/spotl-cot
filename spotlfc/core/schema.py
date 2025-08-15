from __future__ import annotations
from pydantic import BaseModel, Field
from typing import List, Optional, Literal, Dict, Any

Role = Literal["S","P","O","T","L"]

class RoleItem(BaseModel):
    name: Optional[str] = None
    qid: Optional[str] = None
    rel: Optional[str] = None
    time: Optional[str] = None  # ISO8601
    lat: Optional[float] = None
    lon: Optional[float] = None
    value: Optional[str] = None

class SPOTL(BaseModel):
    S: List[RoleItem] = []
    P: List[RoleItem] = []
    O: List[RoleItem] = []
    T: List[RoleItem] = []
    L: List[RoleItem] = []

class EvidenceSPOTL(SPOTL):
    source: str
    url: Optional[str] = None
    lines: Optional[str] = None

class CheckRequest(BaseModel):
    post_text: str
    lang: str = Field(default="en")
    images: Optional[List[str]] = None
    max_pages: int = 3

class CheckResponse(BaseModel):
    verdict: Dict[str, Any]
    evidence: List[EvidenceSPOTL]
    role_scores: Dict[str, float]
    explanation: str
