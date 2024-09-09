# 정부 R&D 과제 총연구개발비 계산 프로그램

def calculate_total_research_cost(government_funding):
    total_research_cost = government_funding / 0.75
    institution_contribution = total_research_cost - government_funding
    
    government_funding_ratio = (government_funding / total_research_cost) * 100
    institution_contribution_ratio = (institution_contribution / total_research_cost) * 100
    
    return total_research_cost, institution_contribution, government_funding_ratio, institution_contribution_ratio

