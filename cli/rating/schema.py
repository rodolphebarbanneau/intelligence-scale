from __future__ import annotations

from pydantic import BaseModel, Field


class CheckAnswer(BaseModel):
    id: str = Field(description="Check id from the rubric, such as `named_actor`.")
    passed: bool = Field(description="True only when the spec proves the check.")
    quote: str = Field(
        default="",
        description="When passed: text copied verbatim from the spec that proves the check. Use ... to join two excerpts. Empty when not passed.",
    )


class LimitAnswer(BaseModel):
    id: str = Field(description="Limit id from the rubric, such as `preview`.")
    applies: bool = Field(description="True only when the spec shows the limit.")
    quote: str = Field(default="", description="When applies: text copied verbatim from the spec that shows the limit.")


class CriterionAnswer(BaseModel):
    key: str = Field(description="Criterion key, such as `II.7`.")
    checks: list[CheckAnswer] = Field(description="One answer for every check of this criterion, at every level.")
    limits: list[LimitAnswer] = Field(description="One answer for every limit of this criterion, including the common limits.")
    note: str = Field(description="One or two plain sentences: the evidence and the limit that decide this criterion.")


class AxisAnswer(BaseModel):
    configuration: str = Field(description="The single product configuration rated: product, plan or edition, and any first-class wrap.")
    summary: str = Field(description="Two to four sentences on the operating model or coverage the product enables today.")
    criteria: list[CriterionAnswer] = Field(description="Every criterion of the rubric, in rubric order.")
    gap: str = Field(description="The smallest set of concrete missing capabilities, named by criterion, that limits the score.")
