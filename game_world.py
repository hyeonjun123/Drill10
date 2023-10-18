import game_world
#리스트오브리스트로만든다. 뭐가 먼저 그려질지 정하기 위해서
objects = [[],[]]  #objects = [[depth0], [depth1]]



def add_object(o, depth =0):
    objects[depth].append(o)

def add_objects(ol, depth = 0):
    objects[depth] += ol

def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            return
    raise ValueError('존재하지않는 객체를지우려함')

def update():
    for layer in objects:
        for o in layer:
            o.update()

def render():
     for layer in objects:
         for o in layer:
            o.draw()


