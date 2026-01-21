from math import sqrt

def get_next_point(step):
    x = int(input(f"Input x{step} coordinates: "))
    y = int(input(f"Input y{step} coordinates: "))
    return(x, y)

def cal_distance(p1, p2):
    distance = sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
    return distance

def main():
    print('------Robot Program------')

point = (0, 0)
dist = []
step = 1

while True:
    npoint = get_next_point(step)
    if npoint == (999, 999):
        break

    dis = cal_distance(point, npoint)
    dist.append(dis)
    point = npoint
    step += 1

    print('----------')
    for a, b in enumerate (dist, 1):
        print(f"Step{a}: {b:.2f} units")
    print('----------')
    print(f"Total distance travelled by robot is {sum(dist):.2f} units")
    
if __name__ == '__main__':
    main()
