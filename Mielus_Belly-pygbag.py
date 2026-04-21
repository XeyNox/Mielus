# Créé par User, le 03/05/2025 en Python 3.7
import pygame
import random
import sys
import math
#import pyttsx3
import os

if os.name == "nt":
    separateur_repertoire = "\\"
elif os.name == "posix":
    separateur_repertoire = "/"
else:
    separateur_repertoire = "séparateur_inconnu"

# Configuration
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
DISK_RADIUS = 15  # 30 px diameter
MIN_OBSTACLE_SIZE_FIRST_LEVELS = 60
MIN_OBSTACLE_SIZE_MID_LEVELS = 40
MIN_OBSTACLE_SIZE_HARD_LEVELS = 20
MAX_OBSTACLE_SIZE_FIRST_LEVELS = 200
MAX_OBSTACLE_SIZE_MID_LEVELS = 140
MAX_OBSTACLE_SIZE_HARD_LEVELS = 100
MIN_OBSTACLE_SPEED = 4
MAX_OBSTACLE_SPEED = 7#5.1
COLORS = {
    'BLUE': (0, 0, 255),
    'RED': (255, 0, 0),
    'GREEN': (0, 255, 0),
    'YELLOW': (255, 255, 0)
}
COOLDOWN_MS = 500
STAR_DIAMETER = DISK_RADIUS * 2
STAR_INCREMENT = 20
monnaies_singulier = [
    "Afghani (Afghanistan)", "Ariary (Madagascar)", "Baht (Thaïlande)", "Balboa (Panama)",
    "Birr (Éthiopie)", "Bolívar (Venezuela)", "Boliviano (Bolivie)", "Cedi (Ghana)", "Colón (Costa Rica)",
    "Couronne danoise (Danemark)", "Couronne norvégienne (Norvège)", "Couronne suédoise (Suède)",
    "Dinar algérien (Algérie)", "Dinar bahreïni (Bahreïn)", "Dinar irakien (Irak)", "Dinar jordanien (Jordanie)",
    "Dinar koweïtien (Koweït)", "Dinar libyen (Libye)", "Dinar serbe (Serbie)", "Dinar tunisien (Tunisie)",
    "Dirham marocain (Maroc)", "Dirham des Émirats arabes unis (Émirats arabes unis)",
    "Dollar américain (États-Unis)", "Dollar australien (Australie)", "Dollar canadien (Canada)",
    "Dollar néo-zélandais (Nouvelle-Zélande)", "Dollar de Singapour (Singapour)", "Euro (Zone euro)",
    "Franc suisse (Suisse)", "Franc CFA (Afrique de l'Ouest)", "Franc CFA (Afrique centrale)",
    "Gourde (Haïti)", "Hryvnia (Ukraine)", "Kwanza (Angola)", "Kyat (Myanmar)", "Lari (Géorgie)",
    "Lek (Albanie)", "Lempira (Honduras)", "Lev (Bulgarie)", "Livre égyptienne (Égypte)",
    "Livre sterling (Royaume-Uni)", "Manat (Azerbaïdjan)", "Metical (Mozambique)", "Naira (Nigéria)",
    "Peso argentin (Argentine)", "Peso chilien (Chili)", "Peso colombien (Colombie)", "Peso cubain (Cuba)",
    "Peso dominicain (République dominicaine)", "Peso mexicain (Mexique)", "Peso philippin (Philippines)",
    "Rial iranien (Iran)", "Rial omanais (Oman)", "Rial qatari (Qatar)", "Rial saoudien (Arabie saoudite)",
    "Riel (Cambodge)", "Ringgit (Malaisie)", "Roupie indienne (Inde)", "Roupie indonésienne (Indonésie)",
    "Roupie mauricienne (Maurice)", "Roupie népalaise (Népal)", "Roupie pakistanaise (Pakistan)",
    "Roupie seychelloise (Seychelles)", "Rouble russe (Russie)", "Rufiyaa (Maldives)", "Shekel israélien (Israël)",
    "Shilling kényan (Kenya)", "Shilling ougandais (Ouganda)", "Som (Kirghizistan)", "Somoni (Tadjikistan)",
    "Tenge (Kazakhstan)", "Tugrik (Mongolie)", "Won nord-coréen (Corée du Nord)", "Won sud-coréen (Corée du Sud)",
    "Yen (Japon)", "Yuan (Chine)", "Zloty (Pologne)"
]

monnaies_pluriel = [
    "Afghanis (Afghanistan)", "Ariarys (Madagascar)", "Bahts (Thaïlande)", "Balboas (Panama)",
    "Birrs (Éthiopie)", "Bolívars (Venezuela)", "Bolivianos (Bolivie)", "Cedis (Ghana)", "Colóns (Costa Rica)",
    "Couronnes danoises (Danemark)", "Couronnes norvégiennes (Norvège)", "Couronnes suédoises (Suède)",
    "Dinars algériens (Algérie)", "Dinars bahreïnis (Bahreïn)", "Dinars irakiens (Irak)", "Dinars jordaniens (Jordanie)",
    "Dinars koweïtiens (Koweït)", "Dinars libyens (Libye)", "Dinars serbes (Serbie)", "Dinars tunisiens (Tunisie)",
    "Dirhams marocains (Maroc)", "Dirhams des Émirats arabes unis (Émirats arabes unis)",
    "Dollars américains (États-Unis)", "Dollars australiens (Australie)", "Dollars canadiens (Canada)",
    "Dollars néo-zélandais (Nouvelle-Zélande)", "Dollars de Singapour (Singapour)", "Euros (Zone euro)",
    "Francs suisses (Suisse)", "Francs CFA (Afrique de l'Ouest)", "Francs CFA (Afrique centrale)",
    "Gourdes (Haïti)", "Hryvnias (Ukraine)", "Kwanzas (Angola)", "Kyats (Myanmar)", "Laris (Géorgie)",
    "Leks (Albanie)", "Lempiras (Honduras)", "Levs (Bulgarie)", "Livres égyptiennes (Égypte)",
    "Livres sterling (Royaume-Uni)", "Manats (Azerbaïdjan)", "Meticals (Mozambique)", "Nairas (Nigéria)",
    "Pesos argentins (Argentine)", "Pesos chiliens (Chili)", "Pesos colombiens (Colombie)", "Pesos cubains (Cuba)",
    "Pesos dominicains (République dominicaine)", "Pesos mexicains (Mexique)", "Pesos philippins (Philippines)",
    "Rials iraniens (Iran)", "Rials omanais (Oman)", "Rials qataris (Qatar)", "Rials saoudiens (Arabie saoudite)",
    "Riels (Cambodge)", "Ringgits (Malaisie)", "Roupies indiennes (Inde)", "Roupies indonésiennes (Indonésie)",
    "Roupies mauriciennes (Maurice)", "Roupies népalaises (Népal)", "Roupies pakistanaises (Pakistan)",
    "Roupies seychelloises (Seychelles)", "Roubles russes (Russie)", "Rufiyaas (Maldives)", "Shekels israéliens (Israël)",
    "Shillings kényans (Kenya)", "Shillings ougandais (Ouganda)", "Soms (Kirghizistan)", "Somonis (Tadjikistan)",
    "Tenges (Kazakhstan)", "Tugriks (Mongolie)", "Wons nord-coréens (Corée du Nord)", "Wons sud-coréens (Corée du Sud)",
    "Yens (Japon)", "Yuans (Chine)", "Zlotys (Pologne)"
]


# Init audio
pygame.mixer.init()
touch_sound = pygame.mixer.Sound('touch.wav')
tear_sound = pygame.mixer.Sound('tear_ext.wav')   # extended dramatic tear
violin_sound = pygame.mixer.Sound('violin.wav')  # 3s symphonic violin
kermit_no_sound = pygame.mixer.Sound('kermit_no.wav')
mielus_belly_sound = pygame.mixer.Sound('mielus_belly_mix.wav')
good_luck_sound = pygame.mixer.Sound('manavoice' + separateur_repertoire + 'good_luck.mp3')
level_sound = pygame.mixer.Sound('manavoice' + separateur_repertoire + 'level.mp3')
and_now__let_s_play_level_sound = pygame.mixer.Sound('manavoice' + separateur_repertoire + 'and_now__let_s_play_level.mp3')
you_won_sound = pygame.mixer.Sound('manavoice' + separateur_repertoire + 'you_won.mp3')
point_sound = pygame.mixer.Sound('manavoice' + separateur_repertoire + 'point.mp3')
points_sound = pygame.mixer.Sound('manavoice' + separateur_repertoire + 'points.mp3')
bonus_sound = pygame.mixer.Sound('manavoice' + separateur_repertoire + 'bonus.mp3')

pleasant_chime_sound = pygame.mixer.Sound('pleasant_chime.wav')

do_sound = pygame.mixer.Sound("notes" + separateur_repertoire + 'do.wav')
re_sound = pygame.mixer.Sound("notes" + separateur_repertoire + 're.wav')
mi_sound = pygame.mixer.Sound("notes" + separateur_repertoire + 'mi.wav')
fa_sound = pygame.mixer.Sound("notes" + separateur_repertoire + 'fa.wav')
sol_sound = pygame.mixer.Sound("notes" + separateur_repertoire + 'sol.wav')
la_sound = pygame.mixer.Sound("notes" + separateur_repertoire + 'la.wav')
si_sound = pygame.mixer.Sound("notes" + separateur_repertoire + 'si.wav')
do_high_sound = pygame.mixer.Sound("notes" + separateur_repertoire + 'do_high.wav')



conversion_sounds = [pleasant_chime_sound, do_sound, re_sound, mi_sound, fa_sound, sol_sound, la_sound, si_sound, do_high_sound]



numbers_sound = []
for i in range(100):
    numbers_sound.append(pygame.mixer.Sound("manavoice" + separateur_repertoire + str(i) + ".ogg"))


def calcul_time_limit(level):
    res = 5000 + level * 2500
    if level == 2 :
        res += 2000
    return res

def annonce_level(level):
    if level == 0:
        level_sound.play()
        pygame.time.delay(int(0.25 * 1000))
    else:
        and_now__let_s_play_level_sound.play()
        pygame.time.delay(int(1.8 * 1000))
    numbers_sound[level+1].play()
    pygame.time.delay(int(0.8 * 1000))
    good_luck_sound.play()



class Obstacle:
    def __init__(self, level, shape, color_name, **kwargs):
        self.shape = shape
        self.color_name = color_name
        self.color = COLORS[color_name]
        if shape == 'rect':
            self.rect = kwargs.get('rect')
        else:
            self.center = kwargs.get('center')
            self.radius = kwargs.get('radius')
            if shape == 'star':
                self.angle = 0.0
                self.angular_speed = random.choice([-1, 1]) * random.uniform(0.05, 0.15)
        #MIN_SPEED = MIN_OBSTACLE_SPEED*0.05*level
        #MAX_SPEED = MAX_OBSTACLE_SPEED*0.05*level

        coef = level/3
        if coef < 8:
            MIN_SPEED = 0.25*coef
            MAX_SPEED = coef
        else:
            MIN_SPEED = 8
            MAX_SPEED = 8

        self.vx = random.uniform(MIN_SPEED, MAX_SPEED) * random.choice([-1, 1])
        self.vy = random.uniform(MIN_SPEED, MAX_SPEED) * random.choice([-1, 1])
        self.last_touched = 0

    def update(self):
        if self.shape == 'rect':
            self.rect.x += self.vx
            self.rect.y += self.vy
            if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
                self.vx *= -1
            if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
                self.vy *= -1
        else:
            x, y = self.center
            x += self.vx
            y += self.vy
            if x - self.radius < 0 or x + self.radius > SCREEN_WIDTH:
                self.vx *= -1
            if y - self.radius < 0 or y + self.radius > SCREEN_HEIGHT:
                self.vy *= -1
            self.center = (x, y)
            if self.shape == 'star':
                self.angle += self.angular_speed

    def draw(self, surface):
        if self.shape == 'rect':
            pygame.draw.rect(surface, self.color, self.rect)
        elif self.shape == 'circle':
            pygame.draw.circle(surface, self.color, (int(self.center[0]), int(self.center[1])), self.radius)
        else:
            points = []
            inner_r = self.radius * 0.5
            for i in range(12):
                ang = self.angle + i * math.pi / 6
                r = self.radius if i % 2 == 0 else inner_r
                x = self.center[0] + r * math.cos(ang)
                y = self.center[1] + r * math.sin(ang)
                points.append((x, y))
            pygame.draw.polygon(surface, self.color, points)

    def collides(self, x, y):
        if self.shape == 'rect':
            return self.rect.collidepoint(x, y)
        dx = x - self.center[0]
        dy = y - self.center[1]
        return dx*dx + dy*dy <= self.radius*self.radius


def generate_obstacles(num, disk_color_name, level):
    obs = []
    num_stars = num // 3 if level >= 3 else 0
    num_normal = num - num_stars

    if level < 5 :
        MIN_OBSTACLE_SIZE = MIN_OBSTACLE_SIZE_FIRST_LEVELS
        MAX_OBSTACLE_SIZE = MAX_OBSTACLE_SIZE_FIRST_LEVELS
    elif level < 7 :
        MIN_OBSTACLE_SIZE = MIN_OBSTACLE_SIZE_MID_LEVELS
        MAX_OBSTACLE_SIZE = MAX_OBSTACLE_SIZE_MID_LEVELS
    else :
        MIN_OBSTACLE_SIZE = MIN_OBSTACLE_SIZE_HARD_LEVELS
        MAX_OBSTACLE_SIZE = MAX_OBSTACLE_SIZE_HARD_LEVELS

    # Normal obstacles
    for _ in range(num_normal):
        shape = random.choice(['rect', 'circle'])
        color = random.choice([c for c in COLORS if c != disk_color_name])
        if shape == 'rect':
            w = random.randint(MIN_OBSTACLE_SIZE, MAX_OBSTACLE_SIZE)
            h = random.randint(MIN_OBSTACLE_SIZE, MAX_OBSTACLE_SIZE)
            x = random.randint(0, SCREEN_WIDTH - w)
            y = random.randint(0, SCREEN_HEIGHT - h)
            obs.append(Obstacle(level, 'rect', color, rect=pygame.Rect(x, y, w, h)))
        else:
            r = random.randint(MIN_OBSTACLE_SIZE // 2, MAX_OBSTACLE_SIZE // 2)
            x = random.randint(r, SCREEN_WIDTH - r)
            y = random.randint(r, SCREEN_HEIGHT - r)
            obs.append(Obstacle(level, 'circle', color, center=(x, y), radius=r))
    # Star obstacles
    cx, cy = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
    threshold = max(cx, cy) * 0.8
    for _ in range(num_stars):
        r = STAR_DIAMETER // 2
        for _ in range(100):
            x = random.randint(r, SCREEN_WIDTH - r)
            y = random.randint(r, SCREEN_HEIGHT - r)
            if math.hypot(x - cx, y - cy) >= threshold:
                break
        obs.append(Obstacle(level, 'star', 'YELLOW', center=(x, y), radius=r))
    random.shuffle(obs)
    return obs


def main():
    global STAR_DIAMETER
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("!! Mielus Belly !!")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 48)

    background_acceuil = pygame.image.load("acceuil.png").convert()
    background_acceuil = pygame.transform.scale(background_acceuil, (SCREEN_WIDTH, SCREEN_HEIGHT))

    background_playing = pygame.image.load("playing.png").convert()
    background_playing = pygame.transform.scale(background_playing, (SCREEN_WIDTH, SCREEN_HEIGHT))

    background_gameover = pygame.image.load("gameover.png").convert()
    background_gameover = pygame.transform.scale(background_gameover, (SCREEN_WIDTH, SCREEN_HEIGHT))

    background_playing_t = []
    for i in range(4) :
        background_playing_t.append(pygame.image.load("background" + separateur_repertoire \
        + "playing" + separateur_repertoire + "playing" + str(i+1) + ".png").convert())
        background_playing_t[i] = pygame.transform.scale(background_playing_t[i], (SCREEN_WIDTH, SCREEN_HEIGHT))

    background_apopo = []
    for i in range(4) :
        background_apopo.append(pygame.image.load("apopo" + separateur_repertoire + "apopo" + str(i+1) + ".png").convert())
        background_apopo[i] = pygame.transform.scale(background_apopo[i], (SCREEN_WIDTH, SCREEN_HEIGHT))

    background_death_star = []
    for i in range(4) :
        background_death_star.append(pygame.image.load("death_star" + separateur_repertoire + "death_star" + str(i+1) + ".png").convert())
        background_death_star[i] = pygame.transform.scale(background_death_star[i], (SCREEN_WIDTH, SCREEN_HEIGHT))


    background_victoire = []
    for i in range(5) :
        background_victoire.append(pygame.image.load("victoire" + separateur_repertoire + "victoire" + str(i+1) + ".png").convert())
        background_victoire[i] = pygame.transform.scale(background_victoire[i], (SCREEN_WIDTH, SCREEN_HEIGHT))

    screen.blit(background_acceuil, (0, 0))

    # Game state init
    level = 1
    score = 0
    disk_color_name = 'BLUE'
    disk_color = COLORS[disk_color_name]
    x, y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
    speed = 5
    STAR_DIAMETER = DISK_RADIUS * 2
    obstacles = generate_obstacles(level, disk_color_name, level)
    start_time = pygame.time.get_ticks()
    time_limit = calcul_time_limit(level)
    state = 'PLAYING'
    tolerance = 3
    indice_monnaie = random.randint(0, len(monnaies_pluriel)-1)

    state = 'START'

    CLIGNOTANT = 0

    while True:
        dt = clock.tick(60)
        now = pygame.time.get_ticks()
        remaining = max(0, (time_limit - (now - start_time)) // 1000)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (state == 'GAMEOVER' or state == 'GAMEOVER_STAR' or state == 'START') and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                level = 1
                score = 0
                disk_color_name = 'BLUE'
                disk_color = COLORS[disk_color_name]
                x, y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
                STAR_DIAMETER = DISK_RADIUS * 2
                obstacles = generate_obstacles(level, disk_color_name, level)
                start_time = now
                time_limit = calcul_time_limit(level)
                state = 'PLAYING'
                tolerance = 2
                annonce_level(level-1)
                indice_monnaie = random.randint(0, len(monnaies_pluriel)-1)

        if state == 'PLAYING':
            keys = pygame.key.get_pressed()
            if keys[pygame.K_h]:
                mielus_belly_sound.play()
            if keys[pygame.K_LEFT] or keys[pygame.K_q]:
                x -= speed
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                x += speed
            if keys[pygame.K_UP] or keys[pygame.K_z]:
                y -= speed
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                y += speed
            x = max(DISK_RADIUS, min(SCREEN_WIDTH - DISK_RADIUS, x))
            y = max(DISK_RADIUS, min(SCREEN_HEIGHT - DISK_RADIUS, y))

            for o in obstacles:
                o.update()
                if o.shape == 'star' and o.collides(x, y):
                    pygame.mixer.stop()
                    tear_sound.play()
                    # wait for tear sound to finish
                    pygame.time.delay(int(1.2 * 1000))
                    violin_sound.play()
                    # wait for violin to finish
                    pygame.time.delay(int(3.0 * 1000))
                    state = 'GAMEOVER_STAR'
                    break
                if o.shape in ('rect', 'circle') and o.collides(x, y) and now - o.last_touched > COOLDOWN_MS:
                    if o.color_name != disk_color_name:
                        o.color_name = disk_color_name
                        o.color = COLORS[disk_color_name]
                        if tolerance == 2 :
                            conversion_sounds[0].play()
                        elif tolerance == 1 :
                            random.choice(conversion_sounds).play()
                        else :
                            kermit_no_sound.play()

                        coef = -3
                        if tolerance != 0:
                            coef = 3 - tolerance
                        score += level*coef

                        screen.blit(background_playing, (0, 0))

                        txt = font.render(f"Time: {remaining}s  Score: {score} Level : {level}", True, (255, 255, 255))
                        screen.blit(txt, (20, 20))
                        pygame.display.flip()



                        STAR_DIAMETER += STAR_INCREMENT
                        for s in obstacles:
                            if s.shape == 'star':
                                s.radius = STAR_DIAMETER // 2
                    else:
                        if tolerance == 2 :
                            mielus_belly_sound.play()
                        else :
                            touch_sound.play()
                        other_colors = [c for c in COLORS if c != disk_color_name]
                        new = random.choice(other_colors) if other_colors else random.choice(list(COLORS))
                        old = disk_color_name
                        disk_color_name = new
                        disk_color = COLORS[new]
                        cnt = 0
                        for o2 in obstacles:
                            if o2.color_name == old:
                                cnt += 1
                                o2.color_name = random.choice([c for c in COLORS if c != old])
                                o2.color = COLORS[o2.color_name]
                        if tolerance > 0:
                            time_limit += cnt * 1500
                            tolerance -= 1
                    o.last_touched = now
                    break

            if state == 'PLAYING' and all(o.color_name == disk_color_name for o in obstacles if o.shape in ('rect', 'circle')):
                bonus_sound.play()
                pygame.time.delay(int(0.6 * 1000))

                bonus = remaining*level - 2*level
                if bonus < 0:
                    bonus = 0
                elif bonus > 99:
                    bonus = 99
                

                font = pygame.font.SysFont(None, 100)

                screen.blit(background_victoire[0], (0, 0))

                if bonus == 1:
                    pt_or_pts = "pt"
                else:
                    pt_or_pts = "pts"

                msg = font.render(f"!!! Bonus : {bonus} {pt_or_pts} !!!", True, (165,137,193))            

                #sub1 = font.render(f"score : {score} + {bonus} = {score+bonus}", True, (230,208,241))

                font = pygame.font.SysFont(None, 48)

                sub2 = font.render(f"^^ LET'S PLAY LEVEL {level+1} ^^", True, (207,236,207))

                screen.blit(msg, (SCREEN_WIDTH // 2 - msg.get_width() // 2, SCREEN_HEIGHT // 2 - 350))
                #screen.blit(sub1, (SCREEN_WIDTH // 2 - sub1.get_width() // 2, SCREEN_HEIGHT // 2 -300))
                #screen.blit(sub2, (SCREEN_WIDTH // 2 - sub2.get_width() // 2, SCREEN_HEIGHT // 2 + 290))

                pygame.display.flip()

                score += bonus
                
                if bonus == 1:
                    pt_pts_sound = point_sound
                else:
                    pt_pts_sound = points_sound

                pygame.time.delay(int(0.4 * 1000))
                youpi_sounds = [[you_won_sound,0.4],[numbers_sound[bonus],0.6],[bonus_sound,0.6],[pt_pts_sound,0.4]]

                for i in range(4):
                    youpi_sounds[i][0].play()
                    pygame.time.delay(int(youpi_sounds[i][1] * 1000))

                    screen.blit(background_victoire[i+1], (0, 0))
                    screen.blit(msg, (SCREEN_WIDTH // 2 - msg.get_width() // 2, SCREEN_HEIGHT // 2 - 350))
                    screen.blit(sub1, (SCREEN_WIDTH // 2 - sub1.get_width() // 2, SCREEN_HEIGHT // 2 + 290))
                    pygame.display.flip()

                pygame.time.delay(int(0.6 * 1000))


                level += 1
                x, y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
                disk_color_name = 'BLUE'
                disk_color = COLORS[disk_color_name]
                STAR_DIAMETER = DISK_RADIUS * 2
                obstacles = generate_obstacles(level, disk_color_name, level)
                start_time = now
                time_limit = calcul_time_limit(level)
                tolerance = 2
                annonce_level(level-1)

            if now - start_time > time_limit:
                pygame.mixer.stop()
                state = 'GAMEOVER'

        if state == 'PLAYING':
            screen.blit(background_playing_t[(pygame.time.get_ticks()//1000) % 4], (0, 0))
            for o in obstacles:
                o.draw(screen)
            pygame.draw.circle(screen, disk_color, (int(x), int(y)), DISK_RADIUS)
            remaining = max(0, (time_limit - (now - start_time)) // 1000)

            score_colour = (255, 255, 255)
            if remaining <= 3:
                numbers_sound[remaining].play()
                font = pygame.font.SysFont(None, (4-remaining)*48)
                coef_red = 255 - (255-100*(4-remaining))
                if coef_red > 255 :
                    coef_red = 255
                score_colour = (coef_red, 0, 0)

            txt = font.render(f"Time: {remaining}s  Score: {score} Level : {level}", True, score_colour)
            screen.blit(txt, (20, 20))
            font = pygame.font.SysFont(None, 48)
        elif state == 'START':
            screen.blit(background_acceuil, (0, 0))
            font = pygame.font.SysFont(None, 190)
            msg = font.render(f"!! MIELLUS BELLY !!", True, (249, 140, 182))
            font = pygame.font.SysFont(None, 186)
            msg2 = font.render(f"!! MIELLUS BELLY !!", True, (49, 40, 82))
            font = pygame.font.SysFont(None, 48)
            sub1 = font.render("Press SPACE to start", True, (255, 255, 255))
            sub2 = font.render("barre d'ESPACE pour commencer", True, (255, 255, 255))
            font = pygame.font.SysFont(None, 28)
            sub3 = font.render("!!! HeeeeeeeY !!!", True, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            font = pygame.font.SysFont(None, 48)

            screen.blit(msg, (SCREEN_WIDTH // 2 - msg.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
            screen.blit(msg2, (SCREEN_WIDTH // 2 - msg.get_width() // 2 + 15, SCREEN_HEIGHT // 2 - 55))
            if CLIGNOTANT == 1 :
                screen.blit(sub1, (SCREEN_WIDTH // 2 - sub1.get_width() // 2, SCREEN_HEIGHT // 2 + 110))
            elif CLIGNOTANT == 3 :
                screen.blit(sub2, (SCREEN_WIDTH // 2 - sub2.get_width() // 2, SCREEN_HEIGHT // 2 + 110))
            else :
                screen.blit(sub3, (SCREEN_WIDTH // 2 - sub3.get_width() // 2, SCREEN_HEIGHT // 2 + 110))

            CLIGNOTANT += 1
            if CLIGNOTANT == 4:
                CLIGNOTANT = 0

            sub_control1 = font.render("Controles :", True, (255, 255, 255))
            screen.blit(sub_control1, (SCREEN_WIDTH // 2 - sub_control1.get_width() // 2, SCREEN_HEIGHT // 2 - 260))

            sub_control2 = font.render("Flèches du clavier (Keyboard Arrows) ou ZQSD", True, (255, 255, 255))
            screen.blit(sub_control2, (SCREEN_WIDTH // 2 - sub_control2.get_width() // 2, SCREEN_HEIGHT // 2 - 200))
            pygame.display.flip()

            pygame.time.delay(int(900))
            mielus_belly_sound.play()
            pygame.time.delay(int(500))
            mielus_belly_sound.play()
            pygame.time.delay(int(200))
            mielus_belly_sound.play()
            pygame.time.delay(int(50))
            mielus_belly_sound.play()

        else:
            kermit_no_sound.play()
            msg = font.render(f"Game Over!", True, (255, 255, 255))
            sub0 = font.render("SECRET : Press H for Mielus belly", True, (255, 255, 255))
            sub1 = font.render(f"Level {level}            Score {score}", True, (255, 255, 255))
            sub2 = font.render("Press SPACE to restart", True, (255, 255, 255))
            fortune = round(score * level**2/1000, 2)
            if fortune == 1:
                monnaie = monnaies_singulier[indice_monnaie]
            else :
                monnaie = monnaies_pluriel[indice_monnaie]

            if fortune >= 0:
                sub3 = font.render(f"tu as gagné {fortune} {monnaie} ", True, (255, 255, 255))
            else :
                sub3 = font.render(f"Tu es endetté. Donner argent : {-1*fortune} {monnaie} ", True, (255, 255, 255))

            sub_control1 = font.render("Controles :", True, (255, 255, 255))
            sub_control2 = font.render("Flèches du clavier (Keyboard Arrows) ou ZQSD", True, (255, 255, 255))

            if state == 'GAMEOVER' :
                tab_game_over = background_apopo
            elif state == 'GAMEOVER_STAR' :
                tab_game_over = background_death_star

            for i in range(4):
                screen.blit(tab_game_over[i], (0, 0))
                if score > 1000:
                        screen.blit(sub0, (SCREEN_WIDTH // 2 - sub0.get_width() // 2, SCREEN_HEIGHT // 2 - 110))
                screen.blit(msg, (SCREEN_WIDTH // 2 - msg.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
                screen.blit(sub1, (SCREEN_WIDTH // 2 - sub1.get_width() // 2, SCREEN_HEIGHT // 2 + 10))
                screen.blit(sub2, (SCREEN_WIDTH // 2 - sub2.get_width() // 2, SCREEN_HEIGHT // 2 + 70))
                screen.blit(sub3, (SCREEN_WIDTH // 2 - sub3.get_width() // 2, SCREEN_HEIGHT // 2 + 130))
                screen.blit(sub_control1, (SCREEN_WIDTH // 2 - sub_control1.get_width() // 2, SCREEN_HEIGHT // 2 - 260))
                screen.blit(sub_control2, (SCREEN_WIDTH // 2 - sub_control2.get_width() // 2, SCREEN_HEIGHT // 2 - 200))
                pygame.display.flip()
                pygame.time.delay(int(250))



        pygame.display.flip()


if __name__ == '__main__':
    main()
