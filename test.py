import random

# 기본 확률 설정
base_6star_rate = 0.02  # 6성 기본 확률 (2%)
pickup_rate = 0.5       # 6성 중 픽업 오퍼레이터 확률 (50%)
simulations = 10000     # 시뮬레이션 횟수
pulls = 10              # 뽑기 횟수

# 보정 시스템 (50회 이후 6성 확률 증가)
def get_6star_rate(pull_count):
    if pull_count < 50:
        return base_6star_rate
    else:
        # 51회째부터 2%씩 증가
        return base_6star_rate + 0.02 * (pull_count - 50)

# 한 번의 뽑기 시뮬레이션
def single_pull(pull_count):
    rate = get_6star_rate(pull_count)
    if random.random() < rate:  # 6성 등장
        if random.random() < pickup_rate:  # 픽업 오퍼레이터 등장
            return True
    return False

# 시뮬레이션 실행
success_count = 0
for _ in range(simulations):
    for pull_count in range(1, pulls + 1):
        if single_pull(pull_count):
            success_count += 1
            break

# 결과 출력
success_rate = success_count / simulations * 100
print(f"{pulls}회 뽑기 내 특정 6성 픽업 오퍼레이터를 뽑을 확률: {success_rate:.2f}%")

#  코드 설명
#  get_6star_rate(): 보정 시스템을 구현하여 50회 이후 6성 확률을 증가시킵니다.
#  single_pull(): 한 번의 뽑기에서 6성 픽업 오퍼레이터를 뽑는지 확인합니다.
#  시뮬레이션은 10,000번 실행되며, 10회 뽑기 내 성공 확률을 계산합니다.
#  결과는 근사값으로, 실제 게임 데이터와 유사한 값을 제공합니다.
