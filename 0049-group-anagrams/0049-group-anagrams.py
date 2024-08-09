from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # 뭔가 떠오른 방법
        # 해시를 만든다 {}
        # strs를 순회하면서
            # 문자 하나하나를 정렬해서 정렬한 게 키에 없으면 해시에 키로 넣고, 정렬하기 전도 넣음
            # 만약 이미 있으면, 그 키에 추가.
        
        str_dict = defaultdict(list)
        result = []
        # 중복 키는 알아서 없어짐...
        for c in strs:
            str_dict[''.join(sorted(c))] = []
        for c in strs:
            if ''.join(sorted(c)) in str_dict:
                str_dict[''.join(sorted(c))].append(c)
        for key in str_dict:
            result.append(str_dict[key])
        return result
        