def solution(n, build_frame):
    structure = set()

    def can_build():
        for x, y, a in structure:
            if a == 0:  # 기둥
                if y == 0 or \
                   (x, y - 1, 0) in structure or \
                   (x - 1, y, 1) in structure or \
                   (x, y, 1) in structure:
                    continue
                return False
            else:  # 보
                if (x, y - 1, 0) in structure or \
                   (x + 1, y - 1, 0) in structure or \
                   ((x - 1, y, 1) in structure and (x + 1, y, 1) in structure):
                    continue
                return False
        return True

    for x, y, a, b in build_frame:
        if b == 1:  # 설치
            structure.add((x, y, a))
            if not can_build():
                structure.remove((x, y, a))
        else:  # 삭제
            structure.remove((x, y, a))
            if not can_build():
                structure.add((x, y, a))

    result = list(map(list, structure))
    result.sort(key=lambda x: (x[0], x[1], x[2]))
    return result
