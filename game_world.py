objects = [[] for _ in range(4)]

collision_pairs = {} # {'boy:ball' : [ [bay] , [ball1,ball2,....]] }

def add_object(o, depth = 0):
    objects[depth].append(o)

def add_objects(ol, depth = 0):
    objects[depth] += ol


def update():
    for layer in objects:
        for o in layer:
            o.update()


def render():
    for layer in objects:
        for o in layer:
            o.draw()


def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o)  # 충돌 그룹에서 삭제 완료
            del o  # 객체 자체를 완전히 메모리에서 제거한다.
            return
    raise ValueError('Cannot delete non existing object')


def clear():
    for layer in objects:
        layer.clear()
def remove_collision_object(o):
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)

    pass


def collide(a, b):
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()

    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False

    return True

def add_collision_pair(group, a, b):
    if group not in collision_pairs:
        print(f'New group {group} added. ')
        collision_pairs[group] =[ [ ], [ ] ]
    if a: #a가 있을 때 즉 , a가 None이 아니면 ..
        collision_pairs[group][0].append(a)
    if b:
        collision_pairs[group][1].append(b)


def handle_collision():
    #등록된 모든 충돌 상황에 대해서 충돌 검사 및 충돌 처리를 수행한다.
    for group,pairs in collision_pairs.items(): #key, value
        for a in pairs[0]:
            for b in pairs[1]:
                if collide(a,b):
                    a.handle_collision(group,b)
                    b.handle_collision(group,a)

    return None