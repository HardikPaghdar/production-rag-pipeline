import pytest
from rag_pipeline.core import query,load

def test_evidence_has_source():
    result=query('examples/knowledge_base','refund manager approval')
    assert result['evidence'] and result['evidence'][0]['source']=='refunds.md'
def test_missing_knowledge_base():
    with pytest.raises(ValueError): load('missing-kb')
def test_short_query_rejected():
    with pytest.raises(ValueError): query('examples/knowledge_base',' ')
