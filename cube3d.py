import numpy as np
import pygame
# -------------- constante --------------
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

theta_x = 0.05
theta_y = 0.05
theta_z = 0.05

weight, height = 1200, 600
x_center, y_center = weight/2, height/2
pas = 10

# -------------- fonction --------------
# créer les points


def createPts():
    pts = {}
    compt = 0
    for i in [-1, 1]:
        for j in [-1, 1]:
            for k in [-1, 1]:
                pts[compt] = np.array([i, j, k])
                compt += 1
    return pts

# calculer le nouveau vecteur de point


def calculAngle(tx, ty, tz, vector):
    cx, sx = np.cos(tx), np.sin(tx)
    cy, sy = np.cos(ty), np.sin(ty)
    cz, sz = np.cos(tz), np.sin(tz)
    mx = np.array([[1, 0, 0],
                   [0, cx, -sx],
                   [0, sx, cx]])
    my = np.array([[cy, 0, sy],
                   [0, 1, 0],
                   [-sy, 0, cy]])
    mz = np.array([[cz, -sz, 0],
                   [sz, cz, 0],
                   [0, 0, 1]])
    return (np.dot(np.dot(mx, np.dot(my, mz)), vector))


def drawLine(pt1, pt2):
    if pt1[2] < 0 or pt2[2] < 0:
        pygame.draw.lines(dis, blue, False, [
                          pt1[0:2]*100+[x_center, y_center], pt2[0:2]*100+[x_center, y_center]])
    else:
        pygame.draw.line(
            dis, blue, pt1[0:2]*100+[x_center, y_center], pt2[0:2]*100+[x_center, y_center])
    pygame.display.update()
    return


# --------------- script --------------
# initialise les points
pts = createPts()
"""
print(pts)
raise ValueError()
"""
# crée la fenetre
pygame.init()
dis = pygame.display.set_mode((weight, height))
pygame.display.set_caption('Cube 3D')
pygame.display.update()

# commence la fenetre
i = 0
game_over = False
while not game_over:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            dis.fill(white)
            if event.key == pygame.K_l:
                game_over = True
            if event.key == pygame.K_z:
                for i in range(8):
                    pts[i] = calculAngle(
                        0.05, 0, 0, pts[i])
            if event.key == pygame.K_q:
                for i in range(8):
                    pts[i] = calculAngle(
                        0, 0.05, 0, pts[i])
            if event.key == pygame.K_d:
                for i in range(8):
                    pts[i] = calculAngle(
                        0, 0, 0.05, pts[i])

        """
        for j in pts:
            pygame.draw.circle(dis, red, pts[0], 10)
        """
        # x_init, y_init, weight, height
        dis.fill(black)
        for i in range(8):
            pts[i] = calculAngle(
                theta_x, theta_y, theta_z, pts[i])
        for i in range(8):
            pygame.draw.circle(
                dis, red, pts[i][0:2]*100+[x_center, y_center], 3, width=1)
        drawLine(pts[1], pts[3])
        drawLine(pts[7], pts[3])
        drawLine(pts[7], pts[5])
        drawLine(pts[1], pts[5])
        drawLine(pts[0], pts[2])
        drawLine(pts[6], pts[2])
        drawLine(pts[6], pts[4])
        drawLine(pts[4], pts[0])
        drawLine(pts[0], pts[1])
        drawLine(pts[2], pts[3])
        drawLine(pts[4], pts[5])
        drawLine(pts[6], pts[7])
        pygame.draw.rect(dis, blue, [x_center, y_center, 10, 10])
        pygame.display.update()
pygame.quit()
quit()
