from dataclasses import dataclass
from typing import Any, Dict, Iterable, List

@dataclass(frozen=True)
class Decision:
    sha: str
    accepted: bool
    reasons: tuple[str, ...]

REQUIRED_FIELDS=("sha","author","visibility","branch","files")

def classify_commit(commit: Dict[str, Any], expected_author: str, expected_branch: str="main") -> Decision:
    reasons: List[str]=[]
    missing=[field for field in REQUIRED_FIELDS if field not in commit]
    if missing: reasons.append("missing fields: "+", ".join(missing))
    if commit.get("visibility") != "public": reasons.append("commit is not public")
    if commit.get("author") != expected_author: reasons.append("different author")
    if commit.get("branch") != expected_branch: reasons.append("different branch")
    if not commit.get("files"): reasons.append("no changed files")
    if commit.get("is_merge",False): reasons.append("merge commit")
    return Decision(str(commit.get("sha","")), not reasons, tuple(reasons))

def classify_history(commits: Iterable[Dict[str,Any]], expected_author: str, expected_branch: str="main") -> List[Decision]:
    return [classify_commit(c, expected_author, expected_branch) for c in commits]

def accepted_shas(commits: Iterable[Dict[str,Any]], expected_author: str, expected_branch: str="main") -> List[str]:
    return [d.sha for d in classify_history(commits, expected_author, expected_branch) if d.accepted]
