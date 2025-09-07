Fork of https://github.com/henriqueannicchino/towerDefense

Defenders of the Realm: Rise of the Guardians
=============================================

In "Defenders of the Realm: Rise of the Guardians," immerse yourself in an epic tower defense adventure where the fate of the realm lies in your hands. As malevolent forces threaten to overrun the once peaceful kingdom, it's up to you to command an elite team of Guardians to defend against the hordes of darkness.

The game features a stunning fantasy world, beautifully rendered with breathtaking landscapes and visually engaging environments. As a formidable strategist, you must strategically position your defensive towers across key locations, utilizing their unique abilities and upgrading them to unleash devastating attacks upon your enemies.

Choose your Guardians wisely, each with their distinct powers and skills, as you lead them into intense battles against the encroaching waves of sinister creatures. Whether it's archers unleashing a volley of arrows, mages conjuring elemental storms, or mighty warriors wielding enchanted blades, the fate of the realm lies in the coordination and mastery of your Guardians' abilities.

Prepare for an onslaught of challenges, as the enemy's strength and tactics evolve with each passing wave. Adapt your strategies, analyze the battlefield, and devise clever traps to fend off even the most cunning adversaries. Unlock powerful relics and artifacts that bestow extraordinary bonuses upon your defenses, pushing the boundaries of your tactical prowess.

As the battle rages on, you will encounter legendary bosses that lead the onslaught. These colossal foes demand impeccable timing and strategic coordination to overcome. Unite your Guardians and unleash their ultimate abilities to face these formidable adversaries in heart-pounding, climactic showdowns.

With each victory, you will earn rewards to enhance your Guardians and fortifications, strengthening your chances of surviving the ever-escalating threats. Engage in thrilling PvP battles, competing against other players worldwide to prove your strategic superiority and claim the title of the ultimate Guardian.

Are you ready to take up the mantle of the Guardians and defend the realm against darkness? Unleash your tactical brilliance, harness the power of your Guardians, and embrace the journey to become the true Defenders of the Realm!

Commits
=======
Caso ocorra um erro como o abaixo tente no Linux.

.. code-block:: shell
	error: invalid path 'longintrepr.h:Zone.Identifier'
	error: could not detach HEAD

...
===
Rodar `buildozer android clean` antes de `./longintrepr.h.copy.py`

.. code-block:: shell
    export PATH=$PATH:~/.local/bin/
	buildozer -v android debug
	sudo su
	/root/.local/bin/buildozer init
	/root/.local/bin/buildozer android clean
	python3 "/home/user/JogoS/tower-defense/longintrepr.h"
	sudo chown user:user -R /home/user
	/root/.local/bin/buildozer -v android debug
	buildozer android clean
	sudo apt update
	sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
	pip3 install --user --upgrade Cython==0.29.33 virtualenv  # the --user should be removed if you do this in a venv
	pip3 install --user --upgrade buildozer

	# add the following line at the end of your ~/.bashrc file
	export PATH=$PATH:~/.local/bin/

	user@DESKTOP-Q1J3N0J:~/JogoS/tower-defense$ cat /home/user/JogoS/tower-defense/.buildozer/android/platform/python-for-android/pythonforandroid/recipes/hostpython3/patches/pyconfig_detection.patch
	--- /usr/lib/python3.10/site.py 2025-09-02 15:30:48.738182781 -0400
	+++ /usr/lib/python3.10-new/site.py     2025-09-02 15:33:08.155207065 -0400
	@@ -543,7 +543,8 @@
						if key == 'include-system-site-packages':
							system_site = value.lower()
						elif key == 'home':
	-                        sys._home = value
	+                        #sys._home = value
	+                        pass

			sys.prefix = sys.exec_prefix = site_prefix


	user@DESKTOP-Q1J3N0J:~/JogoS/tower-defense$ diff -Nru /usr/lib/python3.10/site.py /usr/lib/python3.10-new/site.py
	--- /usr/lib/python3.10/site.py 2025-09-02 15:30:48.738182781 -0400
	+++ /usr/lib/python3.10-new/site.py     2025-09-02 15:33:08.155207065 -0400
	@@ -543,7 +543,8 @@
						if key == 'include-system-site-packages':
							system_site = value.lower()
						elif key == 'home':
	-                        sys._home = value
	+                        #sys._home = value
	+                        pass
