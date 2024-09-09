from src.calculator import calculate_total_research_cost
from src.utils import format_currency, format_percentage

def main():
    government_funding = float(input("정부 출연금을 입력하세요 (단위: 백만원): "))

    total_research_cost, institution_contribution, government_funding_ratio, institution_contribution_ratio = calculate_total_research_cost(government_funding)

    print(f"\n계산 결과:")
    print(f"정부 출연금: {format_currency(government_funding)}")
    print(f"기관 부담금: {format_currency(institution_contribution)}")
    print(f"총 연구개발비: {format_currency(total_research_cost)}")
    print(f"정부 출연금 비율: {format_percentage(government_funding_ratio)}")
    print(f"기관 부담금 비율: {format_percentage(institution_contribution_ratio)}")

if __name__ == "__main__":
    main()
else:
    # 테스트 시에는 이 부분이 실행됩니다.
    pass