from PIL import Image
import urllib.request
import random
import time


class Character():
    def __init__(self, name, hp, power, mp=0, magic_power=0):  # 기본값이 적힌 인자는 맨 뒤에
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power
        self.max_mp = mp
        self.mp = mp
        self.magic_power = magic_power

    def attack(self, other):  # player가 (1.일반공격) 선택시
        damage = random.randint(self.power - 10, self.power + 10)
        if damage == 0:
            print(f"{self.name}의 💫일반공격이 실패했습니다!")
        elif damage < 0:
            other.hp = max(other.hp - damage, 0)
            print(f"{self.name}의 💫일반공격 실패! 🚨{other.name}의 HP가 충전되었습니다🚨")
        else:
            if other.hp > damage:
                other.hp = max(other.hp - damage, 0)
                print(f"{self.name}의 공격! {other.name}에게 {str(damage)}의 데미지🩸를 입혔습니다.")
            elif other.hp < damage:
                print(
                    f"{self.name}의 공격! {other.name}에게 {str(other.hp)}의 데미지🩸를 입혔습니다.")
                other.hp = 0
                print(f"{other.name}이(가) 쓰러졌습니다. "+str(count) +
                      f"번의 치열한 전투 끝에 {self.name}의 승리!\n\n🔺🔺🔺🔺🔺\n\n수고하셨습니다🤍")

    def magic_attack(self, other):  # player가 (2.마법공격) 선택시
        damage = random.randint(self.magic_power - 20, self.magic_power + 20)
        if self.mp == 0:
            print(f"💫mp가 부족해 {self.name}의 💫마법공격이 실패했습니다!")
        else:
            if damage == 0:
                print(f"{self.name}의 💫마법공격이 실패했습니다!")
            elif damage < 0:
                other.hp = max(other.hp - damage, 0)
                print(
                    f"{self.name}의 💫마법공격 실패! 🚨{other.name}의 HP가 {str(-damage)}만큼 충전되었습니다🚨")
            else:
                self.mp = max(self.mp - damage, 0)
                if other.hp > damage:
                    other.hp = max(other.hp - damage, 0)
                    print(
                        f"{self.name}의 공격! {other.name}에게 {str(damage)}의 데미지🩸를 입혔습니다.")
                elif other.hp < damage:
                    print(
                        f"{self.name}의 공격! {other.name}에게 {str(other.hp)}의 데미지🩸를 입혔습니다.")
                    other.hp = 0
                    print(f"{other.name}이(가) 쓰러졌습니다. "+str(count) +
                          f"번의 치열한 전투 끝에 {self.name}의 승리!\n\n🔺🔺🔺🔺🔺\n\n수고하셨습니다🤍")

    def heal(self):  # player가 (4.힐) 선택시
        self.hp += (self.max_hp)*0.5

    def show_status(self):  # player 상태보기 (HP, MP)
        print(
            f"🔋{self.name}의 상태: (HP) {int(self.hp)}/{self.max_hp} (MP) {self.mp}/{self.max_mp}")


class Monster(Character):
    def miss(self, other):  # player가 (3.회피하기) 선택시
        damage = random.randint(self.power - 20, self.power - 10)
        if damage == 0:
            print(f"회피 성공! {self.name}의 💫공격이 빗나갔습니다!")
        elif damage < 0:
            other.hp = max(other.hp - damage, 0)
            print(
                f"회피 성공! 🚑{other.name}의 HP가 {str(-damage)}만큼 충전되었습니다🚑")
        else:
            if other.hp > damage:
                other.hp = max(other.hp - damage, 0)
                print(
                    f"{self.name}의 틈새공격! {other.name}에게 {str(damage)}의 데미지🩸를 입혔습니다.")
            elif other.hp < damage:
                print(
                    f"{self.name}의 틈새공격! {other.name}에게 {str(other.hp)}의 데미지🩸를 입혔습니다.")
                other.hp = 0
                print(f"{other.name}이(가) 쓰러졌습니다. "+str(count) +
                      f"번의 치열한 전투 끝에 {self.name}의 승리!\n\n🔺🔺🔺🔺🔺\n\n수고하셨습니다🤍")

    def show_status(self):  # monster 상태보기 (HP)
        print(f"🔋{self.name}의 상태: (HP) {self.hp}/{self.max_hp}")


# 플레이어 정보
print("\n가보자고!")
time.sleep(0.5)
player_name = input("\n이름을 입력하세요: ")
while player_name == "":
    print("플레이어의 이름을 입력하세요!!")
    player_name = input("Player name: ")
print("\n어떤 무기를 사용하시겠습니까?")
player_weapon = input("1.양손검 2.총 3.지팡이: ")
while player_weapon == "" or player_weapon.isalpha() or int(player_weapon) > 3:
    print("\n무기를 선택하세요!!")
    player_weapon = input("1.양손검 2.총 3.지팡이: ")
# 주무기_양손검
if player_weapon == "1":
    print("\n보조 무기를 선택하세요. 능력치가 달라집니다.")
    player_assist_weapon = input("1.방패 2.총알 3.올빼미: ")
    while player_assist_weapon == "" or player_assist_weapon.isalpha() or int(player_assist_weapon) > 3:
        print("\n보조 무기를 선택하세요!!")
        player_assist_weapon = input("1.방패 2.총알 3.올빼미: ")
    if player_assist_weapon == "1":  # 양손검_방패
        player = Character(player_name, 200, 30, 30, 15)
    elif player_assist_weapon == "2":  # 양손검_총알
        player = Character(player_name, 180, 20, 30, 15)
    elif player_assist_weapon == "3":  # 양손검_올빼미
        player = Character(player_name, 180, 20, 50, 30)
# 주무기_총
elif player_weapon == "2":
    print("\n보조 무기를 선택하세요. 능력치가 달라집니다.")
    player_assist_weapon = input("1.방패 2.총알 3.올빼미: ")
    while player_assist_weapon == "" or player_assist_weapon.isalpha() or int(player_assist_weapon) > 3:
        print("\n보조 무기를 선택하세요!!")
        player_assist_weapon = input("1.방패 2.총알 3.올빼미: ")
    if player_assist_weapon == "1":  # 총_방패
        player = Character(player_name, 150, 20, 30, 15)
    elif player_assist_weapon == "2":  # 총_총알
        player = Character(player_name, 130, 30, 30, 15)
    elif player_assist_weapon == "3":  # 총_올빼미
        player = Character(player_name, 130, 20, 50, 30)
# 주무기_지팡이
elif player_weapon == "3":
    print("\n보조 무기를 선택하세요. 능력치가 달라집니다.")
    player_assist_weapon = input("1.방패 2.총알 3.올빼미: ")
    while player_assist_weapon == "" or player_assist_weapon.isalpha() or int(player_assist_weapon) > 3:
        print("\n보조 무기를 선택하세요!!")
        player_assist_weapon = input("1.방패 2.총알 3.올빼미: ")
    if player_assist_weapon == "1":  # 지팡이_방패
        player = Character(player_name, 130, 10, 100, 30)
    elif player_assist_weapon == "2":  # 지팡이_총알
        player = Character(player_name, 100, 10, 100, 30)
    elif player_assist_weapon == "3":  # 지팡이_올빼미
        player = Character(player_name, 100, 20, 120, 50)

# 몬스터 정보
monster_check = "2"
while monster_check == "2":
    print("\n어떤 몬스터를 처리하시겠습니까?")
    monster_name = input("1.해파리 2.좀비 3.베어: ")
    while monster_name == "" or monster_name.isalpha() or int(monster_name) > 3:
        print("\n몬스터를 선택하세요!!")
        monster_name = input("1.해파리 2.좀비 3.베어: ")
    if monster_name == "1":  # 해파리
        monster = Monster("해파리", 100, 10)
    elif monster_name == "2":  # 좀비
        monster = Monster("좀비", 150, 15)
    elif monster_name == "3":  # 베어
        monster = Monster("베어", 200, 20)

    # 몬스터 귀여운 이미지 띄우기
    if monster_name == "1":  # 해파리
        urllib.request.urlretrieve(
            'https://img.freepik.com/premium-vector/cute-jellyfish_795963-13.jpg', 'jellyfish.jpg')
        image = Image.open('jellyfish.jpg')
    elif monster_name == "2":  # 좀비
        urllib.request.urlretrieve(
            'https://img.freepik.com/free-vector/cute-zombie-frankenstein-from-the-grave-cartoon-illustration-people-halloween-concept-isolated-flat-cartoon-style_138676-2720.jpg', 'zombie.jpg')
        image = Image.open('zombie.jpg')
    elif monster_name == "3":  # 베어
        urllib.request.urlretrieve(
            'https://mblogthumb-phinf.pstatic.net/MjAyMTA5MzBfMjEg/MDAxNjMyOTgwMTY0NTc0.ivC-fbO8uQj0VUNP9Iij-pptOdWMIA9oPeXVFiEoXqAg.BKZn6BcweHNJpwn5HT0AyJLlfJpy7b0_arKcE6cIPe4g.PNG.daehan4work/1.png?type=w800', 'bear.jpg')
        image = Image.open('bear.jpg')
    image.show()

    # 몬스터 재확인
    print("\n"+monster.name+"와 싸우실 수 있겠어요~???~?")
    monster_check = input("1.당연!💪 2.다시 고를까..🤔 3.도..도망..run🏃‍♂️: ")

if monster_check == "3":
    print("\n쫄보시군요! 다음에 다시 만나요🖐")
    raise SystemExit

# 게임 시작
print("\n🔻🔻🔻🔻🔻\n\n지금부터 게임을 시작하지.")
player.show_status()
monster.show_status()
count = 1
heal_count = 0

while player.hp > 0 and monster.hp > 0:
    time.sleep(1)
    print("\n"+str(count)+"번째 전투를 시작합니다👊\n어떤 공격을 하시겠습니까?")
    if player.hp > (player.max_hp)*0.5:
        player_attack = input("1.일반공격 2.마법공격 3.회피하기: ")
        while player_attack == "" or player_attack.isalpha() or int(player_attack) > 3:
            print("\n공격을 선택하세요!!")
            player_attack = input("1.일반공격 2.마법공격 3.회피하기: ")
    elif player.hp <= (player.max_hp)*0.5 and heal_count == 0:
        player_attack = input("1.일반공격 2.마법공격 3.회피하기 4.힐: ")
        while player_attack == "" or player_attack.isalpha() or int(player_attack) > 4:
            print("\n공격을 선택하세요!!")
            player_attack = input("1.일반공격 2.마법공격 3.회피하기 4.힐: ")
    time.sleep(0.5)
    if player_attack == "1":  # 일반공격
        player.attack(monster)
        if monster.hp > 0:
            monster.attack(player)
            if player.hp > 0 and monster.hp > 0:
                player.show_status()
                monster.show_status()
                count += 1
    elif player_attack == "2":  # 마법공격
        player.magic_attack(monster)
        if monster.hp > 0:
            monster.attack(player)
            if player.hp > 0 and monster.hp > 0:
                player.show_status()
                monster.show_status()
                count += 1
    elif player_attack == "3":  # 회피하기
        monster.miss(player)
        if player.hp > 0 and monster.hp > 0:
            player.show_status()
            monster.show_status()
            count += 1
    elif player_attack == "4":  # 힐
        player.heal()
        print("🚑HP가 충전되었습니다🚑 중꺽마!")
        player.show_status()
        monster.show_status()
        count += 1
        heal_count += 1
