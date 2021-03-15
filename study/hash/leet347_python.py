from collections import Counter

def topKFrequent(self, nums, k):
  return list(zip(*Counter(nums).most_common(k)))[0]

# 파이썬에서 *
'''
파이썬에서 *(아스테리크)는 언팩(unpack)이다.
즉, 시퀀스 언패킹 연산자로 시퀀스를 풀어헤치는 연산자이다.

함수의 파라미터가 되었을 떄는 패킹도 가능하다. 위에서 zip에서는 패킹을 하고 있다.
'''

# zip함수
'''
zip() 함수는 2개 이상의 시퀀스를 "짧은 길이 기준으로 일대일 대응"하는 새로운 튜플 시퀀스를 만드는 역할을 한다.
하지만 파이썬 3에서는 제네레이터를 리턴한다.
튜플은 불변 객체이기 때문이다. zip()은 여러 시퀀스에서 동일한 인덱스의 아이템을 순서대로 추출하여 튜플로 만들어주는 역할을 한다.
'''