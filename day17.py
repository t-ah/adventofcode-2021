def main():
    x_min, x_max = 207, 263
    y_min, y_max = -115, -63

    global_max_height = 0
    velocities = set()
    for vx_start in range(x_max + 1):
        if get_max_x(vx_start) < x_min:
            continue
        for vy_start in range(y_min, x_max//2):
            x, y = 0, 0
            vx, vy = vx_start, vy_start
            local_max_height = 0
            while x <= x_max and y >= y_min:
                x += vx
                y += vy
                vx = max(vx - 1, 0)
                vy -= 1
                local_max_height = max(local_max_height, y)
                if x >= x_min and x <= x_max and y >= y_min and y <= y_max:
                    velocities.add((vx_start, vy_start))
                    global_max_height = max(global_max_height, local_max_height)
    print("max y", global_max_height)
    print("count v", len(velocities))


def get_max_x(vx):
    return (vx * (vx + 1)) // 2


if __name__ == "__main__":
    main()